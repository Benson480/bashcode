Set objExcel = CreateObject("Excel.Application")
objExcel.Application.Run "C:\Users\bmwangi\OneDrive - SLI\Desktop\coding\programming\saveallexcelcode.xlsm'!module1.saveAllOpenExcels"
objExcel.DisplayAlerts = False
objExcel.Application.Quit
Set objExcel = Nothing
