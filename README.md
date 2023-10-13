To run this files hit run but that is just possible because there is a file "launch.json" with some script on it.

Otherwise VSCODE is not reading the python3 version, it's is considering only the python version

Another way to run is to run direct on the terminal by: python3 -u file path

To credit card invoices:

1 - Download the invoice from C6 in a csv format and send it to e-mail
2 - From gmail, Download it
3 - On Linux, extract the file
4 - On Linux, rename extracted file to invoice.csv
5 - On terminal run: mv /home/ricardo/Downloads/invoice.csv /home/ricardo/codes/devops_python
6 - On VS Code run: python3 csv_converter.py
7 - On Terminal run: mv saida.json 2023-07.json (according to the month)
