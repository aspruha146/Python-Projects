import qrcode
link = input("link:https://open.spotify.com/playlist/3o1eSfm9jb2kjLEs9Y0U5k")
qrcode= sengo.make_qr(link)
qrcode.save("qrcode.jpg",scale=5)