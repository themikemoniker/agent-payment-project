import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from nwc_client_super import processNWCstring, tryToPayInvoice, didPaymentSucceed

nwc_uri = "nostr+walletconnect://ba80990666ef0b6f4ba5059347beb13242921e54669e680064ca755256a1e3a6?relay=wss%3A%2F%2Frelay.coinos.io&secret=7f337004805d07888b929591980fec8bf1f62c057dfae5a5c9eae2fa84041f5e&lud16=themikemoniker@coinos.io"
invoice = "lnbc1u1p5pup28sp50mh9k0puvwnrx09xdvkrlc486qs3a70ld0h8vegytg2sdyj6fpcspp5435dwzq0cf8qhh4xd9jewfqq23mturjwp5fesh0g9keaung0g3zshp5uwcvgs5clswpfxhm7nyfjmaeysn6us0yvjdexn9yjkv3k7zjhp2sxq9z0rgqcqpnrzjqwuyhm4rwjccnjvkpw5g3jtxhjdwmux6p0qvqk9upadaalt03qg4vrt7puqqjesqqyqqqqlgqqqqztqq2q9qxpqysgqjf6ywqfqq7llrxyql45xnunm86rdva0swg2d0w4ejclw398s5fakm5yl2us7fuhxtgpskfm8vdxc5k837vqanuqzes6elthrq7g96mcqkpe94y"

nwc = processNWCstring(nwc_uri)
tryToPayInvoice(nwc, invoice)

if didPaymentSucceed(nwc, invoice):
    print("✅ Payment succeeded!")
else:
    print("❌ Payment failed or pending.")