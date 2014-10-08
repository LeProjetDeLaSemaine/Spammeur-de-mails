#!/usr/bin/env python
# -*- coding: utf-8 -*-
#En utf-8, car les mauvais logiciels de chez Microsoft ne sont pas capables
#de décoder leur propre encodage. GG Bill !

from smtplib import SMTP
import sys

#meilleurInput reprend input() mais supporte les caractères spéciaux sur Python 2.x
#sur Python 3.x, utilisez la fonction input() normale.
def meilleurInput(unMessage):
	print unMessage,
	chaine = sys.stdin.readline().strip()
	return chaine


malheureuxDestinataire = meilleurInput(" Entrez le mail du malheureux destinataire : ")
username = meilleurInput("Entrez votre nom d'utilisateur GMail : ")
passwd = meilleurInput("Entrez votre mot de passe : ")
message = meilleurInput("Entrez le corps du message : ")

session = SMTP('smtp.gmail.com', 587)
session.ehlo()
session.starttls()

session.login(username, passwd)

msg = "\n" + message
#\n sépare le corps du message des headers qui le précèdent

n = int(meilleurInput("Entrez le nombre de répétitions : "))
print "Veuillez patienter"

for i in range(0, n):
	session.sendmail(username + "@gmail.com", malheureuxDestinataire, msg)