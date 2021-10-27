# PubMedEmail
An attempt to get email addresses for authors of pubmed papers

This directory contains code that will attempt to extract email addresses from pdf versions of PubMed files (though it may work about as well for any pdf). This extraction happens in 2 stages. In the first stage we use the code pdf2txt.py from https://github.com/pdfminer/pdfminer.six to create a text version of the pdf file.  In the second stage we use python regular expression parsing to extract any email addresses from the txt. This happens in the getEmailsFromTxt.py script. Both stages are executed in the extractEmailsFromPDF.sh script. 

Here's an example usage:

for i in `ls -1 testData`; do echo $i; ./extractEmailsFromPDF.sh testData textData $i emails.out; done

Each invocation of extractEmailsFromPDF.sh processes a single pdf file. The arguments to the extractEmailsFromPDF.sh are positional and are 

1) the directory containing the pdf file from which to extract the email addresses
2) the directory in which to write the intermediate text file
3) the name of the pdf file from which to extract the email addresses
4) the name of a file to which the file name and the extracted addresses are appended

The bash for loop above processes each of the pdf files in the testData directory, deposits a text file derived from each pdf into the textData directory and extracts email addresses. The file name and email addresses are appended to the emails.out file
