{\rtf1\ansi\ansicpg1252\cocoartf2639
\cocoatextscaling0\cocoaplatform0{\fonttbl\f0\froman\fcharset0 Times-Bold;\f1\froman\fcharset0 Times-Roman;\f2\fmodern\fcharset0 Courier;
}
{\colortbl;\red255\green255\blue255;\red0\green0\blue0;}
{\*\expandedcolortbl;;\cssrgb\c0\c0\c0;}
{\*\listtable{\list\listtemplateid1\listhybrid{\listlevel\levelnfc23\levelnfcn23\leveljc0\leveljcn0\levelfollow0\levelstartat1\levelspace360\levelindent0{\*\levelmarker \{disc\}}{\leveltext\leveltemplateid1\'01\uc0\u8226 ;}{\levelnumbers;}\fi-360\li720\lin720 }{\listname ;}\listid1}
{\list\listtemplateid2\listhybrid{\listlevel\levelnfc23\levelnfcn23\leveljc0\leveljcn0\levelfollow0\levelstartat1\levelspace360\levelindent0{\*\levelmarker \{disc\}}{\leveltext\leveltemplateid101\'01\uc0\u8226 ;}{\levelnumbers;}\fi-360\li720\lin720 }{\listname ;}\listid2}}
{\*\listoverridetable{\listoverride\listid1\listoverridecount0\ls1}{\listoverride\listid2\listoverridecount0\ls2}}
\margl1440\margr1440\vieww28600\viewh15360\viewkind0
\deftab720
\pard\pardeftab720\sa321\partightenfactor0

\f0\b\fs48 \cf0 \expnd0\expndtw0\kerning0
\outl0\strokewidth0 \strokec2 PDF Converter\
\pard\pardeftab720\sa240\partightenfactor0

\f1\b0\fs24 \cf0 This Python script converts PDF files into plain text (
\f2\fs26 .txt
\f1\fs24 ) and Word documents (
\f2\fs26 .docx
\f1\fs24 ).\
\pard\pardeftab720\sa298\partightenfactor0

\f0\b\fs36 \cf0 Requirements\
\pard\tx220\tx720\pardeftab720\li720\fi-720\sa240\partightenfactor0
\ls1\ilvl0
\f1\b0\fs24 \cf0 \kerning1\expnd0\expndtw0 \outl0\strokewidth0 {\listtext	\uc0\u8226 	}\expnd0\expndtw0\kerning0
\outl0\strokewidth0 \strokec2 Python 3.x\
\ls1\ilvl0\kerning1\expnd0\expndtw0 \outl0\strokewidth0 {\listtext	\uc0\u8226 	}\expnd0\expndtw0\kerning0
\outl0\strokewidth0 \strokec2 Libraries: 
\f2\fs26 pdfplumber
\f1\fs24 , 
\f2\fs26 python-docx
\f1\fs24 \
\pard\pardeftab720\sa240\partightenfactor0
\cf0 Install the libraries using:\
\pard\pardeftab720\partightenfactor0

\f2\fs26 \cf0 \
pip3 install pdfplumber python-docx\
\
\pard\pardeftab720\sa298\partightenfactor0

\f0\b\fs36 \cf0 Usage\
\pard\pardeftab720\sa240\partightenfactor0

\f1\b0\fs24 \cf0 Run the script from the command line with the following format:\
\pard\pardeftab720\partightenfactor0

\f2\fs26 \cf0 \
python3 pdf_converter.py <input_pdf> <output_txt> <output_docx>\
\
\pard\pardeftab720\sa240\partightenfactor0

\f0\b\fs28 \cf0 Example:
\f2\b0\fs26 \
\pard\pardeftab720\partightenfactor0
\cf0 python3 pdf_converter.py example.pdf output.txt output.docx\
\pard\tx220\tx720\pardeftab720\li720\fi-720\sa240\partightenfactor0
\ls2\ilvl0\cf0 \kerning1\expnd0\expndtw0 \outl0\strokewidth0 {\listtext	\uc0\u8226 	}\expnd0\expndtw0\kerning0
\outl0\strokewidth0 \strokec2 <input_pdf>
\f1\fs24 : Path to the PDF you want to convert.\
\ls2\ilvl0
\f2\fs26 \kerning1\expnd0\expndtw0 \outl0\strokewidth0 {\listtext	\uc0\u8226 	}\expnd0\expndtw0\kerning0
\outl0\strokewidth0 \strokec2 <output_txt>
\f1\fs24 : Path where the plain text file will be saved.\
\ls2\ilvl0
\f2\fs26 \kerning1\expnd0\expndtw0 \outl0\strokewidth0 {\listtext	\uc0\u8226 	}\expnd0\expndtw0\kerning0
\outl0\strokewidth0 \strokec2 <output_docx>
\f1\fs24 : Path where the Word document will be saved.\
\pard\pardeftab720\sa240\partightenfactor0
\cf0 After running, you will have both a 
\f2\fs26 .txt
\f1\fs24  and 
\f2\fs26 .docx
\f1\fs24  version of your PDF content.\
}