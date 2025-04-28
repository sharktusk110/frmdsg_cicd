def ReadAccountDataFromExcel(expath,row):
    Excel = Sys.OleObject["Excel.Application"]
    Excel.Workbooks.Open(expath)
  
    RowCount = Excel.ActiveSheet.UsedRange.Rows.Count
    ColumnCount = Excel.ActiveSheet.UsedRange.Columns.Count
    val=VarToString(Excel.Cells.Item[row, 1])
    #Log.Message("Row: " + val);
    return val
    Excel.Quit();
    
def ReadConfigDataFromExcel(expath,row):
        Excel = Sys.OleObject["Excel.Application"]
        Excel.Workbooks.Open(expath)
        config=[]
        RowCount = Excel.ActiveSheet.UsedRange.Rows.Count
        ColumnCount = Excel.ActiveSheet.UsedRange.Columns.Count
        for j in range(2,8):
         config.append(VarToString(Excel.Cells.Item[row, j]))
        #Log.Message("Row: " + val);
        return config
        Excel.Quit();
    

  
  
  

          