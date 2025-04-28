import ReadExcel
import Order_Configuration

def OrderConfigurationTest():
  config = ReadExcel.ReadConfigDataFromExcel("C:\\Users\\SA118193\\Desktop\\AccountSheet2.xlsx",2)
  Order_Configuration.Order_Configuration(config)
  