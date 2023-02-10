import speedtest

test= speedtest.Speedtest()
download = test.download()
upload = test.upload()

print(f"Vitesse de téléchargement : {download} ")
print(f"Vitesse d'envoi : {upload} ")
