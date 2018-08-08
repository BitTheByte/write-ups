#-*- coding:utf-8 -*-
import os
import hashlib
import random
import re


#msg = open("flag.txt").read().strip()
#
#res = ""
#for i in xrange(0, len(msg), 2):
#    pair = msg[i:i+2]
#    a = random.randint(1, 16)
#    b = random.randint(1, 16)
#    res += os.urandom(random.randint(0, 31)).encode("hex")
#    res += hashlib.sha512(pair).hexdigest()[a:-b][::-1]
#    res += os.urandom(random.randint(0, 31)).encode("hex")
#print res

res = """a9693c8ab3579771199c6232692abf50938331b72fe84de8fcb07f989573f4bec9706dc1f86cdb20389de254c36f5843d6935def40ddab8db687e459bf9e38a73b0ccfa63696bfcd4c9b744f06240a7411628161cc9097a655725a5a6e53d23548811ed39ba05ee7e0ac27082159fc862914d315ab11a6fe6d7352b9c18d2b0dcd6048fe9651da0195bfba45a5c75a2fbdb0cc83ec7978cf08adf90bc54c19d6af22355809984db16283f4dabe2d628ccade965f0ee5f537031f12c510adfca7f39abcbecd1a02b15d27903a0bf58729e5936dd1a1b8108313c3f945ff7d68b5e8e90eea6c065a8496f770d74613522d3dbd2a38adc7f8b215a359409db31b9f3c37b1757ca0e4dbf0f23cc8d78733639e70ea37e97861b8ddfe2fee8a431c8f3b33c19670c4257600f69130ba2205e7f5ade42512762b9ab5024aabd68db49d9d9452811ddb39bede3bd60ddbabfe2fc9f12216e6f69c53daff21e6e154fa5f07b4c073d129c4f01a3a452bf786b21a468bf29c186c60697ed50e8ec28a773ea98f3201d4be81704737495aceea28ce017bc2b780d8b176e136028cf12154a9bc6970c8ee7face04ce12b6fcc8fd804196f35a917738213260f57044204e6e94438d8985b75e1d8507c1e66385a812ce09e4c8293ee1aba379911fb419622573f0aa617f44d6ffcb6ad4660bc192c22dbf0940af08195892a21dbfd586b79b44628ffff603d7c652d2ed50550ca2b2bc7c121bdf7d520d3330f58ecdffb21937450a01f87d62327f66871076690c270b5d849f15be850454efc5c90c7b62bf836a3b561d2fb2d4f73c8a2f9af5849f6d71f74b7b03aaedcbeb3ec7b4fcab73f2ba143914b4d0bdb7d4d73418018f0a5bcf206ff80d785128a0ed06b0c3e47c5aac88dcc721f8567248c395d2615f3feeaacbecc180adc918d08276ffebe8e61be98a5fa17888080a029a6f69b3737e8faf26b04dcd004044b6aa19de38805850b265e2ca04271ca2043b82cdd9513b9a12419ed76c43eae81ce77af8e352594ca82c4848c23614bad02cc7fd4f86004df077474c0256645caf755ca79baa4237146d6a68adae32aa8871b8a609849bf7c1036cf131f38ea40ccae5e3faa06e72c26d87f81f1994ea957a7ea231d93734f6c8aa65c9790d3faa456134024ca4dc874bfc77e9e2e0086db0692745574fe46fc88211cbd837121d82b5848d6ec6adb1b804cfd0d95a1019053a65cc9ce6059111cc576dd827bf81493e4c699d11462135cba1f2bbef5397a3a13fd20963bb648aee1583de387038d5f087efede43cbf37087fff2b4b3563ffc2be9e2ab11a9770eb743227503a689d855c749d3b86a0b104b31118dcfe0c0d809e1ccd52deca3457cee26c9170af2b3081d6ab86b4e4f600f093cc5481bac15be1b4151a62f09cf06e71f7cafba3ea6931adddd33b013cb8dcbbac179de42305996ba1246fac02b98f85c157ea1e1d30e00a3a9f259b7584ac408257054986c3159ff6c17264a39fe60f7346cc77b357272c2471f6e518180f96e212974632ff7cde88d24941c9d4f0adb6def526fe66ac9e48a2b914c101559c28b829db3b5f7243f7e683bd67622ba3bcdc99b81daa4206a973046ff4d8a668a075d5ee1ca28745d40357004d1e823c870117ecd4e9838ca5f56c1a57a9e09a0e356bb357bd62d8e7b1d0865c843f1a481ec67b1fa246a96da6a0e1da27b944a26d0281fb1fe70229370d6d3ce72b63481899c814436f585c524b4bd87ade059e5869c0bdb72b5e0ffe65c6f9ceb2e748393cb5f53307139065bc7477993bd16d9d35b20"""


def Find(m,res):
	X = hashlib.sha512(m).hexdigest()[::-1]
	Score = 0
	for x in xrange(-31,31,1):
		for y in xrange(-31,31,1):
			cut = X[x:-y]
			if cut in res and len(cut) > 20:
				Score += 1
	if Score > 50:
		return m
	else:
		return 0

for i in xrange(31,127,1):
	for i2 in xrange(31,127,1):
		pair = chr(i) + chr(i2)
		f = Find(pair,res)
		if  f != 0:
			print "Found {}".format(f)
#flag = FLAG{Find-hash-in-the-trash!!}
