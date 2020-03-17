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
c4 b1 e8 r1.. f16.. r2.. ais,1 ais,64. r64. }
}
}