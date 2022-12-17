# Ravachol bot
## Contribuer
il y'a dans commands.json deux blocs:
- single
  Valide si uniquement ce mot (ou cette phrase) est dans ce que la personne dit, par exemple pour "darmanin" : "darmanin", mais pas "abject darmanin"
- match
  Valide si le mot (ou la phrase) est contenue dans ce que la personne dit. Par exemple, pour "darmanin" : "abject darmanin" ou "darmanin est abject"


Dans chaque commande, il est possible d'ajouter un "random". Par exemple, si vous écrivez "random": 3, la réponse ne se fera qu'une fois sur trois. Si vous ne mettez pas de "random" ou que "random" est 1, la réponse se fera à chaque fois.

Finalement, un bloc "responses", qui est un tableau. si plusieurs réponses sont présentes, elles seront choisies au hasard.



