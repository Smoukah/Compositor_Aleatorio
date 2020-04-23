\version "2.20.0"  % necessary for upgrading to future LilyPond versions.
\header
	{
	title = "Prueba Solo"
	subtitle = "La batalla comienza"
	
}
\score {
\layout{}
\midi{}
\new Staff {
\absolute
\clef C
\time 2/4 
\tempo 4 = 60
\cadenzaOn
{
ais8.. gis,16. r16 r64 e'16 r32 gis,4. f,4 d'4. fis,64. d,64. d'8.. f64. b,32. e,1. \bar "" 
r1. r32 cis1. a,64. e8 cis4.. f2 r64. f'1 r16. r32.. g,4 d'64 a1. r8 \bar "" 
r4.. c2. gis32.. gis'4.. b'32 e'64.. f'1.. ais2 f,1 fis'64. e'16. r8.. gis32.. d64.. b'1. \bar "" 
d1. gis'32. ais,16. r1 fis2 a,4.. gis'16.. a4 c,4.. gis'8.. c,8 b,2 c'64. dis64. f'1.. \bar "" 
r64.. r8. gis'32. f64 r1. 
}
}
}