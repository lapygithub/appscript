#!/usr/bin/env pythonw

from osax import *

# create a ScriptingAddition instance for StandardAdditions
sa = ScriptingAddition()

sa.beep(2)

sa.activate() # bring current process to front so dialog box will be visible
print sa.display_dialog('Hello World!')
# {k.button_returned: u'OK'}

print sa.path_to(k.scripts_folder, from_=k.local_domain)
# mactypes.Alias(u'/Library/Scripts')