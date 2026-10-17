---
id: study_0263
title: "Equal Earth projection"
rank: 272
views: 459726
url: "https://en.wikipedia.org/wiki/Equal_Earth_projection"
pageid: 58246920
description: "Equal-area pseudocylindrical global map projection"
summary: "The Equal Earth map projection is an equal-area pseudocylindrical global map projection invented by Bojan Šavrič, Bernhard Jenny, and Tom Patterson in 2018. It is inspired by the widely used Robinson projection, but unlike the Robinson projection, it retains the relative size of areas, and the projection equations are designed to be simple to implement and fast to evaluate. The creators of the Equal Earth projection intended it to be used only when an equal-area projection was strictly mandated. When publishing its specifications, they warned that equal-area projections are not the panacea tha..."
source: Wikipedia
license: "CC BY-SA 4.0"
month: "2026-09"
retrieved: 2026-10-16
---

# Equal Earth projection

The **Equal Earth map projection** is an [equal-area](https://en.wikipedia.org/wiki/Equal-area_projection "Equal-area projection") [pseudocylindrical](https://en.wikipedia.org/wiki/Pseudocylindrical "Pseudocylindrical") global [map projection](https://en.wikipedia.org/wiki/Map_projection "Map projection") invented by Bojan Šavrič, Bernhard Jenny, and Tom Patterson in 2018. It is inspired by the widely used [Robinson projection](https://en.wikipedia.org/wiki/Robinson_projection "Robinson projection"), but unlike the Robinson projection, it retains the relative size of areas, and the projection equations are designed to be simple to implement and fast to evaluate.

The creators of the Equal Earth projection intended it to be used only when an equal-area projection was strictly mandated. When publishing its specifications, they warned that equal-area projections are not the panacea that many organizations might think. For example, continental shapes suffer.

Following a public campaign called "Correct the Map" to promote the Equal Earth projection, and a resolution by the [African Union](https://en.wikipedia.org/wiki/African_Union "African Union") to officially adopt the projection, the [United Nations General Assembly](https://en.wikipedia.org/wiki/United_Nations_General_Assembly "United Nations General Assembly") approved a [resolution](https://en.wikipedia.org/wiki/United_Nations_General_Assembly_resolution "United Nations General Assembly resolution") addressing the projection in September 2026. The resolution discouraged use of the [Mercator projection](https://en.wikipedia.org/wiki/Mercator_projection "Mercator projection") for most uses other than navigation, while encouraging the use of equal-area projections instead, and favorably mentioning Equal Earth as an option.

## Design motivation

Some map projections distort the relative size of different regions on the map, with non-equatorial regions depicted larger than equatorial regions of the same area. For example, on the [Mercator projection](https://en.wikipedia.org/wiki/Mercator_projection "Mercator projection"), [Greenland](https://en.wikipedia.org/wiki/Greenland "Greenland") appears to be larger than the whole of Africa, when in reality it is only 7% as big. An [equal-area projection](https://en.wikipedia.org/wiki/Equal-area_projection "Equal-area projection") solves this problem by depicting regions in proportion to their original area, at the expense of shape distortion.

In March 2017, [Boston Public Schools](https://en.wikipedia.org/wiki/Boston_Public_Schools "Boston Public Schools") adopted the equal-area [Gall–Peters projection](https://en.wikipedia.org/wiki/Gall%E2%80%93Peters_projection "Gall–Peters projection") for world maps, to accurately show the relative sizes of equatorial and non-equatorial regions. The decision generated controversy in the world of cartography due to that projection's extreme shape distortion in the polar regions. Šavrič, Jenny, and Patterson examined alternative equal-area projections of the world, but could not find any that met their aesthetic criteria, so decided to create a new projection which they considered more visually appealing.

According to Šavrič, Jenny, and Patterson, equal-area projections are not an ideal solution to every mapping problem, as continental shapes are distorted. Equal Earth is only intended for situations calling for an equal-area map.

## Formulation

As with the earlier [Natural Earth projection](https://en.wikipedia.org/wiki/Natural_Earth_projection "Natural Earth projection") (2012) introduced by Patterson, a visual method was used to choose the parameters of the projection. A combination of Putniņš P4ʹ and [Eckert IV projections](https://en.wikipedia.org/wiki/Eckert_IV_projection "Eckert IV projection") was used as the basis. Mathematical formulas for the projection were derived from a polynomial used to define the spacing of parallels. The projection is formulated as the equations:

x

=

2

3
3
λ
⋅

cos
⁡

θ

9

A

4

θ

8
+
7

A

3

θ

6
+
3

A

2

θ

2
+

A

1
,

y

=

A

4

θ

9
+

A

3

θ

7
+

A

2

θ

3
+

A

1
θ
,
{\displaystyle {\begin{aligned}x&={\frac {2{\sqrt {3}}}{3}}\lambda \cdot {\frac {\cos {\theta }}{9A\_{4}\theta ^{8}+7A\_{3}\theta ^{6}+3A\_{2}\theta ^{2}+A\_{1}}},\\[3pt]y&=A\_{4}\theta ^{9}+A\_{3}\theta ^{7}+A\_{2}\theta ^{3}+A\_{1}\theta ,\end{aligned}}}
where

φ
{\displaystyle \varphi }
 is the latitude and

λ
{\displaystyle \lambda }
 is the longitude, ⁠

θ
{\displaystyle \theta }
⁠ is a function of latitude defined by

sin
⁡
θ
=

3
2
sin
⁡

φ
,
{\displaystyle \sin \theta ={\tfrac {\sqrt {3}}{2}}\sin {\varphi },}
and the polynomial coefficients are

A

1

=
1.340264
,

A

2
=
−
0.081106
,

A

3

=
0.000893
,

A

4
=

−
0.003796
,
{\displaystyle {\begin{aligned}A\_{1}&=1.340264,\quad A\_{2}=-0.081106,\\A\_{3}&=0.000893,\quad A\_{4}={\phantom {-}}0.003796,\end{aligned}}}
with all angles expressed in [radians](https://en.wikipedia.org/wiki/Radian "Radian").

The resulting map has an [aspect ratio](https://en.wikipedia.org/wiki/Aspect_ratio "Aspect ratio") of 2.05458:1, a value chosen for aesthetic reasons and very close to the "natural ratio" of a sphere (180°/90°).

### Distortion

Since the surface of a sphere cannot be mapped onto a plane without distortion, all (planar) maps distort shapes in one way or another. The distortion can be visualized using an index called "[Tissot's Indicatrix](https://en.wikipedia.org/wiki/Tissot%27s_Indicatrix "Tissot's Indicatrix")", which shows how the size and shape of an infinitesimal circular area is projected onto the map.

In the Equal Earth projection, a small area on the surface of the Earth shows its accurate shape on the central meridian (0°) at a latitude of 40.4° North or South. At locations closer to the equator than this, shapes are elongated in the north-south direction and compressed in the east-west direction, reaching a maximum shape distortion of 1.35. At locations poleward of 40.4°, shapes are elongated E-W and compressed N-S, with an elongation ratio approaching infinity at the pole (mapping the pole itself to a horizontal line rather than a point.) East and west of the central meridian of 0°, at locations away from the equator the ellipses become tilted, with the north-south axis of the ellipse pointed toward the central meridian.

## Use

An *Equal Earth Political Wall Map* by Tom Patterson, designed for schools and organisations, is labelled using United States [Central Intelligence Agency](https://en.wikipedia.org/wiki/Central_Intelligence_Agency "Central Intelligence Agency") map data. Countries are mostly the same as US government maps; however, Patterson made changes in the depiction of [Myanmar](https://en.wikipedia.org/wiki/Myanmar "Myanmar") (and [Naypyidaw](https://en.wikipedia.org/wiki/Naypyidaw "Naypyidaw")), [Taiwan](https://en.wikipedia.org/wiki/Taiwan "Taiwan") (and [Taipei](https://en.wikipedia.org/wiki/Taipei "Taipei")), [Western Sahara](https://en.wikipedia.org/wiki/Western_Sahara "Western Sahara") ([Western Sahara conflict](https://en.wikipedia.org/wiki/Western_Sahara_conflict "Western Sahara conflict")), depiction of [Crimea](https://en.wikipedia.org/wiki/Crimea "Crimea"), a border between [Kenya](https://en.wikipedia.org/wiki/Kenya "Kenya") and [South Sudan](https://en.wikipedia.org/wiki/South_Sudan "South Sudan"), and boundaries between [China](https://en.wikipedia.org/wiki/China "China"), [India](https://en.wikipedia.org/wiki/India "India"), and [Pakistan](https://en.wikipedia.org/wiki/Pakistan "Pakistan").

One of the first known thematic maps published using the Equal Earth projection is a map of the global mean [temperature anomaly](https://en.wikipedia.org/wiki/Temperature_anomaly "Temperature anomaly") for July 2018, produced by NASA's [Goddard Institute for Space Studies](https://en.wikipedia.org/wiki/Goddard_Institute_for_Space_Studies "Goddard Institute for Space Studies").

### Software support

[OpenStreetMap](https://en.wikipedia.org/wiki/OpenStreetMap "OpenStreetMap")-based maps can be created using Equal Earth projections. [Mapbox](https://en.wikipedia.org/wiki/Mapbox "Mapbox") supports the `equalearth` projection. [Esri](https://en.wikipedia.org/wiki/Esri "Esri") tools support Equal Earth projection. The open-source [PROJ](https://en.wikipedia.org/wiki/PROJ "PROJ") library has included the projection since version 5.2.0, released in September 2018, which makes it available in software built on top of PROJ, such as [QGIS](https://en.wikipedia.org/wiki/QGIS "QGIS"). The website equal.bbox.earth provides software for producing Equal Earth vector tiles which are compatible with map display tools designed for the [Web Mercator projection](https://en.wikipedia.org/wiki/Web_Mercator_projection "Web Mercator projection").

By default, the Equal Earth projection is centered on the [prime meridian](https://en.wikipedia.org/wiki/Prime_meridian "Prime meridian") passing through London, but various software tools support creation of Equal Earth maps centered elsewhere. [Esri](https://en.wikipedia.org/wiki/Esri "Esri") [ArcGIS](https://en.wikipedia.org/wiki/ArcGIS "ArcGIS") Pro 3.7 has *False Easting*, *False Northing* and *Central Meridian* as available parameters. [PROJ](https://en.wikipedia.org/wiki/PROJ "PROJ") based software such as [QGIS](https://en.wikipedia.org/wiki/QGIS "QGIS") can use any central meridian through the `lon_0` parameter, and the [EPSG](https://en.wikipedia.org/wiki/EPSG_Geodetic_Parameter_Dataset "EPSG Geodetic Parameter Dataset") registry defines three variants, centred on Greenwich (EPSG:8857), 90°W (EPSG:8858) and 150°E (EPSG:8859). However, as of September 2026, [Mapbox](https://en.wikipedia.org/wiki/Mapbox "Mapbox") only supports Equal Earth maps centered on the prime meridian.

### Correct The Map campaign

The Correct the Map campaign calls for adopting the Equal Earth projection for world maps, instead of the widely used [Mercator projection](https://en.wikipedia.org/wiki/Mercator_projection "Mercator projection"). The campaign was started by [Africa No Filter](https://en.wikipedia.org/wiki/Africa_No_Filter "Africa No Filter") and [Speak Up Africa](https://en.wikipedia.org/w/index.php?title=Speak_Up_Africa&action=edit&redlink=1 "Speak Up Africa (page does not exist)"), and gained the support of the [African Union](https://en.wikipedia.org/wiki/African_Union "African Union") and the [Caribbean Community](https://en.wikipedia.org/wiki/Caribbean_Community "Caribbean Community"). For the African Union, a change in map projection was a change to influence how people "view, talk about and value Africa". The campaign calls on the [United Nations](https://en.wikipedia.org/wiki/United_Nations "United Nations"), [World Bank](https://en.wikipedia.org/wiki/World_Bank "World Bank"), and [BBC](https://en.wikipedia.org/wiki/BBC "BBC") to "adopt the Equal Earth projection in their data, reports, and materials that include world maps".

### United Nations resolution

On September 4, 2026, the *Correct the Map* resolution, put forward by African Union member states and [The Bahamas](https://en.wikipedia.org/wiki/The_Bahamas "The Bahamas"), was adopted at the [80th session](https://en.wikipedia.org/wiki/80th_session_of_the_United_Nations_General_Assembly "80th session of the United Nations General Assembly") of the [United Nations General Assembly](https://en.wikipedia.org/wiki/United_Nations_General_Assembly "United Nations General Assembly"). The resolution encourages the world to phase out the [Mercator projection](https://en.wikipedia.org/wiki/Mercator_projection "Mercator projection") in favour of the [Equal Earth](https://en.wikipedia.org/wiki/Equal_Earth "Equal Earth") projection and other equal-area projections, which depict equatorial regions larger, and polar regions smaller, compared to the Mercator projection. The resolution links more accurate maps to "[cognitive justice](https://en.wikipedia.org/wiki/Cognitive_justice "Cognitive justice"), historical recognition and equitable representation". UN resolutions are non-enforceable and use of the projection is not mandated, and other projections are not banned.

*The Guardian* wrote the outcome was expected to result in the update of education curriculums and general technology. [Agence France-Presse](https://en.wikipedia.org/wiki/Agence_France-Presse "Agence France-Presse") published a handout map. Šavrič, Jenny, and Patterson were surprised by the projection's near-universal acceptance by the United Nations.

#### Positions of member states

Of the [193 member states of the United Nations](https://en.wikipedia.org/wiki/Member_states_of_the_United_Nations "Member states of the United Nations"), 164 voted in favour of the resolution, six abstained ([Estonia](https://en.wikipedia.org/wiki/Estonia "Estonia"), [Georgia](https://en.wikipedia.org/wiki/Georgia_(country) "Georgia (country)"), [Lithuania](https://en.wikipedia.org/wiki/Lithuania "Lithuania"), [Moldova](https://en.wikipedia.org/wiki/Moldova "Moldova"), [Serbia](https://en.wikipedia.org/wiki/Serbia "Serbia"), and [Ukraine](https://en.wikipedia.org/wiki/Ukraine "Ukraine")), and one voted against (United States).

The [United States](https://en.wikipedia.org/wiki/United_States "United States") opposed the resolution on the grounds that it did not address "genuine problems", saying that it "mocks the work and purpose" of the United Nations, and calling it part of a "larger and more radical ideological project".
[Ukraine](https://en.wikipedia.org/wiki/Ukraine "Ukraine") abstained from the vote, taking issue with the fact that maps published by Tom Patterson on equal-earth.com depicted [Crimea](https://en.wikipedia.org/wiki/Crimea "Crimea") in a different color from Ukraine, which the Ukrainian representative called "wholly unacceptable". Similarly, after the vote, Japanese diplomats contacted Patterson asking for a change to the [Kuril Islands](https://en.wikipedia.org/wiki/Kuril_Islands "Kuril Islands"), which were depicted in the same color as Russia.

France's [foreign minister](https://en.wikipedia.org/wiki/Ministry_for_Europe_and_Foreign_Affairs_(France) "Ministry for Europe and Foreign Affairs (France)") [Jean-Noël Barrot](https://en.wikipedia.org/wiki/Jean-No%C3%ABl_Barrot "Jean-Noël Barrot") announced that France will discontinue teaching the Mercator projection in schools in response to the resolution.

## Alternatives

The [Winkel tripel projection](https://en.wikipedia.org/wiki/Winkel_tripel_projection "Winkel tripel projection") has more accurate shapes than Equal Earth with less accurate sizes, and is regarded as one of the least distorted compromise projections. The [National Geographic Society](https://en.wikipedia.org/wiki/National_Geographic_Society "National Geographic Society") and many educational institutions use Winkel tripel projection for global mapping.

The Equal Earth projection is one of many equal-area [pseudocylindrical](https://en.wikipedia.org/wiki/Pseudocylindrical "Pseudocylindrical") map projections.

The [Natural Earth projection](https://en.wikipedia.org/wiki/Natural_Earth_projection "Natural Earth projection") looks much like Equal Earth, while better preserving the shapes of the continents, but is not equal-area. The [Robinson projection](https://en.wikipedia.org/wiki/Robinson_projection "Robinson projection") is another alternative of this type.

Earlier attempts to give "a truer sense of area while retaining a visually intuitive layout" and replace the [Mercator projection](https://en.wikipedia.org/wiki/Mercator_projection "Mercator projection") include the [Goode homolosine](https://en.wikipedia.org/wiki/Goode_homolosine "Goode homolosine") and [Gall–Peters projection](https://en.wikipedia.org/wiki/Gall%E2%80%93Peters_projection "Gall–Peters projection").

---

*Source: [Wikipedia — Equal Earth projection](https://en.wikipedia.org/wiki/Equal_Earth_projection). Text licensed under [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/).*
