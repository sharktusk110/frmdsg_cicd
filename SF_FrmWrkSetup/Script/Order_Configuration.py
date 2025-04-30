def Order_Configuration(config=[]):
  
    configpg=Aliases.browser.page00300505XmlECon
    nav=Aliases.browser.pageAllSalesOrdersFinanceAndOper
    #Clicks the 'buttonSalestable22SalesorderButt' button.
    nav.buttonSalestable22SalesorderButt.ClickButton()
    #Clicks the 'buttonSalestable22Econconfigure' button.
    nav.formSalesOrder.buttonSalestable22Econconfigure.ClickButton()
    #Clicks the 'buttonConfigureinnewwindowbutton' button.
    nav.buttonConfigureinnewwindowbutton.ClickButton()
    #putting wait inorder to handle application slowness
    Delay(30000);
    #Clicks the 'textnodeConfiguration1' control.
    configpg.textnodeOrderConfigurator.textnodeOrderConfigurator2.linkConfiguration1.textnodeConfiguration1.Click()
    #putting wait inorder to handle application slowness
    Delay(5000);
    #entering type details
    configpg.textboxType.SetText(config[0])
    configpg.textboxType.Keys("[Enter]")
    #putting wait inorder to handle application slowness
    Delay(5000);
    #entering game classification details
    configpg.textboxGamingClassification.SetText(config[1])
    configpg.textboxGamingClassification.Keys("[Enter]")
    #putting wait inorder to handle application slowness
    Delay(5000);
    #entering platform specific details
    configpg.textboxPlatformPfm.SetText(config[2])
    #putting wait inorder to handle application slowness
    Delay(2000);
    configpg.textboxPlatformPfm.Keys("[Enter]")
    #putting wait inorder to handle application slowness
    Delay(5000);
    #entering setchip related details
    configpg.textboxSetChipEpg.SetText(config[3])
    #putting wait inorder to handle application slowness
    Delay(2000);
    configpg.textboxSetChipEpg.Keys("[Enter]")
    #putting wait inorder to handle application slowness
    Delay(5000);
    #entering os related details
    configpg.textboxOsLnx.SetText(config[4])
    Delay(2000);
    configpg.textboxOsLnx.Keys("[Enter]")
    #putting wait inorder to handle application slowness
    Delay(5000);
    #entering bootloader related details
    configpg.textboxBootloaderBtl.SetText(config[5])
    Delay(2000);
    configpg.textboxBootloaderBtl.Keys("[Enter]")
    #Clicks the 'textnodeOrderConfigurator3' control.
    configpg.textnodeOrderConfigurator.textnodeOrderConfigurator2.linkOrderConfigurator.textnodeOrderConfigurator3.Click()
    Delay(2000);
    #Clicks the 'buttonProcessExit' button.
    configpg.textnodeComplianceCheck.textnode6.buttonProcessExit.ClickButton()
    Delay(2000);
    #Clicks the 'buttonYes' button.
    configpg.buttonYes.ClickButton()
