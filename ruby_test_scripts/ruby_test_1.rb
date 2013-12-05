def comparesArray(xmlPath,arrExDB,arrRtXML,modName,msg,remarks)
  begin
    $write.log("Info","Inside comparesArray method from ********.rb")
    if arrExDB.sort == arrRtXML.sort
      qcode = ""
      arrRtXML.each{|x| qcode = qcode+x+","}
      qcode = qcode
      @objXLResult.writePassResults($rowCounter,$rowCounter-1,modName,msg,xmlPath,qcode.chomp(","),qcode.chomp(","),remarks)
    else
      arrRt =arrRtXML-arrExDB
      strRt =""
      arrRt.each{|x|     
        strRt = strRt+x+",\n"
      }
      arrEx =arrExDB-arrRtXML
      strEx =""
      arrEx.each{|x|      
        strEx = strEx+x+",\n"
      }
      @objXLResult.writeFailResults($rowCounter,$rowCounter-1,modName,msg,xmlPath,strEx.chomp(","),strRt.chomp(","),"Does not Match - #{remarks}")
    end
  rescue Exception => e1
    $write.log("Exception"," Problem from comparesArray method from ********.rb. System = #{e1.to_s}")
  end 
end