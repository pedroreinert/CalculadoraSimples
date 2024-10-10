Processo para transformar a calculadora em um arquivo .exe

Após aberto o arquivo no VS Code, abra o terminal e insira o seguinte código: pyinstaller --onefile --windowed --icon=icon.ico calculadora2.py 

Importante lembrar que no codigo acima tem um icone de calculador que coloquei para trazer mais profissionalismo ao .exe, 
Se optar por fazer desta mesma forma o link do icone que usei é https://icon-icons.com/pt/icone/calculadora/34473  
Caso não queira é só remover a parte --icon=icon.ico do codigo
