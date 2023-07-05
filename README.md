# KatanaCentOSLauncher 

# Launcher features custom renderer scripts to adjust based on installed katana versions, renderers, and respective versions. 
# If you have another renderer in the /Renderers folder. It will be used, but lacking functionality.

# The custom scripts use two envVars to achieve the flexibility. These are set when pressing the Launch button and can be used in any script:
#     $KATANA_VERSION - The selected version of Katana. EX: '6.0v2'
#     $RENVER - The selected verion of the specified renderer. EX: '4.2.2.1' (for Arnold)
#     ${KATANA_VERSION:0:3} - Can be used to represent the major version of Katana. EX'6.0'
