#---------------------------------------------------------------------------
# Name:        etg/textdlg.py
# Author:      Robin Dunn
#
# Created:     10-Aug-2012
# Copyright:   (c) 2012 by Total Control Software
# License:     wxWindows License
#---------------------------------------------------------------------------

import etgtools
import etgtools.tweaker_tools as tools

PACKAGE   = "wx"   
MODULE    = "_core"
NAME      = "textdlg"   # Base name of the file to generate to for this script
DOCSTRING = ""

# The classes and/or the basename of the Doxygen XML files to be processed by
# this script. 
ITEMS  = [ "wxTextEntryDialog",
           "wxPasswordEntryDialog",
           ]    
    
#---------------------------------------------------------------------------

def run():
    # Parse the XML file(s) building a collection of Extractor objects
    module = etgtools.ModuleDef(PACKAGE, MODULE, NAME, DOCSTRING)
    etgtools.parseDoxyXML(module, ITEMS)
    
    #-----------------------------------------------------------------
    # Tweak the parsed meta objects in the module object as needed for
    # customizing the generated code and docstrings.
    
    module.addHeaderCode("#include <wx/textdlg.h>")
    module.find('wxGetTextFromUserPromptStr').type = 'const char*'
    module.find('wxGetPasswordFromUserPromptStr').type = 'const char*'
    
    c = module.find('wxTextEntryDialog')
    assert isinstance(c, etgtools.ClassDef)
    tools.fixTopLevelWindowClass(c)
    
    
    c = module.find('wxPasswordEntryDialog')
    tools.fixTopLevelWindowClass(c)
    
    
    #-----------------------------------------------------------------
    tools.doCommonTweaks(module)
    tools.runGenerators(module)
    
    
#---------------------------------------------------------------------------
if __name__ == '__main__':
    run()

