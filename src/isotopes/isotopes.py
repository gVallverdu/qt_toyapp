#!/usr/bin/env python
# coding: utf-8

from pathlib import Path
import numpy as np
import pandas as pd

__all__ = ["read_isotopes_data", "Element", "Isotope", "VERSION", "DATA_FILE",
           "NIST_DATA"]

def read_isotopes_data(path):
    """ Read isotopes data in NIST data base and returns a data frame """

    path = Path(path)

    with path.open("r") as f:
        data = dict()
        el_data = list()
        for line in f:
            if line.strip() == "":
                el_data.append(data)
                data = dict()
            elif line[0] == "#":
                continue
            else:
                key, value = line.strip().split("=")
                if key.strip() == "Atomic Symbol":
                    data["element"] = value.strip()
                elif key.strip() == "Atomic Number":
                    data["atomic number"] = int(value)
                elif key.strip() == "Relative Atomic Mass":
                    value = "".join(value.split("(")).split(")")[0].strip("#")
                    data["exact mass"] = np.float64(value)
                elif key.strip() == "Mass Number":
                    data["mass number"] = int(value)
                elif key.strip() == "Standard Atomic Weight":
                    if value.strip() == "":
                        value = np.nan
                    else:
                        if "[" in value:
                            value = value.strip().strip("[]")
                            if "," in value:
                                vmin, vmax = value.split(",")
                            else:
                                vmin, vmax = value, value
                            value = (np.float64(vmin) + np.float64(vmax)) / 2
                        elif "(" in value:
                            value = "".join(value.split("(")).split(")")[0]
                    data["standard atomic weight"] = np.float64(value)
                elif key.strip() == "Isotopic Composition":
                    if value == " 1":
                        value = np.float64(value)
                    elif value.strip() == "":
                        value = np.nan
                    else:
                        value = "".join(value.split("(")).split(")")[0]
                    data["isotopic abundance"] = np.float64(value)

    return pd.DataFrame(el_data)


def superscripts(word):
    """ Method to create the superscripts for the isotopes.

    Args:
        word (str): a string containing the isotope name
    """
    superscript_map = {"0": "⁰", "1": "¹", "2": "²", "3": "³", "4": "⁴",
                       "5": "⁵", "6": "⁶", "7": "⁷", "8": "⁸", "9": "⁹"}
    trans = str.maketrans(superscript_map)
    word = word.translate(trans)

    return word

# electron mass
# source (doi): 10.1103/PhysRevLett.75.3598 
# atomic mass units (Da)
ELECTRON_MASS = 0.0005485799

# Reading NIST DATA
# https://www.nist.gov/pml/atomic-weights-and-isotopic-compositions-relative-atomic-masses
# TXT = "AtomicWeightsAndIsotopicCompNIST2019.txt"
TXT = Path("resources/data/atomicWeightsAndIsotopicDataNIST2021.txt")
VERSION = 20210913
DATA_FILE = Path(__file__).absolute().parents[1] / TXT

NIST_DATA = read_isotopes_data(DATA_FILE)
NIST_DATA["super symbol"] = NIST_DATA.apply(
    lambda row: f'{superscripts(str(row["mass number"]))}{row["element"]}',
    axis="columns"
)
NIST_DATA["symbol"] = NIST_DATA.apply(
    lambda row: f'{row["mass number"]}{row["element"]}',
    axis="columns"
)


class Element:
    """ This class represent a chemical element """

    def __init__(self, Z=1):
        """ Return an element according to its atomic number """

        self._Z = int(Z)

        data = NIST_DATA[NIST_DATA["atomic number"] == self.Z]
        data = data.sort_values("isotopic abundance", ascending=False)
        if len(data) == 0:
            raise ValueError(f"Element Z = {Z} does not exist.")
        else:
            self.data = data.iloc[0].to_dict()

    @property
    def Z(self):
        """ Atomic number """
        return self._Z

    @property
    def atomic_number(self):
        """ Atomic number """
        return self._Z

    @property
    def symbol(self):
        """ Element symbol """
        return self.data["element"]

    @property
    def atomic_weight(self):
        """ Standard atomic weight"""
        return self.data["standard atomic weight"]

    @property
    def mass_number_most_abundant(self):
        """ The mass number of the most abundant isotope of the element """
        return self.data["mass number"]

    @property
    def exact_mass_most_abundant(self):
        """ The exact mass of the most abundant isotope of the element """
        return self.data["exact mass"]

    @classmethod
    def from_str(cls, symbol):
        """ Return an element from its symbol """
        data = NIST_DATA[NIST_DATA["element"] == symbol]
        if len(data) == 0:
            raise ValueError(f"Element '{symbol}' does not exist.")
        else:
            return cls(data.iloc[0, 0])

    def get_isotopes(self, dropna=False):
        """ Returns the list of isotopes of the element.

        Args:
            dropna (bool): Either to drop isotopes with Nan values or not

        Returns
            A DataFrame with all the isotopes of the element.
        """
        return Isotope.get_isotopes_data(atomic_numbers=[self.Z], dropna=dropna)

    def to_dict(self):
        """ return a dict version of the isotop data """
        return {"atomic number": self.Z,
                "symbol": self.symbol,
                "standard atomic weight": self.atomic_weight,
                "mass number most abundant": self.mass_number_most_abundant,
                }

    def __hash__(self):
        return self.Z

    def __str__(self):
        return f"{self.symbol}"

    def __repr__(self):
        return f"{self.symbol}; Element({self.Z})"

    def __eq__(self, other):
        if isinstance(other, Element):
            return self.Z == other.Z
        elif isinstance(other, int):
            return self.Z == other
        elif isinstance(other, str):
            return self.symbol == other
        else:
            raise TypeError("Cannot compare Element with {type(other)}.")


class Isotope:
    """ This class represent an isotop and provides related properties 
    such as its exact mass and the isotopic abundance. 

    version:
        NIST file version

    data_file:
        Path of the NIST data file

    """

    # data base info
    version = VERSION
    data_file = DATA_FILE

    # compute mass differences
    abundance_exist = NIST_DATA["isotopic abundance"].notna()
    ab_NIST_DATA = NIST_DATA[abundance_exist]
    _delta_matrix = ab_NIST_DATA["exact mass"].values \
                  - ab_NIST_DATA["exact mass"].values[:, np.newaxis]

    def __init__(self, Z=1, A=1):
        """ Return an isotope defined from its atomic number and its
        mass number.

        Args:
            Z (int): atomic number
            A (int): mass number
        """
        self.Z = int(Z)
        self.A = int(A)

        data = NIST_DATA[
            (NIST_DATA["atomic number"] == int(Z)) & (
                NIST_DATA["mass number"] == int(A))
        ]
        if len(data) == 0:
            raise ValueError(f"Isotop Z = {Z}, A = {A} does not exist.")
        elif len(data) > 1:
            print(data)
            raise ValueError("Several isotop correspond to this values")
        else:
            self._data = data.iloc[0].to_dict()

    @property
    def atomic_number(self):
        """ Atomic number """
        return self.Z

    @property
    def symbol(self):
        """ Isotope symbol written as AX such as 13C for carbon with A = 13 """
        return self._data["symbol"]

    @property
    def super_symbol(self):
        """ Isotope symbol written with a super script font """
        return self._data["super symbol"]

    @property
    def mass_number(self):
        """ Mass number or nominal mass """
        return self.A

    @property
    def exact_mass(self):
        """ Exact mass in g.mol-1 """
        return self._data["exact mass"]

    @property
    def abundance(self):
        """ Isotopic aboundance """
        return self._data["isotopic abundance"]

    @property
    def element(self):
        """ The element of this isotope """
        return self._data["element"]

    @classmethod
    def find_mass_split(cls, requested_split=1.003355, tolerance=0.0001, 
                        superscript=False, sort=True):
        """ Find a mass gap between two isotopes.

        Args:
            requested_split (float): the gap between isotopes' masses
            tolerance (float): the tolerance to find the candidates
            superscript (bool): if True, name use superscript symbol
            sort (bool): if True, sort the candidates using the lowest absolute error

        Returns:
            A list of candidates and min index
        """
        candidates = list()

        idx = np.where(np.abs(cls._delta_matrix - requested_split) < tolerance)
        icandidates = np.stack(idx).transpose()

        if len(icandidates) > 0:
            # look for min value
            minval = 1e10
            for i, j in icandidates:
                error = cls._delta_matrix[i, j] - requested_split
                if abs(error) < abs(minval):
                    minval = error

                if superscript:
                    name = (f'{cls.ab_NIST_DATA.iloc[i]["super symbol"]}'
                            f' - {cls.ab_NIST_DATA.iloc[j]["super symbol"]}')
                else:
                    name = (f'{cls.ab_NIST_DATA.iloc[i]["symbol"]}' 
                            f' - {cls.ab_NIST_DATA.iloc[j]["symbol"]}')

                candidates.append((name, error))

        # sort according to the lowest absolute error
        if sort:
            candidates = sorted(candidates, key=lambda x: abs(x[1]))

        return candidates

    @classmethod
    def get_most_abundant(cls, elements=None, atomic_numbers=None):
        """ From the list of elements return a data frame with exact masses
        of the most abundant isotopes. A list of element symbols, as string, 
        or atomic numbers, as integer must be provided.

        Args:
            elements (list): List of element symbols, ``["C", "H", "N"]``
            atomic_numbers (list): List of atomic numbers, ``[6, 1, 7]``

        Returns
            A DataFrame with the most abundant isotope for each element.
        """

        sel = cls.get_isotopes_data(elements, atomic_numbers)
        sel = sel.loc[sel.groupby(
            "element")["isotopic abundance"].idxmax()].copy()

        return sel.reset_index(drop=True)

    @classmethod
    def get_isotopes_list(cls, elements=None, atomic_numbers=None, dropna=False):
        """ From the list of elements return a list of Isotope objects which
        represent the existing isotopes for each element. A list of element 
        symbols, as string, or atomic numbers, as integer must be provided.
        If dropna is True, only isotopes with existing abundance values are
        returned.

        Args:
            elements (list): List of element symbols, ``["C", "H", "N"]``
            atomic_numbers (list): List of atomic numbers, ``[6, 1, 7]``
            dropna (bool): Either to drop isotopes with Nan values or not

        Returns
            A list of Isotope objects.
        """
        data = cls.get_isotopes_data(elements, atomic_numbers, dropna)

        isotopes = list()
        for _, (Z, A) in data[["atomic number", "mass number"]].iterrows():
            isotopes.append(cls(Z, A))

        return isotopes

    @staticmethod
    def get_isotopes_data(elements=None, atomic_numbers=None, dropna=False):
        """ From the list of elements return a data frame with the corresponding
        isotopes. A list of element symbols, as string, or atomic numbers, 
        as integer must be provided.

        Args:
            elements (list): List of element symbols, ``["C", "H", "N"]``
            atomic_numbers (list): List of atomic numbers, ``[6, 1, 7]``
            dropna (bool): Either to drop isotopes with Nan values or not

        Returns
            A DataFrame with the all the isotopes for each element.
        """
        if elements:
            try:
                sel = NIST_DATA[NIST_DATA.element.isin(elements)].copy()
            except TypeError:
                raise TypeError("elements must be a list object.")
        elif atomic_numbers:
            try:
                sel = NIST_DATA[NIST_DATA["atomic number"].isin(
                    atomic_numbers)].copy()
            except TypeError:
                raise TypeError("atomic_numbers must be a list object.")
        else:
            raise ValueError("Invalid arguments. Need a list of elements"
                             " or a list of atomic numbers.")

        if len(sel) == 0:
            raise ValueError("elements or atomic numbers not found.\n"
                             f"elements: {elements}\n"
                             f"atomic_numbers: {atomic_numbers}")

        # add a column with isotop names with superscript format
        sel["isotope"] = sel.apply(
            lambda r: f'{superscripts(str(r["mass number"]))}{r["element"]}',
            axis="columns"
        )

        if dropna:
            return sel.dropna().reset_index(drop=True)
        else:
            return sel.reset_index(drop=True)

    def to_dict(self):
        """ return a dict version of the isotop data """
        return {"atomic number": self.Z, "mass number": self.A,
                "symbol": self.symbol,
                "element": self._data["element"],
                "exact mass": self.exact_mass,
                "isotopic abundance": self.abundance}

    def __hash__(self):
        return (self.Z, self.A)

    def __str__(self):
        # TODO using superscript ?
        # return f"{superscripts(self.A)}{self.symbol}""
        return self.data["symbol"]

    def __repr__(self):
        return f"^{self.A}{self.element}; Isotope({self.Z}, {self.A})"

    def __eq__(self, other):
        return isinstance(other, Isotope) and self.Z == other.Z and self.A == other.A
    
    def __add__(self, other):
        return self.exact_mass + other.exact_mass

    def __sub__(self, other):
        return self.exact_mass - other.exact_mass




