def ExcelExample():
  
  # Get the sheet of the Excel file
  excelFile = Excel.Open("C:\\Users\\SA118193\\Desktop\\Book1.xlsx")
  excelSheet = excelFile.SheetByTitle["Sheet1"]
  
  col=excelFile.ActiveSheet.ColumnCount
  row=excelFile.ActiveSheet.RowCount
  
  for i in range(1,col+1):
   for j in range(1,row+1):
    Log.Message(excelSheet.Cell[i,j].Value)
    
  
  
  # Read data from the Excel file
  #valueA = excelSheet.Cell["A", 3].Value
  #valueB = excelSheet.Cell[2, 3].Value
  #valueC = excelSheet.CellByName["C3"].Value
  
  
  

          