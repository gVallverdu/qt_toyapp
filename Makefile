###### EDIT ##################### 
#Directory with ui and resource files
UI_DIR = src/resources/ui
# RESOURCE_DIR = src/resources
 
#Directory for compiled resources
COMPILED_DIR = src/gui
 
#UI files to compile
UI_FILES = isotopinator.ui main.ui plot_widget.ui last_widget.ui
#Qt resource files to compile
# RESOURCES = images.qrc 
 
#pyuic4 and pyrcc4 binaries
# PYUIC = pyuic4.bat
PYUIC = pyuic5
# PYRCC = pyrcc4
 
RM = rm -v

#################################
# DO NOT EDIT FOLLOWING
 
COMPILED_UI = $(UI_FILES:%.ui=$(COMPILED_DIR)/ui_%.py)
# COMPILED_RESOURCES = $(RESOURCES:%.qrc=$(COMPILED_DIR)/%_rc.py)
 
# all : resources ui 
all: ui 
 
# resources: $(COMPILED_RESOURCES) 

ui: $(COMPILED_UI)
 
$(COMPILED_DIR)/ui_%.py : $(UI_DIR)/%.ui
	$(PYUIC) $< -o $@
 
# $(COMPILED_DIR)/%_rc.py : $(RESOURCE_DIR)/%.qrc
# 	$(PYRCC) $< -o $@
 
clean : 
	$(RM) $(COMPILED_UI) $(COMPILED_RESOURCES) $(COMPILED_UI:.py=.pyc) $(COMPILED_RESOURCES:.py=.pyc)  