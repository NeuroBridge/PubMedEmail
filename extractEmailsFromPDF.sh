#!/bin/bash
# This script processes a single pdf file and extracts email addresses This extraction 
# happens in 2 stages. In the first stage we use the code pdf2txt.py from 
# https://github.com/pdfminer/pdfminer.six to create a text version of the pdf file.  
# In the second stage we use python regular expression parsing to extract any email addresses from the txt
# The first stage happens in the pdf2txt.py call, which is installed with pip install pdfminer.six
# The second stage happens in the getEmailsFromTxt.py code, which is included in this directory

# Positional arguments to this script are:
# 1) the directory containing the pdf file from which to extract the email addresses
# 2) the directory in which to write the intermediate text file
# 3) the name of the pdf file from which to extract the email addresses
# 4) the name of a file to which the file name and the extracted addresses are appended
set -e

# Process the arguments included creating the full paths for the input and output files
indir=$1
outdir=$2
inFile=${1}/${3}
outFilename=`basename $3 ".pdf" `
outFile=${2}/${outFilename}.txt
resultFile=$4

# create the output file only if it is not there
if [[ ! -e $outdir ]]; then
    mkdir $outdir
elif [[ ! -d $outdir ]]; then
    echo "$outdir already exists but is not a directory" 1>&2
fi

# write the file name to the output file
echo $3 >> $resultFile

# don't bother with zero length input files
if [[ -s $infile ]]; then
   echo "input file ${infile} is zero length" >> $resultFile
   exit 1
fi

# don't recreate the text file if it is already there
if [[ ! -e $outFile ]]; then
   pdf2txt.py $inFile > $outFile
fi

# extract the list of emails and write it to the output file
getEmailsFromTxt.py --inputFile $outFile >> $resultFile
