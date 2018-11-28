

Public Function WebGoogle()
  'Cria a instância que irá manipular o navegador Chrome
  Dim driver As New ChromeDriver
  'Declaração de variáveis, destaque para a variável table que recebe um WebElement
  Dim table As WebElement
  Dim Data As Variant
  Dim URL As String
  
  'Faz a chamada do navegador e acessa o primeiro website
  URL = "https://cidades.ibge.gov.br/brasil/ma/panorama"
  driver.Get URL
  
  'Localiza um elemento table na página pelo XPath
  table = driver.FindElementByXPath("//*[@id="dados"]/panorama-resumo/table")
  'Transforma os elementos da table em uma matriz de dados
  Data = table.AsTable.data
  
  'Percorre a tabela imprimindo os dados
  For i = 1 To UBound(Data):
    Debug.Print Data(i, 1)
    Debug.Print Data(i, 2)
  Next
  
  driver.Quit
End Function
