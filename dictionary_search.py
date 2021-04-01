import requests
import json
class Solution:
	def fn(self):
		URL="https://api.dictionaryapi.dev/api/v2/entries/en_US/"
		word=input()
		URL+=word;
		r=requests.get(url=URL)
		ans=r.json()
		print(ans[0]['word'],".",ans[0]['meanings'][0]['partOfSpeech'],".",ans[0]['meanings'][0]['definitions'][0]['definition'])


Solution().fn()