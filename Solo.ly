\version "2.20.0"  % necessary for upgrading to future LilyPond versions.
\header
	{
	title = "Prueba Solo"
	subtitle = "La batalla comienza"
	

\score {
\layout{}
\midi{}
\new Staff {
\absolute
\clef C
\time 2/4
\cadenzaOn
{
r1.. cis,16 r2 ais'1. dis'64. cis,1 g'16.. fis'1 ais,1. gis,16.. f,32. gis,32.. dis1 dis8 d,16 \bar "" 
fis64. g,1 r16. dis,1.. dis'32. cis8. b'1. e,32. r4 b'4 a'16.. cis2.. r2 dis64 f,4.. \bar "" 
r32 b64.. b'4 c'64 cis'2. e,16. r8 gis'16.. r8.. r64. cis,1. a,32. dis'64.. r4. e1 \bar "" 
dis'4 f'64 e'32 r16. e64.. e,8 e4. r16. gis'64 cis'4. g'1.. r32.. cis,8. r16.. r1.. \bar "" 
r1. cis16 r4 c,32.. a64 r8. gis'16.. cis1. r1 c'8.. gis,4. r32 fis,4. r4. c1. \bar "" 
r4.. e,16 r1.. cis1. r16.. dis'64. gis'32.. f'16 r8.. b'1. r64 a16.. r32. b,4.. r16.. \bar "" 
e,16 fis'2. r2.. c,64 ais'2 e'16.. ais,4 cis64 a'4 fis1. 
}
}
}