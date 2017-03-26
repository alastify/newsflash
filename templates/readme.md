# Šablony
V tomto adresáři lze přetěžovat šablony z dílčích aplikací.

## Postup
Jednoduše zkopírujte obsah adresáře ``templates`` z dané aplikace sem.

Např. app ``newsflash`` obsahuje podadresář ``templates``, ve kterém se nachází další podadresář ``newsflash``

    newsflash
        | - templates
        |    |- newsflash
        |    |      index.html
        |    |      ...
    templates


Zkopírujte tedy tento vnořený ``newsflash`` tak, aby se nacházel v tomto adresáři. Výsledek tedy bude:

    newsflash
        | - templates
        |    |- newsflash
        |    |      index.html
        |    |      ...
    templates
        |- newsflash
        |      index.html
        |      ...
