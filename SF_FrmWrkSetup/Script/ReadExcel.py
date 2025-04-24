def ReadAccountDataFromExcel(expath):
    Excel = Sys.OleObject["Excel.Application"]
    Excel.Workbooks.Open(expath)
  
    RowCount = Excel.ActiveSheet.UsedRange.Rows.Count
    ColumnCount = Excel.ActiveSheet.UsedRange.Columns.Count
    val=VarToString(Excel.Cells.Item[2, 1])
    #Log.Message("Row: " + val);
    return val
    Excel.Quit();
    

  
  
  

          