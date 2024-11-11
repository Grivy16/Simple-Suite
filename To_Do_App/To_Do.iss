[Setup]
AppName=To Do
AppVersion=1.0
DefaultDirName={localappdata}\To_Do
DefaultGroupName=To_Do
OutputDir=output
OutputBaseFilename=To_Do_setup
Compression=lzma
SolidCompression=yes

[Files]
Source: "C:\Users\samue\OneDrive\Documents\code\Python\To-do\dist\Main.exe"; DestDir: "{app}"; Flags: ignoreversion

[Icons]
Name: "{group}\To_Do"; Filename: "{app}\Main.exe"
Name: "{group}\Désinstaller_To_Do"; Filename: "{uninstallexe}"

[Run]
Filename: "{app}\Main.exe"; Description: "{cm:LaunchProgram,MonApplication}"; Flags: nowait postinstall skipifsilent
