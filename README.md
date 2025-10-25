#turtle_eight

##Uruchomienie noda spowoduje że żółw zacznie wykonywać ósemki

##Jak uruchomić
1. Uruchom turtlesim:
   ```
	ros2 run turtlesim turtlesim_node
3. W nowym terminalu uruchom node:
    ```
	cd ros2_ws/src/turtle_eight/turtle_eight
	source install/setup.bash
	ros2 run turtle_eight turtle_eight_node
##Działanie	
	
	Żółw na przemian będzie wykonywać obroty w lewo i w prawo, zmieniając kierunek po wykonaniu obrotu o pełne 360 stopni.

##Sprawozdanie

	Wybrałem zadanie nr. 1, ponieważ wydawało mi się najbardziej podobne do rzeczy które miałem już okazje robić.
		Na samym początku znaczną ilość czasu zajeło mi ogarnięcie wszystkich narzędzi (wsl,ros2,gedit) bo nie miałem wcześniej
	okazji, żeby z nimi pracować. Na początku wszystko szło mi dosyć opornie, ale na szczęście dosyć szybko udało mi się złapać jakiś 
	rytm porusznia się w nowym środowisku.
		Sam program wydawał mi się na początku dosyć prosty, ale finalnie nie wysłałem idealnego rozwiązania i poszedłem na kompromis 
	wybierając rozwiązanie proste, ale z lekką wadą.
		Żółw rysuje "ósemke" poruszając się po okręgu, a gdy skończy obrót o 360 stopni zmienia kierunek i dorysowuje lustrzane odbicie.
	Wada tego rozwiązania pojawia się po jakimś czasie, bo możemy wtedy zauważyć że "ósemki" nie pokrywają się 1:1 i z każdą iteracją
		łapią lekki offset.
		
<img width="504" height="528" alt="image" src="https://github.com/user-attachments/assets/6da867ab-1f1f-416e-9a0f-65a8b62c3915" />
