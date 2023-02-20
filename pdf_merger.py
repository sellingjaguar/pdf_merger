import PyPDF2
import os
import argparse

def ParseArgs():
    parser = argparse.ArgumentParser()

    parser.add_argument('-t', help='target directory', type=str, default=os.getcwd())
    parser.add_argument('-o', help='output directory', type=str, default=os.getcwd())
    parser.add_argument('-n', help='output file name', type=str, default='merged')

    return parser.parse_args()

def OrderFiles(f_list ,ord_by, direction):

    #to-do (order by size and name ascending or descending)

    pass

def GetAllPdfs(folder, ord_by="name", desc=False):
    
    pdf_list = []
    for path, NotImplemented, files in os.walk(folder):
        for file in files:
            if file[-4:] == '.pdf':
                file_path = os.path.join(path, file)
                print(f'File found: {file}')
                pdf_list.append(file_path)
    
    #files = OrderFiles(parameter1, parameter2)

    return pdf_list

def merge_pdf(target, output, name):

    files = GetAllPdfs(target)

    print(f'Merging {len(files)} files...')
    merger = PyPDF2.PdfMerger()
    for file in files:
        merger.append(file)
    
    #print(output)
    merger.write(f'{output}/{name}.pdf')


if __name__ == '__main__':

    args = ParseArgs()

    merge_pdf(args.t, args.o, args.n)
