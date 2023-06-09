#!/bin/bash
while true
do
name=$(ls | grep \.zip | perl -pe 's/.zip//')
unzip -P hej $name.zip &>hej
pass=$(cat hej | grep skipping | perl -pe 's/.zip//' | perl -pe 's/skipping: //' | perl -pe 's/ incorrect password//')
echo $pass
if [[ $pass == "" ]]
then
echo done
exit 1
fi
unzip -P $pass $name.zip  && rm $name.zip
done
