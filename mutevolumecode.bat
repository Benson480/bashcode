@echo off
Title Switch Mute Speaker Volume
(echo CreateObject("WScript.Shell"^).SendKeys chr(173^))>"%Temp%\%~n0.vbs"
cscript //NoLogo "%Temp%\%~n0.vbs"