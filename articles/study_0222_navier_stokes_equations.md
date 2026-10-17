---
id: study_0222
title: "Navier–Stokes equations"
rank: 231
views: 517824
url: "https://en.wikipedia.org/wiki/Navier%E2%80%93Stokes_equations"
pageid: 48395
description: "Equations of motion for viscous fluids"
summary: ""
source: Wikipedia
license: "CC BY-SA 4.0"
month: "2026-09"
retrieved: 2026-10-16
---

# Navier–Stokes equations

The **Navier–Stokes equations** ([/nævˈjeɪ ˈstoʊks/](https://en.wikipedia.org/wiki/Help:IPA/English "Help:IPA/English") [*nav-YAY STOHKS*](https://en.wikipedia.org/wiki/Help:Pronunciation_respelling_key "Help:Pronunciation respelling key")) describe the motion of [viscous](https://en.wikipedia.org/wiki/Viscosity "Viscosity") fluids. This system of [partial differential equations](https://en.wikipedia.org/wiki/Partial_differential_equation "Partial differential equation") was named after [Claude-Louis Navier](https://en.wikipedia.org/wiki/Claude-Louis_Navier "Claude-Louis Navier") and [George Gabriel Stokes](https://en.wikipedia.org/wiki/Sir_George_Stokes,_1st_Baronet "Sir George Stokes, 1st Baronet"), who developed them over a few decades of progressive work, from 1822 (Navier) to 1842–1850 (Stokes). [Siméon Denis Poisson](https://en.wikipedia.org/wiki/Sim%C3%A9on_Denis_Poisson "Siméon Denis Poisson") independently achieved the same results.

The Navier–Stokes equations mathematically express [momentum](https://en.wikipedia.org/wiki/Momentum "Momentum") balance for [Newtonian fluids](https://en.wikipedia.org/wiki/Newtonian_fluid "Newtonian fluid") and make use of the [conservation of mass](https://en.wikipedia.org/wiki/Conservation_of_mass "Conservation of mass"). They are sometimes accompanied by an [equation of state](https://en.wikipedia.org/wiki/Equation_of_state "Equation of state") relating [pressure](https://en.wikipedia.org/wiki/Pressure "Pressure"), [temperature](https://en.wikipedia.org/wiki/Temperature "Temperature") and [density](https://en.wikipedia.org/wiki/Density "Density"). They arise from applying [Newton's second law](https://en.wikipedia.org/wiki/Newton%27s_second_law "Newton's second law") to [fluid motion](https://en.wikipedia.org/wiki/Fluid_dynamics "Fluid dynamics"), together with the assumption that the [stress](https://en.wikipedia.org/wiki/Stress_(mechanics) "Stress (mechanics)") in the fluid is the sum of a diffusing viscous term (proportional to the [gradient](https://en.wikipedia.org/wiki/Gradient "Gradient") of velocity) and a pressure term—hence describing *viscous flow*. The Navier–Stokes equations generalize the [Euler equations](https://en.wikipedia.org/wiki/Euler_equations_(fluid_dynamics) "Euler equations (fluid dynamics)") which only consider [inviscid flow](https://en.wikipedia.org/wiki/Inviscid_flow "Inviscid flow").

The Navier–Stokes equations are of great scientific and engineering interest because they may be used to model a wide variety of scenarios. In their full or simplified forms, they can assist in the design of [aircraft](https://en.wikipedia.org/wiki/Aircraft_design_process#Preliminary_design_phase "Aircraft design process") and cars, the study of [blood flow](https://en.wikipedia.org/wiki/Hemodynamics "Hemodynamics"), the design of [power stations](https://en.wikipedia.org/wiki/Power_station "Power station"), the analysis of [pollution](https://en.wikipedia.org/wiki/Pollution "Pollution"), and many other problems. Coupled with [Maxwell's equations](https://en.wikipedia.org/wiki/Maxwell%27s_equations "Maxwell's equations"), they comprise the fundamentals of [magnetohydrodynamics](https://en.wikipedia.org/wiki/Magnetohydrodynamics "Magnetohydrodynamics").

The Navier–Stokes equations are also of great interest to [pure mathematics](https://en.wikipedia.org/wiki/Pure_mathematics "Pure mathematics"). The [Navier–Stokes existence and smoothness](https://en.wikipedia.org/wiki/Navier%E2%80%93Stokes_existence_and_smoothness "Navier–Stokes existence and smoothness") problem concerns whether they have [smooth](https://en.wikipedia.org/wiki/Smoothness "Smoothness") (meaning infinitely differentiable) or bounded solutions in [three-dimensional Euclidean space](https://en.wikipedia.org/wiki/Three-dimensional_space "Three-dimensional space"), as opposed to a breakdown with unbounded solutions. This is one of seven [Millennium Prize Problems](https://en.wikipedia.org/wiki/Millennium_Prize_Problems "Millennium Prize Problems"), notable open mathematics problems for which the [Clay Mathematics Institute](https://en.wikipedia.org/wiki/Clay_Mathematics_Institute "Clay Mathematics Institute") offered $1 million prizes in 2000 for correct solutions. In September 2026, [OpenAI](https://en.wikipedia.org/wiki/OpenAI "OpenAI") announced a claimed counterexample to the existence and smoothness problem. The announcement was followed by a [priority dispute](https://en.wikipedia.org/wiki/Navier%E2%80%93Stokes_priority_controversy "Navier–Stokes priority controversy"), and the claimed counterexample has yet to be independently verified.

## Flow velocity

The solution of the equations is a [flow velocity](https://en.wikipedia.org/wiki/Flow_velocity "Flow velocity"). It is a [vector field](https://en.wikipedia.org/wiki/Vector_field "Vector field")—to every point in a [fluid](https://en.wikipedia.org/wiki/Fluid "Fluid"), at any moment in a time interval, it gives a vector whose direction and magnitude are those of the velocity of the fluid at that point in space and at that moment in time. It is studied in three spatial dimensions and one time dimension, and higher-dimensional analogues are studied in both pure and applied mathematics. Once the velocity field is calculated, other quantities of interest, such as [pressure](https://en.wikipedia.org/wiki/Pressure "Pressure") or [temperature](https://en.wikipedia.org/wiki/Temperature "Temperature"), may be found using [dynamical equations](https://en.wikipedia.org/wiki/Dynamical_systems "Dynamical systems") and relations. This is different from what one normally sees in [classical mechanics](https://en.wikipedia.org/wiki/Classical_mechanics "Classical mechanics"), where solutions are typically [trajectories](https://en.wikipedia.org/wiki/Trajectories "Trajectories") of the position of a [particle](https://en.wikipedia.org/wiki/Particle "Particle") or deflection of a [continuum](https://en.wikipedia.org/wiki/Continuum_(theory) "Continuum (theory)"). Studying velocity instead of position makes more sense for a fluid, although for visualization purposes, one can compute various [trajectories](https://en.wikipedia.org/wiki/Streamlines,_streaklines,_and_pathlines "Streamlines, streaklines, and pathlines"). In particular, the [streamlines](https://en.wikipedia.org/wiki/Streamlines,_streaklines,_and_pathlines "Streamlines, streaklines, and pathlines") of a vector field, interpreted as flow velocity, are the paths along which a massless fluid particle would travel. These paths are the [integral curves](https://en.wikipedia.org/wiki/Integral_curve "Integral curve") whose derivative at each point is equal to the vector field, and they can represent visually the behavior of the vector field at a point in time.

## General continuum equations

The Navier–Stokes momentum equation can be derived as a particular form of the [Cauchy momentum equation](https://en.wikipedia.org/wiki/Cauchy_momentum_equation "Cauchy momentum equation"), whose general convective form is:

D

u

D
t
=

1
ρ
∇
⋅

σ
+

a
.
{\displaystyle {\frac {\mathrm {D} \mathbf {u} }{\mathrm {D} t}}={\frac {1}{\rho }}\nabla \cdot {\boldsymbol {\sigma }}+\mathbf {a} .}
By setting the [Cauchy stress tensor](https://en.wikipedia.org/wiki/Cauchy_stress_tensor "Cauchy stress tensor")

σ
{\textstyle {\boldsymbol {\sigma }}}
 to be the sum of a viscosity term

τ
{\textstyle {\boldsymbol {\tau }}}
 (the [deviatoric stress](https://en.wikipedia.org/wiki/Deviatoric_stress "Deviatoric stress")) and a pressure term

−
p

I
{\textstyle -p\mathbf {I} }
 (volumetric stress), we arrive at:

**Cauchy momentum equation** *(convective form)*

ρ

D

u

D
t
=
−
∇
p
+
∇
⋅

τ
+
ρ

a
{\displaystyle \rho {\frac {\mathrm {D} \mathbf {u} }{\mathrm {D} t}}=-\nabla p+\nabla \cdot {\boldsymbol {\tau }}+\rho \,\mathbf {a} }

where

* D

  D
  t
  {\textstyle {\frac {\mathrm {D} }{\mathrm {D} t}}}
   is the [material derivative](https://en.wikipedia.org/wiki/Material_derivative "Material derivative"), defined as

  ∂

  ∂
  t
  +

  u
  ⋅
  ∇
  {\textstyle {\frac {\partial }{\partial t}}+\mathbf {u} \cdot \nabla }
  ,
* ρ
  {\textstyle \rho }
   is the (mass) density,
* u
  {\textstyle \mathbf {u} }
   is the flow velocity,
* ∇
  ⋅

  {\textstyle \nabla \cdot \,}
   is the [divergence](https://en.wikipedia.org/wiki/Divergence "Divergence"),
* p
  {\textstyle p}
   is the [pressure](https://en.wikipedia.org/wiki/Pressure "Pressure"),
* t
  {\textstyle t}
   is [time](https://en.wikipedia.org/wiki/Time "Time"),
* τ
  {\textstyle {\boldsymbol {\tau }}}
   is the [deviatoric stress tensor](https://en.wikipedia.org/wiki/Deviatoric_stress "Deviatoric stress"), which has order 2,
* a
  {\textstyle \mathbf {a} }
   represents [body accelerations](https://en.wikipedia.org/wiki/Body_force#acceleration "Body force") acting on the continuum, for example [gravity](https://en.wikipedia.org/wiki/Gravity "Gravity"), [inertial accelerations](https://en.wikipedia.org/wiki/Fictitious_force "Fictitious force"), [electrostatic accelerations](https://en.wikipedia.org/wiki/Coulomb%27s_law "Coulomb's law"), and so on.

In this form, it is apparent that in the assumption of an inviscid fluid – no deviatoric stress – Cauchy equations reduce to the [Euler equations](https://en.wikipedia.org/wiki/Euler_equations_(fluid_dynamics) "Euler equations (fluid dynamics)").

Assuming [conservation of mass](https://en.wikipedia.org/wiki/Conservation_of_mass "Conservation of mass"), with the known properties of [divergence](https://en.wikipedia.org/wiki/Divergence "Divergence") and [gradient](https://en.wikipedia.org/wiki/Gradient "Gradient") we can use the mass [continuity equation](https://en.wikipedia.org/wiki/Continuity_equation "Continuity equation"), which represents the mass per unit volume of a [homogenous](https://en.wikipedia.org/wiki/Homogenous "Homogenous") fluid with respect to space and time (i.e., [material derivative](https://en.wikipedia.org/wiki/Material_derivative "Material derivative")

D

D
t
{\textstyle {\frac {\mathbf {D} }{\mathbf {Dt} }}}
) of any finite volume (

V
{\textstyle \mathbf {V} }
) to represent the change of velocity in fluid media:

D
m

D
t
=

∭

V

(

D
ρ

D
t
+
ρ
(
∇
⋅

u
)
)

d
V

D
ρ

D
t
+
ρ
(
∇
⋅

u
)
=

∂
ρ

∂
t
+
(
∇
ρ
)
⋅

u
+
ρ
(
∇
⋅

u
)
=

∂
ρ

∂
t
+
∇
⋅
(
ρ

u
)
=
0
{\displaystyle {\begin{aligned}&{\frac {\mathbf {D} m}{\mathbf {Dt} }}=\iiint \limits \_{V}\left({\frac {\mathbf {D} \rho }{\mathbf {Dt} }}+\rho (\nabla \cdot \mathbf {u} )\right)\,dV\\[5pt]&{\frac {\mathbf {D} \rho }{\mathbf {Dt} }}+\rho (\nabla \cdot \mathbf {u} )={\frac {\partial \rho }{\partial t}}+(\nabla \rho )\cdot \mathbf {u} +\rho (\nabla \cdot \mathbf {u} )={\frac {\partial \rho }{\partial t}}+\nabla \cdot (\rho \mathbf {u} )=0\end{aligned}}}
where

* D
  m

  D
  t
  {\textstyle {\frac {\mathrm {D} m}{\mathrm {D} t}}}
   is the [material derivative](https://en.wikipedia.org/wiki/Material_derivative "Material derivative") of [mass](https://en.wikipedia.org/wiki/Mass "Mass") per unit volume ([density](https://en.wikipedia.org/wiki/Density "Density"),

  ρ
  {\displaystyle \rho }
  ),
* ∭

  V

  (
  F
  (

  x

  1
  ,

  x

  2
  ,

  x

  3
  ,
  t
  )

  )

  d
  V
  {\textstyle \iiint \limits \_{V}{\bigl (}F(x\_{1},x\_{2},x\_{3},t){\bigr )}\,dV}
   is the mathematical operation for the [integration throughout the volume](https://en.wikipedia.org/wiki/Volume_integral "Volume integral") (

  V
  {\textstyle V}
  ),
* ∂

  ∂
  t
  {\textstyle {\frac {\partial }{\partial t}}}
   is the [partial derivative](https://en.wikipedia.org/wiki/Partial_derivative "Partial derivative") mathematical operator,
* ∇
  ⋅

  u

  {\textstyle \nabla \cdot \mathbf {u} \,}
   is the [divergence](https://en.wikipedia.org/wiki/Divergence "Divergence") of the flow velocity (

  u
  {\displaystyle \mathbf {u} }
  ), which is a [scalar field](https://en.wikipedia.org/wiki/Scalar_field "Scalar field"),
* ∇
  ρ

  {\textstyle \nabla \rho \,}
   is the [gradient](https://en.wikipedia.org/wiki/Gradient "Gradient") of [density](https://en.wikipedia.org/wiki/Density "Density") (

  ρ
  {\displaystyle \rho }
  ), which is the vector derivative of a [scalar field](https://en.wikipedia.org/wiki/Scalar_field "Scalar field"),

to arrive at the conservation form of the equations of motion. This is often written:

**Cauchy momentum equation** *(conservation form)*

∂

∂
t
(
ρ

u
)
+
∇
⋅
(
ρ

u
⊗

u
)
=
−
∇
p
+
∇
⋅

τ
+
ρ

a
{\displaystyle {\frac {\partial }{\partial t}}(\rho \,\mathbf {u} )+\nabla \cdot (\rho \,\mathbf {u} \otimes \mathbf {u} )=-\nabla p+\nabla \cdot {\boldsymbol {\tau }}+\rho \,\mathbf {a} }

where

⊗
{\textstyle \otimes }
 is the [outer product](https://en.wikipedia.org/wiki/Outer_product "Outer product") of the flow velocity (

u
{\textstyle \mathbf {u} }
):

u
⊗

u
=

u

u

T
{\displaystyle \mathbf {u} \otimes \mathbf {u} =\mathbf {u} \mathbf {u} ^{\mathsf {T}}}

The left side of the equation describes acceleration, and may be composed of time-dependent and convective components (also the effects of non-inertial coordinates if present). The right side of the equation is in effect a summation of hydrostatic effects, the divergence of deviatoric stress and body forces (such as gravity).

All non-relativistic balance equations, such as the Navier–Stokes equations, can be derived by beginning with the Cauchy equations and specifying the stress tensor through a [constitutive relation](https://en.wikipedia.org/wiki/Constitutive_relation "Constitutive relation"). By expressing the deviatoric (shear) stress tensor in terms of [viscosity](https://en.wikipedia.org/wiki/Viscosity "Viscosity") and the fluid [velocity](https://en.wikipedia.org/wiki/Shear_velocity "Shear velocity") gradient, and assuming constant viscosity, the above Cauchy equations will lead to the Navier–Stokes equations below.

### Convective acceleration

A significant feature of the Cauchy equation and consequently all other continuum equations (including Euler and Navier–Stokes) is the presence of convective acceleration: the effect of acceleration of a flow with respect to space. While individual fluid particles indeed experience time-dependent acceleration, the convective acceleration of the flow field is a spatial effect, one example being fluid speeding up in a nozzle.

## Compressible flow

Remark: here, the deviatoric stress tensor is denoted

τ
{\textstyle {\boldsymbol {\tau }}}
 as it was in the [general continuum equations](#General_continuum_equations) and in the [incompressible flow section](#Incompressible_flow).

The compressible momentum Navier–Stokes equation results from the following assumptions on the Cauchy stress tensor:

* the stress is **[Galilean invariant](https://en.wikipedia.org/wiki/Galilean_invariance "Galilean invariance")**: it does not depend directly on the flow velocity, but only on spatial derivatives of the flow velocity. So the stress variable is the tensor gradient

  ∇

  u
  {\textstyle \nabla \mathbf {u} }
  , or more simply the [rate-of-strain tensor](https://en.wikipedia.org/wiki/Strain-rate_tensor "Strain-rate tensor"):

  ε

  (

  ∇

  u
  )
  ≡

  1
  2
  ∇

  u
  +

  1
  2

  (

  ∇

  u
  )

  T
  {\textstyle {\boldsymbol {\varepsilon }}\left(\nabla \mathbf {u} \right)\equiv {\frac {1}{2}}\nabla \mathbf {u} +{\frac {1}{2}}\left(\nabla \mathbf {u} \right)^{\mathsf {T}}}
* the deviatoric stress is **linear** in this variable:

  σ
  (

  ε
  )
  =
  −
  p

  I
  +

  C
  :

  ε
  {\textstyle {\boldsymbol {\sigma }}({\boldsymbol {\varepsilon }})=-p\mathbf {I} +\mathbf {C} :{\boldsymbol {\varepsilon }}}
  , where

  p
  {\textstyle p}
   is independent on the strain rate tensor,

  C
  {\textstyle \mathbf {C} }
   is the fourth-order tensor representing the constant of proportionality, called the viscosity or [elasticity tensor](https://en.wikipedia.org/wiki/Elasticity_tensor "Elasticity tensor"), and : is the [double-dot product](https://en.wikipedia.org/wiki/Dyadics#Double-dot_product "Dyadics").
* the fluid is assumed to be [isotropic](https://en.wikipedia.org/wiki/Isotropic "Isotropic"), as with gases and simple liquids, and consequently

  C
  {\textstyle \mathbf {C} }
   is an isotropic tensor; furthermore, since the deviatoric stress tensor is symmetric, by [Helmholtz decomposition](https://en.wikipedia.org/wiki/Helmholtz_decomposition "Helmholtz decomposition") it can be expressed in terms of two scalar [Lamé parameters](https://en.wikipedia.org/wiki/Lam%C3%A9_parameters "Lamé parameters"), the [second viscosity](https://en.wikipedia.org/wiki/Second_viscosity "Second viscosity")

  λ
  {\textstyle \lambda }
   and the [dynamic viscosity](https://en.wikipedia.org/wiki/Dynamic_viscosity "Dynamic viscosity")

  μ
  {\textstyle \mu }
  , as it is usual in [linear elasticity](https://en.wikipedia.org/wiki/Linear_elasticity "Linear elasticity"):

  **Linear stress [constitutive equation](https://en.wikipedia.org/wiki/Constitutive_equation "Constitutive equation")** *(expression similar to the one for elastic solid)*

  σ
  (

  ε
  )
  =
  −
  p

  I
  +
  λ
  tr
  ⁡
  (

  ε
  )

  I
  +
  2
  μ

  ε
  {\displaystyle {\boldsymbol {\sigma }}({\boldsymbol {\varepsilon }})=-p\mathbf {I} +\lambda \operatorname {tr} ({\boldsymbol {\varepsilon }})\mathbf {I} +2\mu {\boldsymbol {\varepsilon }}}

  where

  I
  {\textstyle \mathbf {I} }
   is the [identity tensor](https://en.wikipedia.org/wiki/Identity_matrix "Identity matrix"), and

  tr
  ⁡
  (

  ε
  )
  {\textstyle \operatorname {tr} ({\boldsymbol {\varepsilon }})}
   is the [trace](https://en.wikipedia.org/wiki/Trace_(linear_algebra) "Trace (linear algebra)") of the rate-of-strain tensor. So this decomposition can be explicitly defined as:

  σ
  =
  −
  p

  I
  +
  λ
  (
  ∇
  ⋅

  u
  )

  I
  +
  μ

  (

  ∇

  u
  +
  (
  ∇

  u

  )

  T
  )
  .
  {\displaystyle {\boldsymbol {\sigma }}=-p\mathbf {I} +\lambda (\nabla \cdot \mathbf {u} )\mathbf {I} +\mu \left(\nabla \mathbf {u} +(\nabla \mathbf {u} )^{\mathsf {T}}\right).}

Since the [trace](https://en.wikipedia.org/wiki/Trace_(linear_algebra) "Trace (linear algebra)") of the rate-of-strain tensor in three dimensions is the [divergence](https://en.wikipedia.org/wiki/Divergence "Divergence") (i.e. rate of expansion) of the flow:

tr
⁡
(

ε
)
=
∇
⋅

u
.
{\displaystyle \operatorname {tr} ({\boldsymbol {\varepsilon }})=\nabla \cdot \mathbf {u} .}

Given this relation, and since the trace of the identity tensor in three dimensions is three:

tr
⁡
(

I
)
=
3.
{\displaystyle \operatorname {tr} ({\boldsymbol {I}})=3.}

the trace of the stress tensor in three dimensions becomes:

tr
⁡
(

σ
)
=
−
3
p
+
(
3
λ
+
2
μ
)
∇
⋅

u
.
{\displaystyle \operatorname {tr} ({\boldsymbol {\sigma }})=-3p+(3\lambda +2\mu )\nabla \cdot \mathbf {u} .}

So by alternatively decomposing the stress tensor into **isotropic** and **deviatoric** parts, as usual in fluid dynamics:

σ
=
−

[

p
−

(

λ
+

2
3
μ
)

(

∇
⋅

u
)
]

I
+
μ

(

∇

u
+

(

∇

u
)

T
−

2
3

(

∇
⋅

u
)

I
)
{\displaystyle {\boldsymbol {\sigma }}=-\left[p-\left(\lambda +{\tfrac {2}{3}}\mu \right)\left(\nabla \cdot \mathbf {u} \right)\right]\mathbf {I} +\mu \left(\nabla \mathbf {u} +\left(\nabla \mathbf {u} \right)^{\mathsf {T}}-{\tfrac {2}{3}}\left(\nabla \cdot \mathbf {u} \right)\mathbf {I} \right)}

Introducing the [bulk viscosity](https://en.wikipedia.org/wiki/Volume_viscosity "Volume viscosity")

ζ
{\textstyle \zeta }
,

ζ
≡
λ
+

2
3
μ
,
{\displaystyle \zeta \equiv \lambda +{\tfrac {2}{3}}\mu ,}

we arrive at the linear [constitutive equation](https://en.wikipedia.org/wiki/Constitutive_equation "Constitutive equation") in the form usually employed in [thermal hydraulics](https://en.wikipedia.org/wiki/Thermal_hydraulics "Thermal hydraulics"):

**Linear stress constitutive equation** *(expression used for fluids)*

σ
=
−

[
p
−
ζ
(
∇
⋅

u
)

]

I
+
μ

[

∇

u
+
(
∇

u

)

T
−

2
3
(
∇
⋅

u
)

I
]
{\displaystyle {\boldsymbol {\sigma }}=-{\bigl [}p-\zeta (\nabla \cdot \mathbf {u} ){\bigr ]}\mathbf {I} +\mu \left[\nabla \mathbf {u} +(\nabla \mathbf {u} )^{\mathsf {T}}-{\tfrac {2}{3}}(\nabla \cdot \mathbf {u} )\mathbf {I} \right]}

which can also be arranged in the other usual form:

σ
=
−
p

I
+
μ

(

∇

u
+
(
∇

u

)

T
)
+

(

ζ
−

2
3
μ
)
(
∇
⋅

u
)

I
.
{\displaystyle {\boldsymbol {\sigma }}=-p\mathbf {I} +\mu \left(\nabla \mathbf {u} +(\nabla \mathbf {u} )^{\mathsf {T}}\right)+\left(\zeta -{\tfrac {2}{3}}\mu \right)(\nabla \cdot \mathbf {u} )\mathbf {I} .}

Note that in the compressible case the pressure is no more proportional to the [isotropic stress](https://en.wikipedia.org/wiki/Hydrostatic_stress "Hydrostatic stress") term, since there is the additional bulk viscosity term:

p
=
−

1
3
tr
⁡
(

σ
)
+
ζ
(
∇
⋅

u
)
{\displaystyle p=-{\tfrac {1}{3}}\operatorname {tr} ({\boldsymbol {\sigma }})+\zeta (\nabla \cdot \mathbf {u} )}

and the [deviatoric stress tensor](https://en.wikipedia.org/wiki/Deviatoric_stress_tensor "Deviatoric stress tensor")

σ
′
{\displaystyle {\boldsymbol {\sigma }}'}
 is still coincident with the shear stress tensor

τ
{\displaystyle {\boldsymbol {\tau }}}
 (i.e. the deviatoric stress in a Newtonian fluid has no normal stress components), and it has a compressibility term in addition to the incompressible case, which is proportional to the shear viscosity:

σ
′
=

τ
=
μ

[

∇

u
+
(
∇

u

)

T
−

2
3
(
∇
⋅

u
)

I
]
{\displaystyle {\boldsymbol {\sigma }}'={\boldsymbol {\tau }}=\mu \left[\nabla \mathbf {u} +(\nabla \mathbf {u} )^{\mathsf {T}}-{\tfrac {2}{3}}(\nabla \cdot \mathbf {u} )\mathbf {I} \right]}

Both bulk viscosity

ζ
{\textstyle \zeta }
 and dynamic viscosity

μ
{\textstyle \mu }
 need not be constant – in general, they depend on two thermodynamics variables if the fluid contains a single chemical species, say for example, pressure and temperature. Any equation that makes explicit one of these [transport coefficient](https://en.wikipedia.org/wiki/Transport_coefficient "Transport coefficient") in the [conservation variables](https://en.wikipedia.org/w/index.php?title=Conservation_variable&action=edit&redlink=1 "Conservation variable (page does not exist)") is called an [equation of state](https://en.wikipedia.org/wiki/Equation_of_state "Equation of state").

The most general of the Navier–Stokes equations become

**Navier–Stokes momentum equation** *(convective form)*

ρ

D

u

D
t
=
ρ

(

∂

u

∂
t
+
(

u
⋅
∇
)

u
)
=
−
∇
p
+
∇
⋅

(

μ

[

∇

u
+
(
∇

u

)

T
−

2
3
(
∇
⋅

u
)

I
]
)
+
∇
[
ζ
(
∇
⋅

u
)
]
+
ρ

a
.
{\displaystyle \rho {\frac {\mathrm {D} \mathbf {u} }{\mathrm {D} t}}=\rho \left({\frac {\partial \mathbf {u} }{\partial t}}+(\mathbf {u} \cdot \nabla )\mathbf {u} \right)=-\nabla p+\nabla \cdot \left(\mu \left[\nabla \mathbf {u} +(\nabla \mathbf {u} )^{\mathsf {T}}-{\tfrac {2}{3}}(\nabla \cdot \mathbf {u} )\mathbf {I} \right]\right)+\nabla [\zeta (\nabla \cdot \mathbf {u} )]+\rho \mathbf {a} .}

in index notation, the equation can be written as

**Navier–Stokes momentum equation** *(index notation)*

ρ

(

∂

u

i

∂
t
+

u

k

∂

u

i

∂

x

k
)
=
−

∂
p

∂

x

i
+

∂

∂

x

k

[

μ

(

∂

u

i

∂

x

k
+

∂

u

k

∂

x

i
−

2
3

δ

i
k

∂

u

l

∂

x

l
)
]
+

∂

∂

x

i

(

ζ

∂

u

ℓ

∂

x

ℓ
)
+
ρ

a

i
.
{\displaystyle \rho \left({\frac {\partial u\_{i}}{\partial t}}+u\_{k}{\frac {\partial u\_{i}}{\partial x\_{k}}}\right)=-{\frac {\partial p}{\partial x\_{i}}}+{\frac {\partial }{\partial x\_{k}}}\left[\mu \left({\frac {\partial u\_{i}}{\partial x\_{k}}}+{\frac {\partial u\_{k}}{\partial x\_{i}}}-{\tfrac {2}{3}}\delta \_{ik}{\frac {\partial u\_{l}}{\partial x\_{l}}}\right)\right]+{\frac {\partial }{\partial x\_{i}}}\left(\zeta {\frac {\partial u\_{\ell }}{\partial x\_{\ell }}}\right)+\rho a\_{i}.}

The corresponding equation in conservation form can be obtained by considering that, given the mass [continuity equation](https://en.wikipedia.org/wiki/Continuity_equation "Continuity equation"), the left side is equivalent to:

ρ

D

u

D
t
=

∂

∂
t
(
ρ

u
)
+
∇
⋅
(
ρ

u
⊗

u
)
{\displaystyle \rho {\frac {\mathrm {D} \mathbf {u} }{\mathrm {D} t}}={\frac {\partial }{\partial t}}(\rho \mathbf {u} )+\nabla \cdot (\rho \mathbf {u} \otimes \mathbf {u} )}

to give finally:

**Navier–Stokes momentum equation** *(conservative form)*

∂

∂
t
(
ρ

u
)
+
∇
⋅

(

ρ

u
⊗

u
+
[
p
−
ζ
(
∇
⋅

u
)
]

I
−
μ

[

∇

u
+
(
∇

u

)

T
−

2
3
(
∇
⋅

u
)

I
]
)
=
ρ

a
.
{\displaystyle {\frac {\partial }{\partial t}}(\rho \mathbf {u} )+\nabla \cdot \left(\rho \mathbf {u} \otimes \mathbf {u} +[p-\zeta (\nabla \cdot \mathbf {u} )]\mathbf {I} -\mu \left[\nabla \mathbf {u} +(\nabla \mathbf {u} )^{\mathsf {T}}-{\tfrac {2}{3}}(\nabla \cdot \mathbf {u} )\mathbf {I} \right]\right)=\rho \mathbf {a} .}

Apart from its dependence of pressure and temperature, the second viscosity coefficient also depends on the process, that is to say, the second viscosity coefficient is not just a material property. Example: in the case of a sound wave with a definitive frequency that alternatively compresses and expands a fluid element, the second viscosity coefficient depends on the frequency of the wave. This dependence is called the *dispersion*. In some cases, the [second viscosity](https://en.wikipedia.org/wiki/Volume_viscosity "Volume viscosity")

ζ
{\textstyle \zeta }
 can be assumed to be constant in which case, the effect of the volume viscosity

ζ
{\textstyle \zeta }
 is that the mechanical pressure is not equivalent to the thermodynamic [pressure](https://en.wikipedia.org/wiki/Pressure "Pressure"): as demonstrated below.

∇
⋅
(
∇
⋅

u
)

I
=
∇
(
∇
⋅

u
)
,

p
¯
≡
p
−
ζ

∇
⋅

u
,
{\displaystyle {\begin{aligned}&\nabla \cdot (\nabla \cdot \mathbf {u} )\mathbf {I} =\nabla (\nabla \cdot \mathbf {u} ),\\&{\bar {p}}\equiv p-\zeta \,\nabla \cdot \mathbf {u} ,\end{aligned}}}
However, this difference is usually neglected most of the time (that is whenever we are not dealing with processes such as sound absorption and attenuation of shock waves, where second viscosity coefficient becomes important) by explicitly assuming

ζ
=
0
{\textstyle \zeta =0}
. The assumption of setting

ζ
=
0
{\textstyle \zeta =0}
 is called as the **Stokes hypothesis**. The validity of Stokes hypothesis can be demonstrated for monoatomic gas both experimentally and from the kinetic theory; for other gases and liquids, Stokes hypothesis is generally incorrect. With the Stokes hypothesis, the Navier–Stokes equations become

**Navier–Stokes momentum equation** *(convective form, Stokes hypothesis)*

ρ

D

u

D
t
=
ρ

(

∂

u

∂
t
+
(

u
⋅
∇
)

u
)
=
−
∇
p
+
∇
⋅

(

μ

[

∇

u
+
(
∇

u

)

T
−

2
3
(
∇
⋅

u
)

I
]
)
+
ρ

a
.
{\displaystyle \rho {\frac {\mathrm {D} \mathbf {u} }{\mathrm {D} t}}=\rho \left({\frac {\partial \mathbf {u} }{\partial t}}+(\mathbf {u} \cdot \nabla )\mathbf {u} \right)=-\nabla p+\nabla \cdot \left(\mu \left[\nabla \mathbf {u} +(\nabla \mathbf {u} )^{\mathsf {T}}-{\tfrac {2}{3}}(\nabla \cdot \mathbf {u} )\mathbf {I} \right]\right)+\rho \mathbf {a} .}

If the dynamic

μ
{\displaystyle \mu }
 and bulk

ζ
{\displaystyle \zeta }
 viscosities are assumed to be uniform in space, the equations in convective form can be simplified further. By computing the divergence of the stress tensor, since the divergence of tensor

∇

u
{\textstyle \nabla \mathbf {u} }
 is

∇

2

u
{\textstyle \nabla ^{2}\mathbf {u} }
 and the divergence of tensor

(

∇

u
)

T
{\textstyle \left(\nabla \mathbf {u} \right)^{\mathsf {T}}}
 is

∇

(

∇
⋅

u
)
{\textstyle \nabla \left(\nabla \cdot \mathbf {u} \right)}
, one finally arrives to the compressible Navier–Stokes momentum equation:

**Navier–Stokes momentum equation** with uniform shear and bulk viscosities *(convective form)*

D

u

D
t
=
−

1
ρ
∇
p
+
ν

∇

2

u
+

(

1
3
ν
+
ξ
)

∇
(
∇
⋅

u
)
+

a
.
{\displaystyle {\frac {D\mathbf {u} }{Dt}}=-{\frac {1}{\rho }}\nabla p+\nu \,\nabla ^{2}\mathbf {u} +\left({\tfrac {1}{3}}\nu +\xi \right)\,\nabla (\nabla \cdot \mathbf {u} )+\mathbf {a} .}

where

D

D
t
{\textstyle {\frac {\mathrm {D} }{\mathrm {D} t}}}
 is the [material derivative](https://en.wikipedia.org/wiki/Material_derivative "Material derivative").

ν
=

μ
ρ
{\textstyle \nu ={\frac {\mu }{\rho }}}
 is the shear [kinematic viscosity](https://en.wikipedia.org/wiki/Kinematic_viscosity "Kinematic viscosity") and

ξ
=

ζ
ρ
{\textstyle \xi ={\frac {\zeta }{\rho }}}
 is the bulk kinematic viscosity. The left-hand side changes in the conservation form of the Navier–Stokes momentum equation.
By bringing the operator on the flow velocity on the left side, one also has:

**Navier–Stokes momentum equation** with uniform shear and bulk viscosities *(convective form)*

(

∂

∂
t
+

u
⋅
∇
−
ν

∇

2
−

(

1
3
ν
+
ξ
)

∇
(
∇
⋅
)
)

u
=
−

1
ρ
∇
p
+

a
.
{\displaystyle \left({\frac {\partial }{\partial t}}+\mathbf {u} \cdot \nabla -\nu \,\nabla ^{2}-\left({\tfrac {1}{3}}\nu +\xi \right)\,\nabla (\nabla \cdot )\right)\mathbf {u} =-{\frac {1}{\rho }}\nabla p+\mathbf {a} .}

The convective acceleration term can also be written as

u
⋅
∇

u
=
(
∇
×

u
)
×

u
+

1
2
∇

u

2
,
{\displaystyle \mathbf {u} \cdot \nabla \mathbf {u} =(\nabla \times \mathbf {u} )\times \mathbf {u} +{\tfrac {1}{2}}\nabla \mathbf {u} ^{2},}
where the vector

(
∇
×

u
)
×

u
{\textstyle (\nabla \times \mathbf {u} )\times \mathbf {u} }
 is known as the [Lamb vector](https://en.wikipedia.org/wiki/Lamb_vector "Lamb vector").

For the special case of an [incompressible flow](https://en.wikipedia.org/wiki/Incompressible_flow "Incompressible flow"), the pressure constrains the flow so that the volume of [fluid elements](https://en.wikipedia.org/wiki/Fluid_element "Fluid element") is constant: [isochoric flow](https://en.wikipedia.org/wiki/Isochoric_process "Isochoric process") resulting in a [solenoidal](https://en.wikipedia.org/wiki/Solenoidal_vector_field "Solenoidal vector field") velocity field with

∇
⋅

u
=
0
{\textstyle \nabla \cdot \mathbf {u} =0}
.

## Incompressible flow

The incompressible momentum Navier–Stokes equation results from the following assumptions on the Cauchy stress tensor:

* the stress is **[Galilean invariant](https://en.wikipedia.org/wiki/Galilean_invariance "Galilean invariance")**: it does not depend directly on the flow velocity, but only on spatial derivatives of the flow velocity. So the stress variable is the tensor gradient

  ∇

  u
  {\textstyle \nabla \mathbf {u} }
  .
* the fluid is assumed to be [isotropic](https://en.wikipedia.org/wiki/Isotropic "Isotropic"), as with gases and simple liquids, and consequently

  τ
  {\textstyle {\boldsymbol {\tau }}}
   is an isotropic tensor; furthermore, since the deviatoric stress tensor can be expressed in terms of the [dynamic viscosity](https://en.wikipedia.org/wiki/Dynamic_viscosity "Dynamic viscosity")

  μ
  {\textstyle \mu }
  :

  **Stokes' stress [constitutive equation](https://en.wikipedia.org/wiki/Constitutive_equation "Constitutive equation")** *(expression used for incompressible elastic solids)*

  :   τ
      =
      2
      μ

      ε
      {\displaystyle {\boldsymbol {\tau }}=2\mu {\boldsymbol {\varepsilon }}}

  where

  ε
  =

  1
  2

  (

  ∇
  u
  +

  ∇
  u

  T
  )
  {\displaystyle {\boldsymbol {\varepsilon }}={\tfrac {1}{2}}\left(\mathbf {\nabla u} +\mathbf {\nabla u} ^{\mathsf {T}}\right)}
  is the rate-of-[strain tensor](https://en.wikipedia.org/wiki/Strain_tensor "Strain tensor"). So this decomposition can be made explicit as:

  **Stokes's stress constitutive equation** *(expression used for incompressible viscous fluids)*

  :   τ
      =
      μ

      [

      ∇

      u
      +
      (
      ∇

      u

      )

      T
      ]
      {\displaystyle {\boldsymbol {\tau }}=\mu \left[\nabla \mathbf {u} +(\nabla \mathbf {u} )^{\mathsf {T}}\right]}

This constitutive equation is also called the **[Newtonian law of viscosity](https://en.wikipedia.org/wiki/Newtonian_fluid#Newtonian_law_of_viscosity "Newtonian fluid")**.
Dynamic viscosity μ need not be constant – in incompressible flows it can depend on density and on pressure. Any equation that makes explicit one of these [transport coefficient](https://en.wikipedia.org/wiki/Transport_coefficient "Transport coefficient") in the [conservative variables](https://en.wikipedia.org/w/index.php?title=Conservative_variable&action=edit&redlink=1 "Conservative variable (page does not exist)") is called an [equation of state](https://en.wikipedia.org/wiki/Equation_of_state "Equation of state").

The divergence of the deviatoric stress in case of uniform viscosity is given by:

∇
⋅

τ
=
2
μ
∇
⋅

ε
=
μ
∇
⋅

(

∇

u
+
∇

u

T
)
=
μ

∇

2

u
{\displaystyle \nabla \cdot {\boldsymbol {\tau }}=2\mu \nabla \cdot {\boldsymbol {\varepsilon }}=\mu \nabla \cdot \left(\nabla \mathbf {u} +\nabla \mathbf {u} ^{\mathsf {T}}\right)=\mu \,\nabla ^{2}\mathbf {u} }
because

∇
⋅

u
=
0
{\textstyle \nabla \cdot \mathbf {u} =0}
 for an incompressible fluid.

Incompressibility rules out density and pressure waves like sound or [shock waves](https://en.wikipedia.org/wiki/Shock_wave "Shock wave"), so this simplification is not useful if these phenomena are of interest. The incompressible flow assumption typically holds well with all fluids at low [Mach numbers](https://en.wikipedia.org/wiki/Mach_number "Mach number") (say up to about Mach 0.3), such as for modelling air winds at normal temperatures. the incompressible Navier–Stokes equations are best visualized by dividing for the density:

**[Incompressible](https://en.wikipedia.org/wiki/Incompressible_flow "Incompressible flow") Navier–Stokes equations** with uniform viscosity *(convective form)*

D

u

D
t
=

∂

u

∂
t
+
(

u
⋅
∇
)

u
=
ν

∇

2

u
−

1
ρ
∇
p
+

1
ρ

f
{\displaystyle {\frac {D\mathbf {u} }{Dt}}={\frac {\partial \mathbf {u} }{\partial t}}+(\mathbf {u} \cdot \nabla )\mathbf {u} =\nu \,\nabla ^{2}\mathbf {u} -{\frac {1}{\rho }}\nabla p+{\frac {1}{\rho }}\mathbf {f} }

where

ν
=

μ
ρ
{\textstyle \nu ={\frac {\mu }{\rho }}}
 is called the [kinematic viscosity](https://en.wikipedia.org/wiki/Kinematic_viscosity "Kinematic viscosity").
By isolating the fluid velocity, one can also state:

**[Incompressible](https://en.wikipedia.org/wiki/Incompressible_flow "Incompressible flow") Navier–Stokes equations** with constant viscosity *(alternative convective form)*

(

∂

∂
t
+

u
⋅
∇
−
ν

∇

2
)

u
=
−

1
ρ
∇
p
+

1
ρ

f
.
{\displaystyle \left({\frac {\partial }{\partial t}}+\mathbf {u} \cdot \nabla -\nu \,\nabla ^{2}\right)\mathbf {u} =-{\frac {1}{\rho }}\nabla p+{\frac {1}{\rho }}\mathbf {f} .}

If the density is constant throughout the fluid domain, or, in other words, if all fluid elements have the same density,

ρ
{\textstyle \rho }
, then we have

**[Incompressible](https://en.wikipedia.org/wiki/Incompressible_flow "Incompressible flow") Navier–Stokes equations with constant density and viscosity** *(convective form)*

D

u

D
t
=
ν

∇

2

u
−
∇

p
ρ
+

1
ρ

f
,
{\displaystyle {\frac {D\mathbf {u} }{Dt}}=\nu \,\nabla ^{2}\mathbf {u} -\nabla {\frac {p}{\rho }}+{\frac {1}{\rho }}\mathbf {f} ,}

where

p
ρ
{\textstyle {\frac {p}{\rho }}}
 is called the unit [pressure head](https://en.wikipedia.org/wiki/Pressure_head "Pressure head").

In incompressible flows, the pressure field satisfies the [Poisson equation](https://en.wikipedia.org/wiki/Poisson_equation "Poisson equation"),

∇

2
p
=
−
ρ

∂

u

i

∂

x

k

∂

u

k

∂

x

i
=
−
ρ

∂

2

u

i

u

k

∂

x

k

x

i
,
{\displaystyle \nabla ^{2}p=-\rho {\frac {\partial u\_{i}}{\partial x\_{k}}}{\frac {\partial u\_{k}}{\partial x\_{i}}}=-\rho {\frac {\partial ^{2}u\_{i}u\_{k}}{\partial x\_{k}x\_{i}}},}

which is obtained by taking the divergence of the momentum equations.

A laminar flow example

Velocity profile (laminar flow):

u

x
=
u
(
y
)
,

u

y
=
0
,

u

z
=
0
{\displaystyle u\_{x}=u(y),\quad u\_{y}=0,\quad u\_{z}=0}
for the x-direction, simplify the Navier–Stokes equation:

0
=
−

d
P

d
x
+
μ

(

d

2
u

d

y

2
)
{\displaystyle 0=-{\frac {\mathrm {d} P}{\mathrm {d} x}}+\mu \left({\frac {\mathrm {d} ^{2}u}{\mathrm {d} y^{2}}}\right)}

Integrate twice to find the velocity profile with boundary conditions

y
=
h
,
 
u
=
0
{\displaystyle y=h,\ u=0}
;

y
=
−
h
,
 
u
=
0
{\displaystyle y=-h,\ u=0}
:

u
=

1

2
μ

d
P

d
x

y

2
+
A
y
+
B
{\displaystyle u={\frac {1}{2\mu }}{\frac {\mathrm {d} P}{\mathrm {d} x}}y^{2}+Ay+B}

From this equation, substitute in the two boundary conditions to get two equations:

0

=

1

2
μ

d
P

d
x

h

2
+
A
h
+
B

0

=

1

2
μ

d
P

d
x

h

2
−
A
h
+
B
{\displaystyle {\begin{aligned}0&={\frac {1}{2\mu }}{\frac {\mathrm {d} P}{\mathrm {d} x}}h^{2}+Ah+B\\0&={\frac {1}{2\mu }}{\frac {\mathrm {d} P}{\mathrm {d} x}}h^{2}-Ah+B\end{aligned}}}

Add and solve for

B
{\displaystyle B}
:

B
=
−

1

2
μ

d
P

d
x

h

2
{\displaystyle B=-{\frac {1}{2\mu }}{\frac {\mathrm {d} P}{\mathrm {d} x}}h^{2}}

Substitute and solve for

A
{\displaystyle A}
:

A
=
0
{\displaystyle A=0}

Finally this gives the velocity profile:

u
=

1

2
μ

d
P

d
x

(

y

2
−

h

2
)
{\displaystyle u={\frac {1}{2\mu }}{\frac {\mathrm {d} P}{\mathrm {d} x}}\left(y^{2}-h^{2}\right)}

It is well worth observing the meaning of each term (compare to the [Cauchy momentum equation](https://en.wikipedia.org/wiki/Cauchy_momentum_equation "Cauchy momentum equation")):

∂

u

∂
t
⏟

Variation
+

(

u
⋅
∇
)

u
⏟

Convective

acceleration
⏞

Inertia (per volume)
=

∂
∂

−
∇
w
⏟

Internal

source
+

ν

∇

2

u
⏟

Diffusion
⏞

Divergence of stress
+

g
⏟

External

source
.
{\displaystyle \overbrace {{\vphantom {\frac {}{}}}\underbrace {\frac {\partial \mathbf {u} }{\partial t}} \_{\text{Variation}}+\underbrace {{\vphantom {\frac {}{}}}(\mathbf {u} \cdot \nabla )\mathbf {u} } \_{\begin{smallmatrix}{\text{Convective}}\\{\text{acceleration}}\end{smallmatrix}}} ^{\text{Inertia (per volume)}}=\overbrace {{\vphantom {\frac {\partial }{\partial }}}\underbrace {{\vphantom {\frac {}{}}}-\nabla w} \_{\begin{smallmatrix}{\text{Internal}}\\{\text{source}}\end{smallmatrix}}+\underbrace {{\vphantom {\frac {}{}}}\nu \nabla ^{2}\mathbf {u} } \_{\text{Diffusion}}} ^{\text{Divergence of stress}}+\underbrace {{\vphantom {\frac {}{}}}\mathbf {g} } \_{\begin{smallmatrix}{\text{External}}\\{\text{source}}\end{smallmatrix}}.}

The higher-order term, namely the [shear stress](https://en.wikipedia.org/wiki/Shear_stress "Shear stress") divergence

∇
⋅

τ
{\textstyle \nabla \cdot {\boldsymbol {\tau }}}
, has simply reduced to the [vector Laplacian](https://en.wikipedia.org/wiki/Vector_Laplacian "Vector Laplacian") term

μ

∇

2

u
{\textstyle \mu \nabla ^{2}\mathbf {u} }
. This Laplacian term can be interpreted as the difference between the velocity at a point and the mean velocity in a small surrounding volume. This implies that – for a Newtonian fluid – viscosity operates as a *diffusion of momentum*, in much the same way as the [heat conduction](https://en.wikipedia.org/wiki/Heat_conduction "Heat conduction"). In fact neglecting the convection term, incompressible Navier–Stokes equations lead to a vector [diffusion equation](https://en.wikipedia.org/wiki/Diffusion_equation "Diffusion equation") (namely [Stokes equations](https://en.wikipedia.org/wiki/Stokes_flow "Stokes flow")), but in general the convection term is present, so incompressible Navier–Stokes equations belong to the class of [convection–diffusion equations](https://en.wikipedia.org/wiki/Convection%E2%80%93diffusion_equation "Convection–diffusion equation").

In the usual case of an external field being a [conservative field](https://en.wikipedia.org/wiki/Conservative_field "Conservative field"):

g
=
−
∇
φ
{\displaystyle \mathbf {g} =-\nabla \varphi }
by defining the [hydraulic head](https://en.wikipedia.org/wiki/Hydraulic_head "Hydraulic head"):

h
≡
w
+
φ
{\displaystyle h\equiv w+\varphi }

one can finally condense the whole source in one term, arriving to the incompressible Navier–Stokes equation with conservative external field:

∂

u

∂
t
+
(

u
⋅
∇
)

u
−
ν

∇

2

u
=
−
∇
h
.
{\displaystyle {\frac {\partial \mathbf {u} }{\partial t}}+(\mathbf {u} \cdot \nabla )\mathbf {u} -\nu \,\nabla ^{2}\mathbf {u} =-\nabla h.}

The incompressible Navier–Stokes equations with uniform density and viscosity and conservative external field is the **fundamental equation of [hydraulics](https://en.wikipedia.org/wiki/Hydraulics "Hydraulics")**. The domain for these equations is commonly a 3 or fewer dimensional [Euclidean space](https://en.wikipedia.org/wiki/Euclidean_space "Euclidean space"), for which an [orthogonal coordinate](https://en.wikipedia.org/wiki/Orthogonal_coordinate "Orthogonal coordinate") reference frame is usually set to explicit the system of scalar partial differential equations to be solved. In 3-dimensional orthogonal coordinate systems are 3: [Cartesian](https://en.wikipedia.org/wiki/Cartesian_coordinate_system "Cartesian coordinate system"), [cylindrical](https://en.wikipedia.org/wiki/Cylindrical_coordinate_system "Cylindrical coordinate system"), and [spherical](https://en.wikipedia.org/wiki/Spherical_coordinate_system "Spherical coordinate system"). Expressing the Navier–Stokes vector equation in Cartesian coordinates is quite straightforward and not much influenced by the number of dimensions of the euclidean space employed, and this is the case also for the first-order terms (like the variation and convection ones) also in non-cartesian orthogonal coordinate systems. But for the higher order terms (the two coming from the divergence of the deviatoric stress that distinguish Navier–Stokes equations from Euler equations) some [tensor calculus](https://en.wikipedia.org/wiki/Tensor_calculus "Tensor calculus") is required for deducing an expression in non-cartesian orthogonal coordinate systems.
A special case of the fundamental equation of hydraulics is the [Bernoulli's equation](https://en.wikipedia.org/wiki/Bernoulli%27s_equation "Bernoulli's equation").

The incompressible Navier–Stokes equation is composite, the sum of two orthogonal equations,

∂

u

∂
t

=

Π

S

(

−
(

u
⋅
∇
)

u
+
ν

∇

2

u
)
+

f

S

ρ

−
1

∇
p

=

Π

I

(

−
(

u
⋅
∇
)

u
+
ν

∇

2

u
)
+

f

I
{\displaystyle {\begin{aligned}{\frac {\partial \mathbf {u} }{\partial t}}&=\Pi ^{S}\left(-(\mathbf {u} \cdot \nabla )\mathbf {u} +\nu \,\nabla ^{2}\mathbf {u} \right)+\mathbf {f} ^{S}\\\rho ^{-1}\,\nabla p&=\Pi ^{I}\left(-(\mathbf {u} \cdot \nabla )\mathbf {u} +\nu \,\nabla ^{2}\mathbf {u} \right)+\mathbf {f} ^{I}\end{aligned}}}
where

Π

S
{\textstyle \Pi ^{S}}
 and

Π

I
{\textstyle \Pi ^{I}}
 are solenoidal and [irrotational](https://en.wikipedia.org/wiki/Conservative_vector_field "Conservative vector field") projection operators satisfying

Π

S
+

Π

I
=
1
{\textstyle \Pi ^{S}+\Pi ^{I}=1}
, and

f

S
{\textstyle \mathbf {f} ^{S}}
 and

f

I
{\textstyle \mathbf {f} ^{I}}
 are the non-conservative and conservative parts of the body force. This result follows from the [Helmholtz theorem](https://en.wikipedia.org/wiki/Helmholtz_decomposition "Helmholtz decomposition") (also known as the fundamental theorem of vector calculus). The first equation is a pressureless governing equation for the velocity, while the second equation for the pressure is a functional of the velocity and is related to the pressure Poisson equation.

The explicit functional form of the projection operator in 3D is found from the Helmholtz theorem:

Π

S

F
(

r
)
=

1

4
π
∇
×
∫

∇

′
×

F
(

r
′
)

|

r
−

r
′

|

d

V
′
,

Π

I
=
1
−

Π

S
{\displaystyle \Pi ^{S}\,\mathbf {F} (\mathbf {r} )={\frac {1}{4\pi }}\nabla \times \int {\frac {\nabla ^{\prime }\times \mathbf {F} (\mathbf {r} ')}{|\mathbf {r} -\mathbf {r} '|}}\,\mathrm {d} V',\quad \Pi ^{I}=1-\Pi ^{S}}
with a similar structure in 2D. Thus the governing equation is an [integro-differential equation](https://en.wikipedia.org/wiki/Integro-differential_equation "Integro-differential equation") similar to [Coulomb's](https://en.wikipedia.org/wiki/Coulomb%27s_law "Coulomb's law") and [Biot–Savart's law](https://en.wikipedia.org/wiki/Biot%E2%80%93Savart_law "Biot–Savart law"), not convenient for numerical computation.

An equivalent weak or variational form of the equation, proved to produce the same velocity solution as the Navier–Stokes equation, is given by,

(

w
,

∂

u

∂
t
)
=
−

(

w
,

(

u
⋅
∇
)

u

)
−
ν

(

∇

w
:
∇

u
)
+

(

w
,

f

S
)
{\displaystyle \left(\mathbf {w} ,{\frac {\partial \mathbf {u} }{\partial t}}\right)=-{\bigl (}\mathbf {w} ,\left(\mathbf {u} \cdot \nabla \right)\mathbf {u} {\bigr )}-\nu \left(\nabla \mathbf {w} :\nabla \mathbf {u} \right)+\left(\mathbf {w} ,\mathbf {f} ^{S}\right)}

for divergence-free test functions

w
{\textstyle \mathbf {w} }
 satisfying appropriate boundary conditions. Here, the projections are accomplished by the orthogonality of the solenoidal and irrotational function spaces. The discrete form of this is eminently suited to finite element computation of divergence-free flow, as we shall see in the next section. There, one will be able to address the question, "How does one specify pressure-driven (Poiseuille) problems with a pressureless governing equation?".

The absence of pressure forces from the governing velocity equation demonstrates that the equation is not a dynamic one, but rather a kinematic equation where the divergence-free condition serves the role of a conservation equation. This would seem to refute the frequent statements that the incompressible pressure enforces the divergence-free condition.

### Weak form of the incompressible Navier–Stokes equations

#### Strong form

Consider the incompressible Navier–Stokes equations for a [Newtonian fluid](https://en.wikipedia.org/wiki/Newtonian_fluid "Newtonian fluid") of constant density

ρ
{\textstyle \rho }
 in a domain

Ω
⊂

R

d

(
d
=
2
,
3
)
{\displaystyle \Omega \subset \mathbb {R} ^{d}\quad (d=2,3)}
with boundary

∂
Ω
=

Γ

D
∪

Γ

N
,
{\displaystyle \partial \Omega =\Gamma \_{D}\cup \Gamma \_{N},}
being

Γ

D
{\textstyle \Gamma \_{D}}
 and

Γ

N
{\textstyle \Gamma \_{N}}
 portions of the boundary where respectively a [Dirichlet](https://en.wikipedia.org/wiki/Dirichlet_boundary_condition "Dirichlet boundary condition") and a [Neumann boundary condition](https://en.wikipedia.org/wiki/Neumann_boundary_condition "Neumann boundary condition") is applied (

Γ

D
∩

Γ

N
=
∅
{\textstyle \Gamma \_{D}\cap \Gamma \_{N}=\emptyset }
):

{

ρ

∂

u

∂
t
+
ρ
(

u
⋅
∇
)

u
−
∇
⋅

σ
(

u
,
p
)
=

f

 in 
Ω
×
(
0
,
T
)

∇
⋅

u
=
0

 in 
Ω
×
(
0
,
T
)

u
=

g

 on 

Γ

D
×
(
0
,
T
)

σ
(

u
,
p
)

n
^
=

h

 on 

Γ

N
×
(
0
,
T
)

u
(
0
)
=

u

0

 in 
Ω
×
{
0
}

{\displaystyle {\begin{cases}\rho {\dfrac {\partial \mathbf {u} }{\partial t}}+\rho (\mathbf {u} \cdot \nabla )\mathbf {u} -\nabla \cdot {\boldsymbol {\sigma }}(\mathbf {u} ,p)=\mathbf {f} &{\text{ in }}\Omega \times (0,T)\\\nabla \cdot \mathbf {u} =0&{\text{ in }}\Omega \times (0,T)\\\mathbf {u} =\mathbf {g} &{\text{ on }}\Gamma \_{D}\times (0,T)\\{\boldsymbol {\sigma }}(\mathbf {u} ,p){\hat {\mathbf {n} }}=\mathbf {h} &{\text{ on }}\Gamma \_{N}\times (0,T)\\\mathbf {u} (0)=\mathbf {u} \_{0}&{\text{ in }}\Omega \times \{0\}\end{cases}}}

u
{\textstyle \mathbf {u} }
 is the fluid velocity,

p
{\textstyle p}
 the fluid pressure,

f
{\textstyle \mathbf {f} }
 a given forcing term,

n
^
{\displaystyle {\hat {\mathbf {n} }}}
 the outward directed unit normal vector to

Γ

N
{\textstyle \Gamma \_{N}}
, and

σ
(

u
,
p
)
{\textstyle {\boldsymbol {\sigma }}(\mathbf {u} ,p)}
 the [viscous stress tensor](https://en.wikipedia.org/wiki/Viscous_stress_tensor "Viscous stress tensor") defined as:

σ
(

u
,
p
)
=
−
p

I
+
2
μ

ε
(

u
)
.
{\displaystyle {\boldsymbol {\sigma }}(\mathbf {u} ,p)=-p\mathbf {I} +2\mu {\boldsymbol {\varepsilon }}(\mathbf {u} ).}
Let

μ
{\textstyle \mu }
 be the dynamic viscosity of the fluid,

I
{\textstyle \mathbf {I} }
 the second-order [identity tensor](https://en.wikipedia.org/wiki/Identity_matrix "Identity matrix") and

ε
(

u
)
{\textstyle {\boldsymbol {\varepsilon }}(\mathbf {u} )}
 the [strain-rate tensor](https://en.wikipedia.org/wiki/Strain-rate_tensor "Strain-rate tensor") defined as:

ε
(

u
)
=

1
2

(

(

∇

u
)
+

(

∇

u
)

T
)
.
{\displaystyle {\boldsymbol {\varepsilon }}(\mathbf {u} )={\tfrac {1}{2}}\left(\left(\nabla \mathbf {u} \right)+\left(\nabla \mathbf {u} \right)^{\mathsf {T}}\right).}
The functions

g
{\textstyle \mathbf {g} }
 and

h
{\textstyle \mathbf {h} }
 are given Dirichlet and Neumann boundary data, while

u

0
{\textstyle \mathbf {u} \_{0}}
 is the [initial condition](https://en.wikipedia.org/wiki/Initial_condition "Initial condition"). The first equation is the momentum balance equation, while the second represents the [mass conservation](https://en.wikipedia.org/wiki/Conservation_of_mass "Conservation of mass"), namely the [continuity equation](https://en.wikipedia.org/wiki/Continuity_equation "Continuity equation").
Assuming constant dynamic viscosity, using the vectorial identity

∇
⋅

(

∇

f
)

T
=
∇
(
∇
⋅

f
)
{\displaystyle \nabla \cdot \left(\nabla \mathbf {f} \right)^{\mathsf {T}}=\nabla (\nabla \cdot \mathbf {f} )}
and exploiting mass conservation, the divergence of the total stress tensor in the momentum equation can also be expressed as:

∇
⋅

σ
(

u
,
p
)

=
∇
⋅

(

−
p

I
+
2
μ

ε
(

u
)
)

=
−
∇
p
+
2
μ
∇
⋅

ε
(

u
)

=
−
∇
p
+
2
μ
∇
⋅

[

1
2

(

(

∇

u
)
+

(

∇

u
)

T
)
]

=
−
∇
p
+
μ

(

Δ

u
+
∇
⋅

(

∇

u
)

T
)

=
−
∇
p
+
μ

(
Δ

u
+
∇

(
∇
⋅

u
)
⏟

=
0

)
=
−
∇
p
+
μ

Δ

u
.
{\displaystyle {\begin{aligned}\nabla \cdot {\boldsymbol {\sigma }}(\mathbf {u} ,p)&=\nabla \cdot \left(-p\mathbf {I} +2\mu {\boldsymbol {\varepsilon }}(\mathbf {u} )\right)\\&=-\nabla p+2\mu \nabla \cdot {\boldsymbol {\varepsilon }}(\mathbf {u} )\\&=-\nabla p+2\mu \nabla \cdot \left[{\tfrac {1}{2}}\left(\left(\nabla \mathbf {u} \right)+\left(\nabla \mathbf {u} \right)^{\mathsf {T}}\right)\right]\\&=-\nabla p+\mu \left(\Delta \mathbf {u} +\nabla \cdot \left(\nabla \mathbf {u} \right)^{\mathsf {T}}\right)\\&=-\nabla p+\mu {\bigl (}\Delta \mathbf {u} +\nabla \underbrace {(\nabla \cdot \mathbf {u} )} \_{=0}{\bigr )}=-\nabla p+\mu \,\Delta \mathbf {u} .\end{aligned}}}
Moreover, note that the Neumann boundary conditions can be rearranged as:

σ
(

u
,
p
)

n
^
=

(
−
p

I
+
2
μ

ε
(

u
)

)

n
^
=
−
p

n
^
+
μ

∂

u

∂

n
^
.
{\displaystyle {\boldsymbol {\sigma }}(\mathbf {u} ,p){\hat {\mathbf {n} }}={\bigl (}-p\mathbf {I} +2\mu {\boldsymbol {\varepsilon }}(\mathbf {u} ){\bigr )}{\hat {\mathbf {n} }}=-p{\hat {\mathbf {n} }}+\mu {\frac {\partial {\boldsymbol {u}}}{\partial {\hat {\mathbf {n} }}}}.}

#### Weak form

In order to find the weak form of the Navier–Stokes equations, firstly, consider the momentum equation

ρ

∂

u

∂
t
−
μ
Δ

u
+
ρ
(

u
⋅
∇
)

u
+
∇
p
=

f
{\displaystyle \rho {\frac {\partial \mathbf {u} }{\partial t}}-\mu \Delta \mathbf {u} +\rho (\mathbf {u} \cdot \nabla )\mathbf {u} +\nabla p=\mathbf {f} }
multiply it for a test function

v
{\textstyle \mathbf {v} }
, defined in a suitable space

V
{\textstyle V}
, and integrate both members with respect to the domain

Ω
{\textstyle \Omega }
:

∫

Ω
ρ

∂

u

∂
t
⋅

v
−

∫

Ω
μ
Δ

u
⋅

v
+

∫

Ω
ρ
(

u
⋅
∇
)

u
⋅

v
+

∫

Ω
∇
p
⋅

v
=

∫

Ω

f
⋅

v
{\displaystyle \int \limits \_{\Omega }\rho {\frac {\partial \mathbf {u} }{\partial t}}\cdot \mathbf {v} -\int \limits \_{\Omega }\mu \Delta \mathbf {u} \cdot \mathbf {v} +\int \limits \_{\Omega }\rho (\mathbf {u} \cdot \nabla )\mathbf {u} \cdot \mathbf {v} +\int \limits \_{\Omega }\nabla p\cdot \mathbf {v} =\int \limits \_{\Omega }\mathbf {f} \cdot \mathbf {v} }
Counter-integrating by parts the diffusive and the pressure terms and by using Gauss's theorem:

−

∫

Ω
μ
Δ

u
⋅

v

=

∫

Ω
μ
∇

u
⋅
∇

v
−

∫

∂
Ω
μ

∂

u

∂

n
^
⋅

v

∫

Ω
∇
p
⋅

v

=
−

∫

Ω
p
∇
⋅

v
+

∫

∂
Ω
p

v
⋅

n
^
{\displaystyle {\begin{aligned}-\int \limits \_{\Omega }\mu \Delta \mathbf {u} \cdot \mathbf {v} &=\int \limits \_{\Omega }\mu \nabla \mathbf {u} \cdot \nabla \mathbf {v} -\int \limits \_{\partial \Omega }\mu {\frac {\partial \mathbf {u} }{\partial {\hat {\mathbf {n} }}}}\cdot \mathbf {v} \\\int \limits \_{\Omega }\nabla p\cdot \mathbf {v} &=-\int \limits \_{\Omega }p\nabla \cdot \mathbf {v} +\int \limits \_{\partial \Omega }p\mathbf {v} \cdot {\hat {\mathbf {n} }}\end{aligned}}}

Using these relations, one gets:

∫

Ω
ρ

∂

u

∂
t
⋅

v
+

∫

Ω
μ
∇

u
⋅
∇

v
+

∫

Ω
ρ
(

u
⋅
∇
)

u
⋅

v
−

∫

Ω
p
∇
⋅

v
=

∫

Ω

f
⋅

v
+

∫

∂
Ω

(

μ

∂

u

∂

n
^
−
p

n
^
)
⋅

v

∀

v
∈
V
.
{\displaystyle \int \limits \_{\Omega }\rho {\dfrac {\partial \mathbf {u} }{\partial t}}\cdot \mathbf {v} +\int \limits \_{\Omega }\mu \nabla \mathbf {u} \cdot \nabla \mathbf {v} +\int \limits \_{\Omega }\rho (\mathbf {u} \cdot \nabla )\mathbf {u} \cdot \mathbf {v} -\int \limits \_{\Omega }p\nabla \cdot \mathbf {v} =\int \limits \_{\Omega }\mathbf {f} \cdot \mathbf {v} +\int \limits \_{\partial \Omega }\left(\mu {\frac {\partial \mathbf {u} }{\partial {\hat {\mathbf {n} }}}}-p{\hat {\mathbf {n} }}\right)\cdot \mathbf {v} \quad \forall \mathbf {v} \in V.}
In the same fashion, the continuity equation is multiplied for a test function

q
{\textstyle q}
 belonging to a space

Q
{\textstyle Q}
 and integrated in the domain

Ω
{\textstyle \Omega }
:

∫

Ω
q
∇
⋅

u
=
0.

∀
q
∈
Q
.
{\displaystyle \int \limits \_{\Omega }q\nabla \cdot \mathbf {u} =0.\quad \forall q\in Q.}
The space functions are chosen as follows:

V
=

[

H

0

1
(
Ω
)
]

d

=

{

v
∈

[

H

1
(
Ω
)
]

d
:

v
=

0

 on 

Γ

D
}
,

Q

=

L

2
(
Ω
)
{\displaystyle {\begin{aligned}V=\left[H\_{0}^{1}(\Omega )\right]^{d}&=\left\{\mathbf {v} \in \left[H^{1}(\Omega )\right]^{d}:\quad \mathbf {v} =\mathbf {0} {\text{ on }}\Gamma \_{D}\right\},\\Q&=L^{2}(\Omega )\end{aligned}}}
Considering that the test function

v
{\textstyle \mathbf {v} }
 vanishes on the Dirichlet boundary and considering the Neumann condition, the integral on the boundary can be rearranged as:

∫

∂
Ω

(

μ

∂

u

∂

n
^
−
p

n
^
)
⋅

v
=

∫

Γ

D

(

μ

∂

u

∂

n
^
−
p

n
^
)
⋅

v
⏟

v
=

0

 on 

Γ

D
 
+

∫

Γ

N

∫

Γ

N

(

μ

∂

u

∂

n
^
−
p

n
^
)
⏟

=

h

 on 

Γ

N
⋅

v
=

∫

Γ

N

h
⋅

v
.
{\displaystyle \int \limits \_{\partial \Omega }\left(\mu {\frac {\partial \mathbf {u} }{\partial {\hat {\mathbf {n} }}}}-p{\hat {\mathbf {n} }}\right)\cdot \mathbf {v} =\underbrace {\int \limits \_{\Gamma \_{D}}\left(\mu {\frac {\partial \mathbf {u} }{\partial {\hat {\mathbf {n} }}}}-p{\hat {\mathbf {n} }}\right)\cdot \mathbf {v} } \_{\mathbf {v} =\mathbf {0} {\text{ on }}\Gamma \_{D}\ }+\int \limits \_{\Gamma \_{N}}\underbrace {{\vphantom {\int \limits \_{\Gamma \_{N}}}}\left(\mu {\frac {\partial \mathbf {u} }{\partial {\hat {\mathbf {n} }}}}-p{\hat {\mathbf {n} }}\right)} \_{=\mathbf {h} {\text{ on }}\Gamma \_{N}}\cdot \mathbf {v} =\int \limits \_{\Gamma \_{N}}\mathbf {h} \cdot \mathbf {v} .}
Having this in mind, the [weak formulation](https://en.wikipedia.org/wiki/Weak_formulation "Weak formulation") of the Navier–Stokes equations is expressed as:

find 

u
∈

L

2

(

R

+

[

H

1
(
Ω
)
]

d
)
∩

C

0

(

R

+

[

L

2
(
Ω
)
]

d
)

 such that: 

{

∫

Ω
ρ

∂

u

∂
t
⋅

v
+

∫

Ω
μ
∇

u
⋅
∇

v
+

∫

Ω
ρ
(

u
⋅
∇
)

u
⋅

v
−

∫

Ω
p
∇
⋅

v
=

∫

Ω

f
⋅

v
+

∫

Γ

N

h
⋅

v

∀

v
∈
V
,

∫

Ω
q
∇
⋅

u
=
0

∀
q
∈
Q
.

{\displaystyle {\begin{aligned}&{\text{find }}\mathbf {u} \in L^{2}\left(\mathbb {R} ^{+}\;\left[H^{1}(\Omega )\right]^{d}\right)\cap C^{0}\left(\mathbb {R} ^{+}\;\left[L^{2}(\Omega )\right]^{d}\right){\text{ such that: }}\\[5pt]&\quad {\begin{cases}\displaystyle \int \limits \_{\Omega }\rho {\dfrac {\partial \mathbf {u} }{\partial t}}\cdot \mathbf {v} +\int \limits \_{\Omega }\mu \nabla \mathbf {u} \cdot \nabla \mathbf {v} +\int \limits \_{\Omega }\rho (\mathbf {u} \cdot \nabla )\mathbf {u} \cdot \mathbf {v} -\int \limits \_{\Omega }p\nabla \cdot \mathbf {v} =\int \limits \_{\Omega }\mathbf {f} \cdot \mathbf {v} +\int \limits \_{\Gamma \_{N}}\mathbf {h} \cdot \mathbf {v} \quad \forall \mathbf {v} \in V,\\\displaystyle \int \limits \_{\Omega }q\nabla \cdot \mathbf {u} =0\quad \forall q\in Q.\end{cases}}\end{aligned}}}

### Discrete velocity

With partitioning of the problem domain and defining [basis functions](https://en.wikipedia.org/wiki/Basis_function "Basis function") on the partitioned domain, the discrete form of the governing equation is

(

w

i
,

∂

u

j

∂
t
)
=
−

(

w

i
,

(

u
⋅
∇
)

u

j

)
−
ν

(

∇

w

i
:
∇

u

j
)
+

(

w

i
,

f

S
)
.
{\displaystyle \left(\mathbf {w} \_{i},{\frac {\partial \mathbf {u} \_{j}}{\partial t}}\right)=-{\bigl (}\mathbf {w} \_{i},\left(\mathbf {u} \cdot \nabla \right)\mathbf {u} \_{j}{\bigr )}-\nu \left(\nabla \mathbf {w} \_{i}:\nabla \mathbf {u} \_{j}\right)+\left(\mathbf {w} \_{i},\mathbf {f} ^{S}\right).}

It is desirable to choose basis functions that reflect the essential feature of incompressible flow – the elements must be divergence-free. While the velocity is the variable of interest, the existence of the stream function or vector potential is necessary by the Helmholtz theorem. Further, to determine fluid flow in the absence of a pressure gradient, one can specify the difference of stream function values across a 2D channel, or the [line integral](https://en.wikipedia.org/wiki/Line_integral "Line integral") of the tangential component of the vector potential around the channel in 3D, the flow being given by [Stokes' theorem](https://en.wikipedia.org/wiki/Stokes%27_theorem "Stokes' theorem"). Discussion will be restricted to 2D in the following.

We further restrict discussion to continuous Hermite finite elements which have at least first-derivative degrees-of-freedom. With this, one can draw a large number of candidate triangular and rectangular elements from the [plate-bending](https://en.wikipedia.org/wiki/Bending_of_plates "Bending of plates") literature. These elements have derivatives as components of the gradient. In 2D, the gradient and curl of a scalar are clearly orthogonal, given by the expressions,

∇
φ

=

(

∂
φ

∂
x
,

∂
φ

∂
y
)

T
,

∇
×
φ

=

(

∂
φ

∂
y
,

−

∂
φ

∂
x
)

T
.
{\displaystyle {\begin{aligned}\nabla \varphi &=\left({\frac {\partial \varphi }{\partial x}},\,{\frac {\partial \varphi }{\partial y}}\right)^{\mathsf {T}},\\[5pt]\nabla \times \varphi &=\left({\frac {\partial \varphi }{\partial y}},\,-{\frac {\partial \varphi }{\partial x}}\right)^{\mathsf {T}}.\end{aligned}}}

Adopting continuous plate-bending elements, interchanging the derivative degrees-of-freedom and changing the sign of the appropriate one gives many families of stream function elements.

Taking the curl of the scalar stream function elements gives divergence-free velocity elements. The requirement that the stream function elements be continuous assures that the normal component of the velocity is continuous across element interfaces, all that is necessary for vanishing divergence on these interfaces.

Boundary conditions are simple to apply. The stream function is constant on no-flow surfaces, with no-slip velocity conditions on surfaces.
Stream function differences across open channels determine the flow. No boundary conditions are necessary on open boundaries, though consistent values may be used with some problems. These are all Dirichlet conditions.

The algebraic equations to be solved are simple to set up, but of course are [non-linear](#Nonlinearity), requiring iteration of the linearized equations.

Similar considerations apply to three-dimensions, but extension from 2D is not immediate because of the vector nature of the potential, and there exists no simple relation between the gradient and the curl as was the case in 2D.

### Pressure recovery

Recovering pressure from the velocity field is easy. The discrete weak equation for the pressure gradient is,

(

g

i
,
∇
p
)
=
−

(

g

i
,

(

u
⋅
∇
)

u

j

)
−
ν

(

∇

g

i
:
∇

u

j
)
+

(

g

i
,

f

I
)
{\displaystyle (\mathbf {g} \_{i},\nabla p)=-{\bigl (}\mathbf {g} \_{i},\left(\mathbf {u} \cdot \nabla \right)\mathbf {u} \_{j}{\bigr )}-\nu \left(\nabla \mathbf {g} \_{i}:\nabla \mathbf {u} \_{j}\right)+\left(\mathbf {g} \_{i},\mathbf {f} ^{I}\right)}

where the test/weight functions are irrotational. Any conforming scalar finite element may be used. However, the pressure gradient field may also be of interest. In this case, one can use scalar Hermite elements for the pressure. For the test/weight functions

g

i
{\textstyle \mathbf {g} \_{i}}
 one would choose the irrotational vector elements obtained from the gradient of the pressure element.

## Non-inertial frame of reference

The rotating frame of reference introduces some interesting pseudo-forces into the equations through the [material derivative](https://en.wikipedia.org/wiki/Material_derivative "Material derivative") term. Consider a stationary [inertial frame of reference](https://en.wikipedia.org/wiki/Inertial_frame_of_reference "Inertial frame of reference")

K
{\textstyle K}
 , and a [non-inertial frame of reference](https://en.wikipedia.org/wiki/Non-inertial_frame_of_reference "Non-inertial frame of reference")

K
′
{\textstyle K'}
, which is translating with velocity

U
(
t
)
{\textstyle \mathbf {U} (t)}
 and rotating with angular velocity

Ω
(
t
)
{\textstyle \Omega (t)}
 with respect to the stationary frame. The Navier–Stokes equation observed from the non-inertial frame then becomes

**Navier–Stokes momentum equation in non-inertial frame**

ρ

(

∂

u

∂
t
+
(

u
⋅
∇
)

u
)
=

−
∇
p
+
∇
⋅

(

μ

[

∇

u
+
(
∇

u

)

T
−

2
3
(
∇
⋅

u
)

I
]
)
+
∇
[
ζ
(
∇
⋅

u
)
]
+
ρ

f

−
ρ

[

2

Ω
×

u
+

Ω
×
(

Ω
×

x
)
+

d

U

d
t
+

d

Ω

d
t
×

x
]
{\displaystyle {\begin{aligned}\rho \left({\frac {\partial \mathbf {u} }{\partial t}}+(\mathbf {u} \cdot \nabla )\mathbf {u} \right)=&-\nabla p+\nabla \cdot \left(\mu \left[\nabla \mathbf {u} +(\nabla \mathbf {u} )^{\mathsf {T}}-{\tfrac {2}{3}}(\nabla \cdot \mathbf {u} )\mathbf {I} \right]\right)+\nabla [\zeta (\nabla \cdot \mathbf {u} )]+\rho \mathbf {f} \\&-\rho \left[2\mathbf {\Omega } \times \mathbf {u} +\mathbf {\Omega } \times (\mathbf {\Omega } \times \mathbf {x} )+{\frac {\mathrm {d} \mathbf {U} }{\mathrm {d} t}}+{\frac {\mathrm {d} \mathbf {\Omega } }{\mathrm {d} t}}\times \mathbf {x} \right]\end{aligned}}}

Here

x
{\textstyle \mathbf {x} }
 and

u
{\textstyle \mathbf {u} }
 are measured in the non-inertial frame. The first term in the parenthesis represents [Coriolis acceleration](https://en.wikipedia.org/wiki/Coriolis_acceleration "Coriolis acceleration"), the second term is due to [centrifugal acceleration](https://en.wikipedia.org/wiki/Centrifugal_force "Centrifugal force"), the third is due to the linear acceleration of

K
′
{\textstyle K'}
 with respect to

K
{\textstyle K}
 and the fourth term is due to the angular acceleration of

K
′
{\textstyle K'}
 with respect to

K
{\textstyle K}
.

## Other equations

The Navier–Stokes equations are strictly a statement of the balance of momentum. To fully describe fluid flow, more information is needed, how much depending on the assumptions made. This additional information may include boundary data ([no-slip](https://en.wikipedia.org/wiki/No-slip_condition "No-slip condition"), [capillary surface](https://en.wikipedia.org/wiki/Capillary_surface "Capillary surface"), etc.), conservation of mass, [balance of energy](https://en.wikipedia.org/wiki/First_law_of_thermodynamics_(fluid_mechanics) "First law of thermodynamics (fluid mechanics)"), and/or an [equation of state](https://en.wikipedia.org/wiki/Equation_of_state "Equation of state").

### Continuity equation for incompressible fluid

Regardless of the flow assumptions, a statement of the [conservation of mass](https://en.wikipedia.org/wiki/Conservation_of_mass "Conservation of mass") is generally necessary. This is achieved through the mass [continuity equation](https://en.wikipedia.org/wiki/Continuity_equation "Continuity equation"), as discussed above in the "General continuum equations" within this article, as follows:

D
m

D
t

=

∭

V

(

D
ρ

D
t
+
ρ
(
∇
⋅

u
)
)
d
V

D
ρ

D
t
+
ρ
(
∇
⋅

u
)

=

∂
ρ

∂
t
+
(

∇
ρ
)
⋅

u
+

ρ
(
∇
⋅

u
)
=

∂
ρ

∂
t
+
∇
⋅
(

ρ

u
)
=
0
{\displaystyle {\begin{aligned}{\frac {\mathbf {D} m}{\mathbf {Dt} }}&={\iiint \limits \_{V}}\left({{\frac {\mathbf {D} \rho }{\mathbf {Dt} }}+\rho (\nabla \cdot \mathbf {u} )}\right)dV\\{\frac {\mathbf {D} \rho }{\mathbf {Dt} }}+\rho (\nabla \cdot {\mathbf {u} })&={\frac {\partial \rho }{\partial t}}+({\nabla \rho })\cdot {\mathbf {u} }+{\rho }(\nabla \cdot \mathbf {u} )={\frac {\partial \rho }{\partial t}}+\nabla \cdot ({\rho \mathbf {u} })=0\end{aligned}}}
A fluid media for which the [density](https://en.wikipedia.org/wiki/Density "Density")

ρ
{\displaystyle \rho }
 is constant is called [*incompressible*](https://en.wikipedia.org/wiki/Incompressible_flow "Incompressible flow"). Therefore, the rate of change of

ρ
{\displaystyle \rho }
 with respect to time

∂
ρ

∂
t
{\textstyle {\frac {\partial \rho }{\partial t}}}
 and the [gradient](https://en.wikipedia.org/wiki/Gradient "Gradient") of density

∇
ρ
{\textstyle \nabla \rho }
 are equal to zero. In this case the general equation of continuity,

∂
ρ

∂
t
+
∇
⋅
(

ρ

u
)
=
0
{\textstyle {\frac {\partial \rho }{\partial t}}+\nabla \cdot ({\rho \mathbf {u} })=0}
, reduces to:

ρ
(
∇

⋅

u
)
=
0
{\displaystyle \rho (\nabla {\cdot }{\mathbf {u} })=0}
 Furthermore, assuming that

ρ
≠
0
{\displaystyle \rho \neq 0}
 means that the right-hand side of the equation (zero) is divisible by [density](https://en.wikipedia.org/wiki/Density "Density")

ρ
{\displaystyle \rho }
. Therefore, the continuity equation for an [incompressible fluid](https://en.wikipedia.org/wiki/Incompressible_flow "Incompressible flow") reduces further to:

(
∇

⋅

u
)
=
0
{\displaystyle (\nabla {\cdot {\mathbf {u} }})=0}
This relationship,

(
∇

⋅

u
)
=
0
{\textstyle (\nabla {\cdot {\mathbf {u} }})=0}
, identifies that the [divergence](https://en.wikipedia.org/wiki/Divergence "Divergence") of the flow velocity [vector](https://en.wikipedia.org/wiki/Vector_field "Vector field")

u
{\displaystyle \mathbf {u} }
 is equal to zero, which means that for an [incompressible fluid](https://en.wikipedia.org/wiki/Incompressible_flow "Incompressible flow") the [flow velocity field](https://en.wikipedia.org/wiki/Flow_velocity "Flow velocity") is a [solenoidal vector field](https://en.wikipedia.org/wiki/Solenoidal_vector_field "Solenoidal vector field") or a [divergence-free vector field](https://en.wikipedia.org/wiki/Divergence-free "Divergence-free"). Note that this relationship can be expanded upon due to its uniqueness with the [vector Laplace operator](https://en.wikipedia.org/wiki/Vector_Laplace_operator "Vector Laplace operator")

∇

2

u
=
∇
(
∇
⋅

u
)
−
∇
×
(
∇
×

u
)
{\displaystyle \nabla ^{2}\mathbf {u} =\nabla (\nabla \cdot \mathbf {u} )-\nabla \times (\nabla \times \mathbf {u} )}
, and [vorticity](https://en.wikipedia.org/wiki/Vorticity "Vorticity")

ω
=
∇
×

u
{\displaystyle {\boldsymbol {\omega }}=\nabla \times \mathbf {u} }
 which is now expressed like so, for an [incompressible fluid](https://en.wikipedia.org/wiki/Incompressible_flow "Incompressible flow"):

∇

2

u
=
−

(
∇
×
(
∇
×

u
)

)
=
−
(
∇
×

ω
)
{\displaystyle \nabla ^{2}\mathbf {u} =-{\bigl (}\nabla \times (\nabla \times \mathbf {u} ){\bigr )}=-(\nabla \times {\boldsymbol {\omega }})}

## Stream function for incompressible 2D fluid

Taking the [curl](https://en.wikipedia.org/wiki/Curl_(mathematics) "Curl (mathematics)") of the incompressible Navier–Stokes equation results in the elimination of pressure. This is especially easy to see if 2D Cartesian flow is assumed (like in the degenerate 3D case with

u

z
=
0
{\textstyle u\_{z}=0}
 and no dependence of anything on

z
{\textstyle z}
), where the equations reduce to:

ρ

(

∂

u

x

∂
t
+

u

x

∂

u

x

∂
x
+

u

y

∂

u

x

∂
y
)

=
−

∂
p

∂
x
+
μ

(

∂

2

u

x

∂

x

2
+

∂

2

u

x

∂

y

2
)
+
ρ

g

x

ρ

(

∂

u

y

∂
t
+

u

x

∂

u

y

∂
x
+

u

y

∂

u

y

∂
y
)

=
−

∂
p

∂
y
+
μ

(

∂

2

u

y

∂

x

2
+

∂

2

u

y

∂

y

2
)
+
ρ

g

y
.
{\displaystyle {\begin{aligned}\rho \left({\frac {\partial u\_{x}}{\partial t}}+u\_{x}{\frac {\partial u\_{x}}{\partial x}}+u\_{y}{\frac {\partial u\_{x}}{\partial y}}\right)&=-{\frac {\partial p}{\partial x}}+\mu \left({\frac {\partial ^{2}u\_{x}}{\partial x^{2}}}+{\frac {\partial ^{2}u\_{x}}{\partial y^{2}}}\right)+\rho g\_{x}\\\rho \left({\frac {\partial u\_{y}}{\partial t}}+u\_{x}{\frac {\partial u\_{y}}{\partial x}}+u\_{y}{\frac {\partial u\_{y}}{\partial y}}\right)&=-{\frac {\partial p}{\partial y}}+\mu \left({\frac {\partial ^{2}u\_{y}}{\partial x^{2}}}+{\frac {\partial ^{2}u\_{y}}{\partial y^{2}}}\right)+\rho g\_{y}.\end{aligned}}}

Differentiating the first with respect to

y
{\textstyle y}
, the second with respect to

x
{\textstyle x}
 and subtracting the resulting equations will eliminate pressure and any [conservative force](https://en.wikipedia.org/wiki/Conservative_force "Conservative force").
For incompressible flow, defining the [stream function](https://en.wikipedia.org/wiki/Stream_function "Stream function")

ψ
{\textstyle \psi }
 through

u

x
=

∂
ψ

∂
y
;

u

y
=
−

∂
ψ

∂
x
{\displaystyle u\_{x}={\frac {\partial \psi }{\partial y}};\quad u\_{y}=-{\frac {\partial \psi }{\partial x}}}
results in mass continuity being unconditionally satisfied (given the stream function is continuous), and then incompressible Newtonian 2D momentum and mass conservation condense into one equation:

∂

∂
t

(

∇

2
ψ
)
+

∂
ψ

∂
y

∂

∂
x

(

∇

2
ψ
)
−

∂
ψ

∂
x

∂

∂
y

(

∇

2
ψ
)
=
ν

∇

4
ψ
{\displaystyle {\frac {\partial }{\partial t}}\left(\nabla ^{2}\psi \right)+{\frac {\partial \psi }{\partial y}}{\frac {\partial }{\partial x}}\left(\nabla ^{2}\psi \right)-{\frac {\partial \psi }{\partial x}}{\frac {\partial }{\partial y}}\left(\nabla ^{2}\psi \right)=\nu \nabla ^{4}\psi }

where

∇

4
{\textstyle \nabla ^{4}}
 is the 2D [biharmonic operator](https://en.wikipedia.org/wiki/Biharmonic_operator "Biharmonic operator") and

ν
{\textstyle \nu }
 is the [kinematic viscosity](https://en.wikipedia.org/wiki/Kinematic_viscosity "Kinematic viscosity"),

ν
=

μ
ρ
{\textstyle \nu ={\frac {\mu }{\rho }}}
. We can also express this compactly using the [Jacobian determinant](https://en.wikipedia.org/wiki/Jacobian_matrix_and_determinant "Jacobian matrix and determinant"):

∂

∂
t

(

∇

2
ψ
)
+

∂

(

ψ
,

∇

2
ψ
)

∂
(
y
,
x
)
=
ν

∇

4
ψ
.
{\displaystyle {\frac {\partial }{\partial t}}\left(\nabla ^{2}\psi \right)+{\frac {\partial \left(\psi ,\nabla ^{2}\psi \right)}{\partial (y,x)}}=\nu \nabla ^{4}\psi .}

This single equation together with appropriate boundary conditions describes 2D fluid flow, taking only kinematic viscosity as a parameter. Note that the equation for [creeping flow](https://en.wikipedia.org/wiki/Creeping_flow "Creeping flow") results when the left side is assumed zero.

In [axisymmetric](https://en.wikipedia.org/wiki/Axisymmetric "Axisymmetric") flow another stream function formulation, called the [Stokes stream function](https://en.wikipedia.org/wiki/Stokes_stream_function "Stokes stream function"), can be used to describe the velocity components of an incompressible flow with one [scalar](https://en.wikipedia.org/wiki/Scalar_(mathematics) "Scalar (mathematics)") function.

The incompressible Navier–Stokes equation is a [differential algebraic equation](https://en.wikipedia.org/wiki/Differential_algebraic_equation "Differential algebraic equation"), having the inconvenient feature that there is no explicit mechanism for advancing the pressure in time. Consequently, much effort has been expended to eliminate the pressure from all or part of the computational process. The stream function formulation eliminates the pressure but only in two dimensions and at the expense of introducing higher derivatives and elimination of the velocity, which is the primary variable of interest.

## Properties

### Nonlinearity

The Navier–Stokes equations are [nonlinear](https://en.wikipedia.org/wiki/Nonlinearity "Nonlinearity") [partial differential equations](https://en.wikipedia.org/wiki/Partial_differential_equations "Partial differential equations") in the general case and so remain in almost every real situation. In some cases, such as one-dimensional flow and [Stokes flow](https://en.wikipedia.org/wiki/Stokes_flow "Stokes flow") (or creeping flow), the equations can be simplified to linear equations. The nonlinearity makes most problems difficult or impossible to solve and is the main contributor to the [turbulence](https://en.wikipedia.org/wiki/Turbulence "Turbulence") that the equations model.

The nonlinearity is due to [convective](https://en.wikipedia.org/wiki/Convective "Convective") acceleration, which is an acceleration associated with the change in velocity over position. Hence, any convective flow, whether turbulent or not, will involve nonlinearity. An example of convective but [laminar](https://en.wikipedia.org/wiki/Laminar_flow "Laminar flow") (nonturbulent) flow would be the passage of a viscous fluid (for example, oil) through a small converging [nozzle](https://en.wikipedia.org/wiki/Nozzle "Nozzle"). Such flows, whether exactly solvable or not, can often be thoroughly studied and understood.

### Turbulence

[Turbulence](https://en.wikipedia.org/wiki/Turbulence "Turbulence") is the time-dependent [chaotic](https://en.wikipedia.org/wiki/Chaos_theory "Chaos theory") behaviour seen in many fluid flows. It is generally believed that it is due to the [inertia](https://en.wikipedia.org/wiki/Inertia "Inertia") of the fluid as a whole: the culmination of time-dependent and convective acceleration; hence flows where inertial effects are small tend to be laminar (the [Reynolds number](https://en.wikipedia.org/wiki/Reynolds_number "Reynolds number") quantifies how much the flow is affected by inertia). It is believed, though not known with certainty, that the Navier–Stokes equations describe turbulence properly.

The numerical solution of the Navier–Stokes equations for turbulent flow is extremely difficult, and due to the significantly different mixing-length scales that are involved in turbulent flow, the stable solution of this requires such a fine mesh resolution that the computational time becomes significantly infeasible for calculation or [direct numerical simulation](https://en.wikipedia.org/wiki/Direct_numerical_simulation "Direct numerical simulation"). Attempts to solve turbulent flow using a laminar solver typically result in a time-unsteady solution, which fails to converge appropriately. To counter this, time-averaged equations such as the [Reynolds-averaged Navier–Stokes equations](https://en.wikipedia.org/wiki/Reynolds-averaged_Navier%E2%80%93Stokes_equations "Reynolds-averaged Navier–Stokes equations") (RANS), supplemented with turbulence models, are used in practical [computational fluid dynamics](https://en.wikipedia.org/wiki/Computational_fluid_dynamics "Computational fluid dynamics") (CFD) applications when modeling turbulent flows. Some models include the [Spalart–Allmaras](https://en.wikipedia.org/wiki/Spalart%E2%80%93Allmaras_turbulence_model "Spalart–Allmaras turbulence model"), [k–ω](https://en.wikipedia.org/wiki/K-omega_turbulence_model "K-omega turbulence model"), [k–ε](https://en.wikipedia.org/wiki/Turbulence_kinetic_energy "Turbulence kinetic energy"), and [SST](https://en.wikipedia.org/w/index.php?title=SST_(Menter%27s_Shear_Stress_Transport)&action=edit&redlink=1 "SST (Menter's Shear Stress Transport) (page does not exist)") models, which add a variety of additional equations to bring closure to the RANS equations. [Large eddy simulation](https://en.wikipedia.org/wiki/Large_eddy_simulation "Large eddy simulation") (LES) can also be used to solve these equations numerically. This approach is computationally more expensive—in time and in computer memory—than RANS, but produces better results because it explicitly resolves the larger turbulent scales.

### Applicability

Together with supplemental equations (for example, conservation of mass) and well-formulated boundary conditions, the Navier–Stokes equations seem to model fluid motion accurately; even turbulent flows seem (on average) to agree with real world observations.

The Navier–Stokes equations assume that the fluid being studied is a [continuum](https://en.wikipedia.org/wiki/Continuum_mechanics "Continuum mechanics") (it is infinitely divisible and not composed of particles such as atoms or molecules), and is not moving at [relativistic velocities](https://en.wikipedia.org/wiki/Relativistic_velocity "Relativistic velocity"). At very small scales or under extreme conditions, real fluids made out of discrete molecules will produce results different from the continuous fluids modeled by the Navier–Stokes equations. For example, [capillarity](https://en.wikipedia.org/wiki/Capillarity "Capillarity") of internal layers in fluids appears for flow with high gradients. For large [Knudsen number](https://en.wikipedia.org/wiki/Knudsen_number "Knudsen number") of the problem, the [Boltzmann equation](https://en.wikipedia.org/wiki/Boltzmann_equation "Boltzmann equation") may be a suitable replacement. Failing that, one may have to resort to [molecular dynamics](https://en.wikipedia.org/wiki/Molecular_dynamics "Molecular dynamics") or various hybrid methods.

Another limitation is simply the complicated nature of the equations. Time-tested formulations exist for common fluid families, but the application of the Navier–Stokes equations to less common families tends to result in very complicated formulations and often to open research problems. For this reason, these equations are usually written for [Newtonian fluids](https://en.wikipedia.org/wiki/Newtonian_fluid "Newtonian fluid") where the viscosity model is [linear](https://en.wikipedia.org/wiki/Linear "Linear"); truly general models for the flow of other kinds of fluids (such as blood) do not exist.

## Application to specific problems

The Navier–Stokes equations, even when written explicitly for specific fluids, are rather generic in nature and their proper application to specific problems can be very diverse. This is partly because there is an enormous variety of problems that may be modeled, ranging from as simple as the distribution of static pressure to as complicated as [multiphase flow](https://en.wikipedia.org/wiki/Multiphase_flow "Multiphase flow") driven by [surface tension](https://en.wikipedia.org/wiki/Surface_tension "Surface tension").

Generally, application to specific problems begins with some flow assumptions and initial/boundary condition formulation, this may be followed by [scale analysis](https://en.wikipedia.org/wiki/Scale_analysis_(mathematics) "Scale analysis (mathematics)") to further simplify the problem.

### Parallel flow

Assume steady, parallel, one-dimensional, non-convective pressure-driven flow between parallel plates, the resulting scaled (dimensionless) [boundary value problem](https://en.wikipedia.org/wiki/Boundary_value_problem "Boundary value problem") is:

d

2
u

d

y

2
=
−
1
;

u
(
0
)
=
u
(
1
)
=
0.
{\displaystyle {\frac {\mathrm {d} ^{2}u}{\mathrm {d} y^{2}}}=-1;\quad u(0)=u(1)=0.}

The boundary condition is the [no slip condition](https://en.wikipedia.org/wiki/No_slip_condition "No slip condition"). This problem is easily solved for the flow field:

u
(
y
)
=

y
−

y

2
2
.
{\displaystyle u(y)={\frac {y-y^{2}}{2}}.}

From this point onward, more quantities of interest can be easily obtained, such as viscous drag force or net flow rate.

### Radial flow

Difficulties may arise when the problem becomes slightly more complicated. A seemingly modest twist on the parallel flow above would be the *radial* flow between parallel plates; this involves convection and thus non-linearity. The velocity field may be represented by a function

f
(
z
)
{\displaystyle f(z)}
 that must satisfy:

d

2
f

d

z

2
+
R

f

2
=
−
1
;

f
(
−
1
)
=
f
(
1
)
=
0.
{\displaystyle {\frac {\mathrm {d} ^{2}f}{\mathrm {d} z^{2}}}+Rf^{2}=-1;\quad f(-1)=f(1)=0.}

This [ordinary differential equation](https://en.wikipedia.org/wiki/Ordinary_differential_equation "Ordinary differential equation") is what is obtained when the Navier–Stokes equations are written and the flow assumptions applied (additionally, the pressure gradient is solved for). The [nonlinear](https://en.wikipedia.org/wiki/Nonlinearity "Nonlinearity") term makes this a very difficult problem to solve analytically (a lengthy [implicit](https://en.wikipedia.org/wiki/Implicit_function "Implicit function") solution may be found which involves [elliptic integrals](https://en.wikipedia.org/wiki/Elliptic_integral "Elliptic integral") and [roots of cubic polynomials](https://en.wikipedia.org/wiki/Cubic_formula "Cubic formula")). Issues with the actual existence of solutions arise for

R
>
1.41
{\textstyle R>1.41}
 (approximately; this is not [√2](https://en.wikipedia.org/wiki/Square_root_of_2 "Square root of 2")), the parameter

R
{\textstyle R}
 being the Reynolds number with appropriately chosen scales. This is an example of flow assumptions losing their applicability, and an example of the difficulty in "high" Reynolds number flows.

### Convection

A type of natural convection that can be described by the Navier–Stokes equation is the [Rayleigh–Bénard convection](https://en.wikipedia.org/wiki/Rayleigh%E2%80%93B%C3%A9nard_convection "Rayleigh–Bénard convection"). It is one of the most commonly studied convection phenomena because of its analytical and experimental accessibility.

## Exact solutions of the Navier–Stokes equations

Some exact solutions to the Navier–Stokes equations exist. Examples of degenerate cases—with the non-linear terms in the Navier–Stokes equations equal to zero—are [Poiseuille flow](https://en.wikipedia.org/wiki/Hagen-Poiseuille_equation "Hagen-Poiseuille equation"), [Couette flow](https://en.wikipedia.org/wiki/Couette_flow "Couette flow") and the oscillatory [Stokes boundary layer](https://en.wikipedia.org/wiki/Stokes_boundary_layer "Stokes boundary layer"). But also, more interesting examples, solutions to the full non-linear equations, exist, such as [Jeffery–Hamel flow](https://en.wikipedia.org/wiki/Jeffery%E2%80%93Hamel_flow "Jeffery–Hamel flow"), [Von Kármán swirling flow](https://en.wikipedia.org/wiki/Von_K%C3%A1rm%C3%A1n_swirling_flow "Von Kármán swirling flow"), [stagnation point flow](https://en.wikipedia.org/wiki/Stagnation_point_flow "Stagnation point flow"), [Landau–Squire jet](https://en.wikipedia.org/wiki/Landau%E2%80%93Squire_jet "Landau–Squire jet"), and [Taylor–Green vortex](https://en.wikipedia.org/wiki/Taylor%E2%80%93Green_vortex "Taylor–Green vortex"). Time-dependent [self-similar](https://en.wikipedia.org/wiki/Self-similar_solution "Self-similar solution") solutions of the three-dimensional non-compressible Navier–Stokes equations in Cartesian coordinate can be given with the help of the [Kummer's functions](https://en.wikipedia.org/wiki/Kummer%27s_function "Kummer's function") with quadratic arguments. For the compressible Navier–Stokes equations the time-dependent self-similar solutions are however the [Whittaker functions](https://en.wikipedia.org/wiki/Whittaker_function "Whittaker function") again with quadratic arguments when the [polytropic](https://en.wikipedia.org/wiki/Polytrope "Polytrope") [equation of state](https://en.wikipedia.org/wiki/Equation_of_state "Equation of state") is used as a closing condition. Note that the existence of these exact solutions does not imply they are stable: turbulence may develop at higher Reynolds numbers.

Under additional assumptions, the component parts can be separated.

A two-dimensional example

For example, in the case of an unbounded planar domain with **two-dimensional** — incompressible and stationary — flow in [polar coordinates](https://en.wikipedia.org/wiki/Polar_coordinates "Polar coordinates") (*r*,*φ*), the velocity components (*ur*,*uφ*) and pressure p are:

u

r

=

A
r
,

u

φ

=
B

(

1
r
−

r

A
ν
+
1
)
,

p

=
−

A

2
+

B

2

2

r

2
−

2

B

2
ν

r

A
ν
A
+

B

2

r

(

2
A
ν
+
2
)

2
A
ν
+
2
{\displaystyle {\begin{aligned}u\_{r}&={\frac {A}{r}},\\u\_{\varphi }&=B\left({\frac {1}{r}}-r^{{\frac {A}{\nu }}+1}\right),\\p&=-{\frac {A^{2}+B^{2}}{2r^{2}}}-{\frac {2B^{2}\nu r^{\frac {A}{\nu }}}{A}}+{\frac {B^{2}r^{\left({\frac {2A}{\nu }}+2\right)}}{{\frac {2A}{\nu }}+2}}\end{aligned}}}

where A and B are arbitrary constants. This solution is valid in the domain *r* ≥ 1 and for *A* < −2*ν*.

In Cartesian coordinates, when the viscosity is zero (*ν* = 0), this is:

v
(
x
,
y
)

=

1

x

2
+

y

2

(

A
x
+
B
y

A
y
−
B
x
)
,

p
(
x
,
y
)

=
−

A

2
+

B

2

2

(

x

2
+

y

2
)
{\displaystyle {\begin{aligned}\mathbf {v} (x,y)&={\frac {1}{x^{2}+y^{2}}}{\begin{pmatrix}Ax+By\\Ay-Bx\end{pmatrix}},\\p(x,y)&=-{\frac {A^{2}+B^{2}}{2\left(x^{2}+y^{2}\right)}}\end{aligned}}}

A three-dimensional example

For example, in the case of an unbounded Euclidean domain with **three-dimensional** — incompressible, stationary and with zero viscosity (*ν* = 0) — radial flow in [Cartesian coordinates](https://en.wikipedia.org/wiki/Cartesian_coordinates "Cartesian coordinates") (*x*,*y*,*z*), the velocity vector **v** and pressure p are:[*[citation needed](https://en.wikipedia.org/wiki/Wikipedia:Citation_needed "Wikipedia:Citation needed")*]

v
(
x
,
y
,
z
)

=

A

x

2
+

y

2
+

z

2

(

x

y

z
)
,

p
(
x
,
y
,
z
)

=
−

A

2

2

(

x

2
+

y

2
+

z

2
)
.
{\displaystyle {\begin{aligned}\mathbf {v} (x,y,z)&={\frac {A}{x^{2}+y^{2}+z^{2}}}{\begin{pmatrix}x\\y\\z\end{pmatrix}},\\p(x,y,z)&=-{\frac {A^{2}}{2\left(x^{2}+y^{2}+z^{2}\right)}}.\end{aligned}}}

There is a singularity at *x* = *y* = *z* = 0.

### A three-dimensional steady-state vortex solution

A steady-state example with no singularities comes from considering the flow along the lines of a [Hopf fibration](https://en.wikipedia.org/wiki/Hopf_fibration "Hopf fibration"). Let

r
{\textstyle r}
 be a constant radius of the inner coil. One set of solutions is given by:

ρ
(
x
,
y
,
z
)

=

3
B

r

2
+

x

2
+

y

2
+

z

2

p
(
x
,
y
,
z
)

=

−

A

2
B

(

r

2
+

x

2
+

y

2
+

z

2
)

3

u
(
x
,
y
,
z
)

=

A

(

r

2
+

x

2
+

y

2
+

z

2
)

2

(

2
(
−
r
y
+
x
z
)

2
(
r
x
+
y
z
)

r

2
−

x

2
−

y

2
+

z

2
)

g

=
0

μ

=
0
{\displaystyle {\begin{aligned}\rho (x,y,z)&={\frac {3B}{r^{2}+x^{2}+y^{2}+z^{2}}}\\p(x,y,z)&={\frac {-A^{2}B}{\left(r^{2}+x^{2}+y^{2}+z^{2}\right)^{3}}}\\\mathbf {u} (x,y,z)&={\frac {A}{\left(r^{2}+x^{2}+y^{2}+z^{2}\right)^{2}}}{\begin{pmatrix}2(-ry+xz)\\2(rx+yz)\\r^{2}-x^{2}-y^{2}+z^{2}\end{pmatrix}}\\g&=0\\\mu &=0\end{aligned}}}

for arbitrary constants

A
{\textstyle A}
 and

B
{\textstyle B}
. This is a solution in a non-viscous gas (compressible fluid) whose density, velocities and pressure goes to zero far from the origin. (Note this is not a solution to the Clay Millennium problem because that refers to incompressible fluids where

ρ
{\textstyle \rho }
 is a constant, and neither does it deal with the uniqueness of the Navier–Stokes equations with respect to any [turbulence](https://en.wikipedia.org/wiki/Turbulence "Turbulence") properties.) It is also worth pointing out that the components of the velocity vector are exactly those from the [Pythagorean quadruple](https://en.wikipedia.org/wiki/Pythagorean_quadruple "Pythagorean quadruple") parametrization. Other choices of density and pressure are possible with the same velocity field:

Other choices of density and pressure

Another choice of pressure and density with the same velocity vector above is one where the pressure and density fall to zero at the origin and are highest in the central loop at *z* = 0, *x*2 + *y*2 = *r*2:

ρ
(
x
,
y
,
z
)

=

20
B

(

x

2
+

y

2
)

(

r

2
+

x

2
+

y

2
+

z

2
)

3

p
(
x
,
y
,
z
)

=

−

A

2
B

(

r

2
+

x

2
+

y

2
+

z

2
)

4
+

−
4

A

2
B

(

x

2
+

y

2
)

(

r

2
+

x

2
+

y

2
+

z

2
)

5
.
{\displaystyle {\begin{aligned}\rho (x,y,z)&={\frac {20B\left(x^{2}+y^{2}\right)}{\left(r^{2}+x^{2}+y^{2}+z^{2}\right)^{3}}}\\p(x,y,z)&={\frac {-A^{2}B}{\left(r^{2}+x^{2}+y^{2}+z^{2}\right)^{4}}}+{\frac {-4A^{2}B\left(x^{2}+y^{2}\right)}{\left(r^{2}+x^{2}+y^{2}+z^{2}\right)^{5}}}.\end{aligned}}}

In fact in general there are simple solutions for any polynomial function f where the density is:

ρ
(
x
,
y
,
z
)
=

1

r

2
+

x

2
+

y

2
+

z

2
f

(

x

2
+

y

2

(

r

2
+

x

2
+

y

2
+

z

2
)

2
)
.
{\displaystyle \rho (x,y,z)={\frac {1}{r^{2}+x^{2}+y^{2}+z^{2}}}f\left({\frac {x^{2}+y^{2}}{\left(r^{2}+x^{2}+y^{2}+z^{2}\right)^{2}}}\right).}

### Viscous three-dimensional periodic solutions

Two examples of periodic fully-three-dimensional viscous solutions are described in.
These solutions are defined on a three-dimensional [torus](https://en.wikipedia.org/wiki/Torus "Torus")

T

3
=

R

3

/

L

Z

3
{\displaystyle \mathbb {T} ^{3}=\mathbb {R} ^{3}/{L\mathbb {Z} ^{3}}}
 and are characterized by positive and negative [helicity](https://en.wikipedia.org/wiki/Hydrodynamical_helicity "Hydrodynamical helicity") respectively.
The solution with positive helicity is given by:

u

x

=

4

2

3

3

U

0

[

sin
⁡

(

k
x
−

π
3
)
cos
⁡

(

k
y
+

π
3
)
sin
⁡

(

k
z
+

π
2
)
−
cos
⁡

(

k
z
−

π
3
)
sin
⁡

(

k
x
+

π
3
)
sin
⁡

(

k
y
+

π
2
)

]

e

−
3
ν

k

2
t

u

y

=

4

2

3

3

U

0

[

sin
⁡

(

k
y
−

π
3
)
cos
⁡

(

k
z
+

π
3
)
sin
⁡

(

k
x
+

π
2
)
−
cos
⁡

(

k
x
−

π
3
)
sin
⁡

(

k
y
+

π
3
)
sin
⁡

(

k
z
+

π
2
)

]

e

−
3
ν

k

2
t

u

z

=

4

2

3

3

U

0

[

sin
⁡

(

k
z
−

π
3
)
cos
⁡

(

k
x
+

π
3
)
sin
⁡

(

k
y
+

π
2
)
−
cos
⁡

(

k
y
−

π
3
)
sin
⁡

(

k
z
+

π
3
)
sin
⁡

(

k
x
+

π
2
)

]

e

−
3
ν

k

2
t
{\displaystyle {\begin{aligned}u\_{x}&={\frac {4{\sqrt {2}}}{3{\sqrt {3}}}}\,U\_{0}\left[\,\sin \left(kx-{\frac {\pi }{3}}\right)\cos \left(ky+{\frac {\pi }{3}}\right)\sin \left(kz+{\frac {\pi }{2}}\right)-\cos \left(kz-{\frac {\pi }{3}}\right)\sin \left(kx+{\frac {\pi }{3}}\right)\sin \left(ky+{\frac {\pi }{2}}\right)\,\right]e^{-3\nu k^{2}t}\\u\_{y}&={\frac {4{\sqrt {2}}}{3{\sqrt {3}}}}\,U\_{0}\left[\,\sin \left(ky-{\frac {\pi }{3}}\right)\cos \left(kz+{\frac {\pi }{3}}\right)\sin \left(kx+{\frac {\pi }{2}}\right)-\cos \left(kx-{\frac {\pi }{3}}\right)\sin \left(ky+{\frac {\pi }{3}}\right)\sin \left(kz+{\frac {\pi }{2}}\right)\,\right]e^{-3\nu k^{2}t}\\u\_{z}&={\frac {4{\sqrt {2}}}{3{\sqrt {3}}}}\,U\_{0}\left[\,\sin \left(kz-{\frac {\pi }{3}}\right)\cos \left(kx+{\frac {\pi }{3}}\right)\sin \left(ky+{\frac {\pi }{2}}\right)-\cos \left(ky-{\frac {\pi }{3}}\right)\sin \left(kz+{\frac {\pi }{3}}\right)\sin \left(kx+{\frac {\pi }{2}}\right)\,\right]e^{-3\nu k^{2}t}\end{aligned}}}
where

k
=
2
π

/
L
{\displaystyle k=2\pi /L}
 is the wave number and the velocity components are normalized so that the average kinetic energy per unit of mass is

U

0

2

/
2
{\displaystyle U\_{0}^{2}/2}
 at

t
=
0
{\displaystyle t=0}
.
The pressure field is obtained from the velocity field as

p
=

p

0
−

ρ

0
‖

u

‖

2

/
2
{\displaystyle p=p\_{0}-\rho \_{0}\|{\boldsymbol {u}}\|^{2}/2}
 (where

p

0
{\displaystyle p\_{0}}
 and

ρ

0
{\displaystyle \rho \_{0}}
 are reference values for the pressure and density fields respectively).
Since both the solutions belong to the class of [Beltrami flow](https://en.wikipedia.org/wiki/Beltrami_flow "Beltrami flow"), the vorticity field is parallel to the velocity and, for the case with positive helicity, is given by

ω
=

3

k

u
{\displaystyle \omega ={\sqrt {3}}\,k\,{\boldsymbol {u}}}
.
These solutions can be regarded as a generalization in three dimensions of the classic two-dimensional [Taylor–Green vortex](https://en.wikipedia.org/wiki/Taylor%E2%80%93Green_vortex "Taylor–Green vortex").

### OpenAI announcement

On 8 September 2026, [artificial intelligence](https://en.wikipedia.org/wiki/Artificial_intelligence "Artificial intelligence") company [OpenAI](https://en.wikipedia.org/wiki/OpenAI "OpenAI") announced it had solved the [Millennium Prize Problem](https://en.wikipedia.org/wiki/Millennium_Prize_Problems "Millennium Prize Problems") on [the existence and smoothness of the incompressible Navier–Stokes](https://en.wikipedia.org/wiki/Navier%E2%80%93Stokes_existence_and_smoothness "Navier–Stokes existence and smoothness") equations in [three-dimensional Euclidean space](https://en.wikipedia.org/wiki/Three-dimensional_space "Three-dimensional space"). OpenAI stated that the solution to the problem, a counterexample that refers to statements C and D of the problem statement, was developed by its researchers using as many as 10,000 coordinated [agents](https://en.wikipedia.org/wiki/AI_agent "AI agent") running an internal [frontier model](https://en.wikipedia.org/wiki/Frontier_model "Frontier model"), along with a formalization in the [Lean](https://en.wikipedia.org/wiki/Lean_(proof_assistant) "Lean (proof assistant)") proof assistant. The claim has not been verified by external mathematicians or the Clay Mathematics Institute, while OpenAI stated it would not claim the Millennium Prize. The announcement was accompanied by a [priority dispute](https://en.wikipedia.org/wiki/Scientific_priority "Scientific priority") with [Levent Alpöge](https://en.wikipedia.org/wiki/Levent_Alp%C3%B6ge "Levent Alpöge") (employed at rival AI company [Anthropic](https://en.wikipedia.org/wiki/Anthropic "Anthropic")) and [Tristan Buckmaster](https://en.wikipedia.org/wiki/Tristan_Buckmaster "Tristan Buckmaster"), who had derived a set of closely related results on the [Euler equations](https://en.wikipedia.org/wiki/Euler_equations_(fluid_dynamics) "Euler equations (fluid dynamics)"). The method used to generate the claimed solution built upon a method developed by Diego Córdoba and Luis Martínez Zoroa in 2023 to prove blowup phenomena in related fluid equations.

On 6 October a paper published on arxiv found discrepencies between OpenAI's Lean proof and natural language proof

## Wyld diagrams

**Wyld diagrams** are bookkeeping [graphs](https://en.wikipedia.org/wiki/Graph_(discrete_mathematics) "Graph (discrete mathematics)") that correspond to the Navier–Stokes equations via a [perturbation expansion](https://en.wikipedia.org/wiki/Perturbation_theory "Perturbation theory") of the fundamental [continuum mechanics](https://en.wikipedia.org/wiki/Continuum_mechanics "Continuum mechanics"). Similar to the [Feynman diagrams](https://en.wikipedia.org/wiki/Feynman_diagram "Feynman diagram") in [quantum field theory](https://en.wikipedia.org/wiki/Quantum_field_theory "Quantum field theory"), these diagrams are an extension of [Mstislav Keldysh](https://en.wikipedia.org/wiki/Mstislav_Keldysh "Mstislav Keldysh")'s technique for nonequilibrium processes in fluid dynamics.[*[citation needed](https://en.wikipedia.org/wiki/Wikipedia:Citation_needed "Wikipedia:Citation needed")*] In other words, these diagrams assign [graphs](https://en.wikipedia.org/wiki/Graph_theory "Graph theory") to the (often) [turbulent](https://en.wikipedia.org/wiki/Turbulence "Turbulence") phenomena in turbulent fluids by allowing [correlated](https://en.wikipedia.org/wiki/Correlation_function "Correlation function") and interacting fluid particles to obey [stochastic processes](https://en.wikipedia.org/wiki/Stochastic_processes "Stochastic processes") associated to [pseudo-random](https://en.wikipedia.org/wiki/Pseudo-random "Pseudo-random") [functions](https://en.wikipedia.org/wiki/Function_(mathematics) "Function (mathematics)") in [probability distributions](https://en.wikipedia.org/wiki/Probability_distribution "Probability distribution").

## Representations in 3D

Note that the formulas in this section make use of the single-line notation for partial derivatives, where, e.g.

∂

x
u
{\textstyle \partial \_{x}u}
 means the partial derivative of

u
{\textstyle u}
 with respect to

x
{\textstyle x}
, and

∂

y

2

f

θ
{\textstyle \partial \_{y}^{2}f\_{\theta }}
 means the second-order partial derivative of

f

θ
{\textstyle f\_{\theta }}
 with respect to

y
{\textstyle y}
.

A 2022 paper provides a less costly, dynamical and recurrent solution of the Navier-Stokes equation for 3D turbulent fluid flows. On suitably short time scales, the dynamics of turbulence is deterministic.

### Cartesian coordinates

From the general form of the Navier–Stokes, with the velocity vector expanded as

u
=
(

u

x
,

u

y
,

u

z
)
{\textstyle \mathbf {u} =(u\_{x},u\_{y},u\_{z})}
, sometimes respectively named

u
{\textstyle u}
,

v
{\textstyle v}
,

w
{\textstyle w}
, we may write the vector equation explicitly,

x
:
 

ρ

(

∂

t

u

x
+

u

x

∂

x

u

x
+

u

y

∂

y

u

x
+

u

z

∂

z

u

x
)

=
−

∂

x
p
+
μ

(

∂

x

2

u

x
+

∂

y

2

u

x
+

∂

z

2

u

x
)
+

1
3
μ
 

∂

x

(

∂

x

u

x
+

∂

y

u

y
+

∂

z

u

z
)
+
ρ

g

x
{\displaystyle {\begin{aligned}x:\ &\rho \left({\partial \_{t}u\_{x}}+u\_{x}\,{\partial \_{x}u\_{x}}+u\_{y}\,{\partial \_{y}u\_{x}}+u\_{z}\,{\partial \_{z}u\_{x}}\right)\\&\quad =-\partial \_{x}p+\mu \left({\partial \_{x}^{2}u\_{x}}+{\partial \_{y}^{2}u\_{x}}+{\partial \_{z}^{2}u\_{x}}\right)+{\frac {1}{3}}\mu \ \partial \_{x}\left({\partial \_{x}u\_{x}}+{\partial \_{y}u\_{y}}+{\partial \_{z}u\_{z}}\right)+\rho g\_{x}\\\end{aligned}}}

y
:
 

ρ

(

∂

t

u

y
+

u

x

∂

x

u

y
+

u

y

∂

y

u

y
+

u

z

∂

z

u

y
)

=
−

∂

y
p
+
μ

(

∂

x

2

u

y
+

∂

y

2

u

y
+

∂

z

2

u

y
)
+

1
3
μ
 

∂

y

(

∂

x

u

x
+

∂

y

u

y
+

∂

z

u

z
)
+
ρ

g

y
{\displaystyle {\begin{aligned}y:\ &\rho \left({\partial \_{t}u\_{y}}+u\_{x}{\partial \_{x}u\_{y}}+u\_{y}{\partial \_{y}u\_{y}}+u\_{z}{\partial \_{z}u\_{y}}\right)\\&\quad =-{\partial \_{y}p}+\mu \left({\partial \_{x}^{2}u\_{y}}+{\partial \_{y}^{2}u\_{y}}+{\partial \_{z}^{2}u\_{y}}\right)+{\frac {1}{3}}\mu \ \partial \_{y}\left({\partial \_{x}u\_{x}}+{\partial \_{y}u\_{y}}+{\partial \_{z}u\_{z}}\right)+\rho g\_{y}\\\end{aligned}}}

z
:
 

ρ

(

∂

t

u

z
+

u

x

∂

x

u

z
+

u

y

∂

y

u

z
+

u

z

∂

z

u

z
)

=
−

∂

z
p
+
μ

(

∂

x

2

u

z
+

∂

y

2

u

z
+

∂

z

2

u

z
)
+

1
3
μ
 

∂

z

(

∂

x

u

x
+

∂

y

u

y
+

∂

z

u

z
)
+
ρ

g

z
.
{\displaystyle {\begin{aligned}z:\ &\rho \left({\partial \_{t}u\_{z}}+u\_{x}{\partial \_{x}u\_{z}}+u\_{y}{\partial \_{y}u\_{z}}+u\_{z}{\partial \_{z}u\_{z}}\right)\\&\quad =-{\partial \_{z}p}+\mu \left({\partial \_{x}^{2}u\_{z}}+{\partial \_{y}^{2}u\_{z}}+{\partial \_{z}^{2}u\_{z}}\right)+{\frac {1}{3}}\mu \ \partial \_{z}\left({\partial \_{x}u\_{x}}+{\partial \_{y}u\_{y}}+{\partial \_{z}u\_{z}}\right)+\rho g\_{z}.\end{aligned}}}

Note that gravity has been accounted for as a body force, and the values of

g

x
{\textstyle g\_{x}}
,

g

y
{\textstyle g\_{y}}
,

g

z
{\textstyle g\_{z}}
 will depend on the orientation of gravity with respect to the chosen set of coordinates.

The continuity equation reads:

∂

t
ρ
+

∂

x
(
ρ

u

x
)
+

∂

y
(
ρ

u

y
)
+

∂

z
(
ρ

u

z
)
=
0.
{\displaystyle \partial \_{t}\rho +\partial \_{x}(\rho u\_{x})+\partial \_{y}(\rho u\_{y})+\partial \_{z}(\rho u\_{z})=0.}

When the flow is incompressible,

ρ
{\textstyle \rho }
 does not change for any fluid particle, and its [material derivative](https://en.wikipedia.org/wiki/Material_derivative "Material derivative") vanishes:

D
ρ

D
t
=
0
{\textstyle {\frac {\mathrm {D} \rho }{\mathrm {D} t}}=0}
. The continuity equation is reduced to:

∂

x

u

x
+

∂

y

u

y
+

∂

z

u

z
=
0.
{\displaystyle \partial \_{x}u\_{x}+\partial \_{y}u\_{y}+\partial \_{z}u\_{z}=0.}

Thus, for the incompressible version of the Navier–Stokes equation the second part of the viscous terms fall away (see [Incompressible flow](https://en.wikipedia.org/wiki/Incompressible_flow "Incompressible flow")).

This system of four equations comprises the most commonly used and studied form. Though comparatively more compact than other representations, this is still a [nonlinear](https://en.wikipedia.org/wiki/Nonlinearity "Nonlinearity") system of [partial differential equations](https://en.wikipedia.org/wiki/Partial_differential_equations "Partial differential equations") for which solutions are difficult to obtain.

### Cylindrical coordinates

A change of variables on the Cartesian equations will yield the following momentum equations for

r
{\textstyle r}
,

ϕ
{\textstyle \phi }
, and

z
{\textstyle z}

r
:
 

ρ

(

∂

t

u

r
+

u

r

∂

r

u

r
+

u

φ
r

∂

φ

u

r
+

u

z

∂

z

u

r
−

u

φ

2
r
)

=
−

∂

r
p

+
μ

(

1
r

∂

r

(

r

∂

r

u

r
)
+

1

r

2

∂

φ

2

u

r
+

∂

z

2

u

r
−

u

r

r

2
−

2

r

2

∂

φ

u

φ
)

+

1
3
μ

∂

r

(

1
r

∂

r

(

r

u

r
)
+

1
r

∂

φ

u

φ
+

∂

z

u

z
)

+
ρ

g

r
{\displaystyle {\begin{aligned}r:\ &\rho \left({\partial \_{t}u\_{r}}+u\_{r}{\partial \_{r}u\_{r}}+{\frac {u\_{\varphi }}{r}}{\partial \_{\varphi }u\_{r}}+u\_{z}{\partial \_{z}u\_{r}}-{\frac {u\_{\varphi }^{2}}{r}}\right)\\&\quad =-{\partial \_{r}p}\\&\qquad +\mu \left({\frac {1}{r}}\partial \_{r}\left(r{\partial \_{r}u\_{r}}\right)+{\frac {1}{r^{2}}}{\partial \_{\varphi }^{2}u\_{r}}+{\partial \_{z}^{2}u\_{r}}-{\frac {u\_{r}}{r^{2}}}-{\frac {2}{r^{2}}}{\partial \_{\varphi }u\_{\varphi }}\right)\\&\qquad +{\frac {1}{3}}\mu \partial \_{r}\left({\frac {1}{r}}{\partial \_{r}\left(ru\_{r}\right)}+{\frac {1}{r}}{\partial \_{\varphi }u\_{\varphi }}+{\partial \_{z}u\_{z}}\right)\\&\qquad +\rho g\_{r}\\[8px]\end{aligned}}}

φ
:
 

ρ

(

∂

t

u

φ
+

u

r

∂

r

u

φ
+

u

φ
r

∂

φ

u

φ
+

u

z

∂

z

u

φ
+

u

r

u

φ
r
)

=
−

1
r

∂

φ
p

+
μ

(

1
r
 

∂

r

(

r

∂

r

u

φ
)
+

1

r

2

∂

φ

2

u

φ
+

∂

z

2

u

φ
−

u

φ

r

2
+

2

r

2

∂

φ

u

r
)

+

1
3
μ

1
r

∂

φ

(

1
r

∂

r

(

r

u

r
)
+

1
r

∂

φ

u

φ
+

∂

z

u

z
)

+
ρ

g

φ
{\displaystyle {\begin{aligned}\varphi :\ &\rho \left({\partial \_{t}u\_{\varphi }}+u\_{r}{\partial \_{r}u\_{\varphi }}+{\frac {u\_{\varphi }}{r}}{\partial \_{\varphi }u\_{\varphi }}+u\_{z}{\partial \_{z}u\_{\varphi }}+{\frac {u\_{r}u\_{\varphi }}{r}}\right)\\&\quad =-{\frac {1}{r}}{\partial \_{\varphi }p}\\&\qquad +\mu \left({\frac {1}{r}}\ \partial \_{r}\left(r{\partial \_{r}u\_{\varphi }}\right)+{\frac {1}{r^{2}}}{\partial \_{\varphi }^{2}u\_{\varphi }}+{\partial \_{z}^{2}u\_{\varphi }}-{\frac {u\_{\varphi }}{r^{2}}}+{\frac {2}{r^{2}}}{\partial \_{\varphi }u\_{r}}\right)\\&\qquad +{\frac {1}{3}}\mu {\frac {1}{r}}\partial \_{\varphi }\left({\frac {1}{r}}{\partial \_{r}\left(ru\_{r}\right)}+{\frac {1}{r}}{\partial \_{\varphi }u\_{\varphi }}+{\partial \_{z}u\_{z}}\right)\\&\qquad +\rho g\_{\varphi }\\[8px]\end{aligned}}}

z
:
 

ρ

(

∂

t

u

z
+

u

r

∂

r

u

z
+

u

φ
r

∂

φ

u

z
+

u

z

∂

z

u

z
)

=
−

∂

z
p

+
μ

(

1
r

∂

r

(

r

∂

r

u

z
)
+

1

r

2

∂

φ

2

u

z
+

∂

z

2

u

z
)

+

1
3
μ

∂

z

(

1
r

∂

r

(

r

u

r
)
+

1
r

∂

φ

u

φ
+

∂

z

u

z
)

+
ρ

g

z
.
{\displaystyle {\begin{aligned}z:\ &\rho \left({\partial \_{t}u\_{z}}+u\_{r}{\partial \_{r}u\_{z}}+{\frac {u\_{\varphi }}{r}}{\partial \_{\varphi }u\_{z}}+u\_{z}{\partial \_{z}u\_{z}}\right)\\&\quad =-{\partial \_{z}p}\\&\qquad +\mu \left({\frac {1}{r}}\partial \_{r}\left(r{\partial \_{r}u\_{z}}\right)+{\frac {1}{r^{2}}}{\partial \_{\varphi }^{2}u\_{z}}+{\partial \_{z}^{2}u\_{z}}\right)\\&\qquad +{\frac {1}{3}}\mu \partial \_{z}\left({\frac {1}{r}}{\partial \_{r}\left(ru\_{r}\right)}+{\frac {1}{r}}{\partial \_{\varphi }u\_{\varphi }}+{\partial \_{z}u\_{z}}\right)\\&\qquad +\rho g\_{z}.\end{aligned}}}

The gravity components will generally not be constants, however for most applications either the coordinates are chosen so that the gravity components are constant or else it is assumed that gravity is counteracted by a pressure field (for example, flow in horizontal pipe is treated normally without gravity and without a vertical pressure gradient). The continuity equation is:

∂

t
ρ
+

1
r

∂

r

(

ρ
r

u

r
)
+

1
r

∂

φ

(

ρ

u

φ
)
+

∂

z

(

ρ

u

z
)
=
0.
{\displaystyle {\partial \_{t}\rho }+{\frac {1}{r}}\partial \_{r}\left(\rho ru\_{r}\right)+{\frac {1}{r}}{\partial \_{\varphi }\left(\rho u\_{\varphi }\right)}+{\partial \_{z}\left(\rho u\_{z}\right)}=0.}

This cylindrical representation of the incompressible Navier–Stokes equations is the second most commonly seen (the first being Cartesian above). Cylindrical coordinates are chosen to take advantage of symmetry, so that a velocity component can disappear. A very common case is axisymmetric flow with the assumption of no tangential velocity (

u

ϕ
=
0
{\textstyle u\_{\phi }=0}
), and the remaining quantities are independent of

ϕ
{\textstyle \phi }
:

ρ

(

∂

t

u

r
+

u

r

∂

r

u

r
+

u

z

∂

z

u

r
)

=
−

∂

r
p
+
μ

(

1
r

∂

r

(

r

∂

r

u

r
)
+

∂

z

2

u

r
−

u

r

r

2
)
+
ρ

g

r

ρ

(

∂

t

u

z
+

u

r

∂

r

u

z
+

u

z

∂

z

u

z
)

=
−

∂

z
p
+
μ

(

1
r

∂

r

(

r

∂

r

u

z
)
+

∂

z

2

u

z
)
+
ρ

g

z

1
r

∂

r

(

r

u

r
)
+

∂

z

u

z

=
0.
{\displaystyle {\begin{aligned}\rho \left({\partial \_{t}u\_{r}}+u\_{r}{\partial \_{r}u\_{r}}+u\_{z}{\partial \_{z}u\_{r}}\right)&=-{\partial \_{r}p}+\mu \left({\frac {1}{r}}\partial \_{r}\left(r{\partial \_{r}u\_{r}}\right)+{\partial \_{z}^{2}u\_{r}}-{\frac {u\_{r}}{r^{2}}}\right)+\rho g\_{r}\\\rho \left({\partial \_{t}u\_{z}}+u\_{r}{\partial \_{r}u\_{z}}+u\_{z}{\partial \_{z}u\_{z}}\right)&=-{\partial \_{z}p}+\mu \left({\frac {1}{r}}\partial \_{r}\left(r{\partial \_{r}u\_{z}}\right)+{\partial \_{z}^{2}u\_{z}}\right)+\rho g\_{z}\\{\frac {1}{r}}\partial \_{r}\left(ru\_{r}\right)+{\partial \_{z}u\_{z}}&=0.\end{aligned}}}

### Spherical coordinates

In [spherical coordinates](https://en.wikipedia.org/wiki/Spherical_coordinates "Spherical coordinates"), the

r
{\textstyle r}
,

ϕ
{\textstyle \phi }
, and

θ
{\textstyle \theta }
 momentum equations are (note the convention used:

θ
{\textstyle \theta }
 is polar angle, or [colatitude](https://en.wikipedia.org/wiki/Colatitude "Colatitude"),

0
≤
θ
≤
π
{\textstyle 0\leq \theta \leq \pi }
):

r
:
 

ρ

(

∂

t

u

r
+

u

r

∂

r

u

r
+

u

φ

r
sin
⁡
θ

∂

φ

u

r
+

u

θ
r

∂

θ

u

r
−

u

φ

2
+

u

θ

2
r
)

=
−

∂

r
p

+
μ

(

1

r

2

∂

r

(

r

2

∂

r

u

r
)
+

1

r

2

sin

2
⁡
θ

∂

φ

2

u

r
+

1

r

2
sin
⁡
θ

∂

θ

(

sin
⁡
θ

∂

θ

u

r
)
−
2

u

r
+

∂

θ

u

θ
+

u

θ
cot
⁡
θ

r

2
−

2

r

2
sin
⁡
θ

∂

φ

u

φ
)

+

1
3
μ

∂

r

(

1

r

2

∂

r

(

r

2

u

r
)
+

1

r
sin
⁡
θ

∂

θ

(

u

θ
sin
⁡
θ
)
+

1

r
sin
⁡
θ

∂

φ

u

φ
)

+
ρ

g

r
{\displaystyle {\begin{aligned}r:\ &\rho \left({\partial \_{t}u\_{r}}+u\_{r}{\partial \_{r}u\_{r}}+{\frac {u\_{\varphi }}{r\sin \theta }}{\partial \_{\varphi }u\_{r}}+{\frac {u\_{\theta }}{r}}{\partial \_{\theta }u\_{r}}-{\frac {u\_{\varphi }^{2}+u\_{\theta }^{2}}{r}}\right)\\&\quad =-{\partial \_{r}p}\\&\qquad +\mu \left({\frac {1}{r^{2}}}\partial \_{r}\left(r^{2}{\partial \_{r}u\_{r}}\right)+{\frac {1}{r^{2}\sin ^{2}\theta }}{\partial \_{\varphi }^{2}u\_{r}}+{\frac {1}{r^{2}\sin \theta }}\partial \_{\theta }\left(\sin \theta {\partial \_{\theta }u\_{r}}\right)-2{\frac {u\_{r}+{\partial \_{\theta }u\_{\theta }}+u\_{\theta }\cot \theta }{r^{2}}}-{\frac {2}{r^{2}\sin \theta }}{\partial \_{\varphi }u\_{\varphi }}\right)\\&\qquad +{\frac {1}{3}}\mu \partial \_{r}\left({\frac {1}{r^{2}}}\partial \_{r}\left(r^{2}u\_{r}\right)+{\frac {1}{r\sin \theta }}\partial \_{\theta }\left(u\_{\theta }\sin \theta \right)+{\frac {1}{r\sin \theta }}{\partial \_{\varphi }u\_{\varphi }}\right)\\&\qquad +\rho g\_{r}\\[8px]\end{aligned}}}

φ
:
 

ρ

(

∂

t

u

φ
+

u

r

∂

r

u

φ
+

u

φ

r
sin
⁡
θ

∂

φ

u

φ
+

u

θ
r

∂

θ

u

φ
+

u

r

u

φ
+

u

φ

u

θ
cot
⁡
θ
r
)

=
−

1

r
sin
⁡
θ

∂

φ
p

+
μ

(

1

r

2

∂

r

(

r

2

∂

r

u

φ
)
+

1

r

2

sin

2
⁡
θ

∂

φ

2

u

φ
+

1

r

2
sin
⁡
θ

∂

θ

(

sin
⁡
θ

∂

θ

u

φ
)
+

2
sin
⁡
θ

∂

φ

u

r
+
2
cos
⁡
θ

∂

φ

u

θ
−

u

φ

r

2

sin

2
⁡
θ
)

+

1
3
μ

1

r
sin
⁡
θ

∂

φ

(

1

r

2

∂

r

(

r

2

u

r
)
+

1

r
sin
⁡
θ

∂

θ

(

u

θ
sin
⁡
θ
)
+

1

r
sin
⁡
θ

∂

φ

u

φ
)

+
ρ

g

φ
{\displaystyle {\begin{aligned}\varphi :\ &\rho \left({\partial \_{t}u\_{\varphi }}+u\_{r}{\partial \_{r}u\_{\varphi }}+{\frac {u\_{\varphi }}{r\sin \theta }}{\partial \_{\varphi }u\_{\varphi }}+{\frac {u\_{\theta }}{r}}{\partial \_{\theta }u\_{\varphi }}+{\frac {u\_{r}u\_{\varphi }+u\_{\varphi }u\_{\theta }\cot \theta }{r}}\right)\\&\quad =-{\frac {1}{r\sin \theta }}{\partial \_{\varphi }p}\\&\qquad +\mu \left({\frac {1}{r^{2}}}\partial \_{r}\left(r^{2}{\partial \_{r}u\_{\varphi }}\right)+{\frac {1}{r^{2}\sin ^{2}\theta }}{\partial \_{\varphi }^{2}u\_{\varphi }}+{\frac {1}{r^{2}\sin \theta }}\partial \_{\theta }\left(\sin \theta {\partial \_{\theta }u\_{\varphi }}\right)+{\frac {2\sin \theta {\partial \_{\varphi }u\_{r}}+2\cos \theta {\partial \_{\varphi }u\_{\theta }}-u\_{\varphi }}{r^{2}\sin ^{2}\theta }}\right)\\&\qquad +{\frac {1}{3}}\mu {\frac {1}{r\sin \theta }}\partial \_{\varphi }\left({\frac {1}{r^{2}}}\partial \_{r}\left(r^{2}u\_{r}\right)+{\frac {1}{r\sin \theta }}\partial \_{\theta }\left(u\_{\theta }\sin \theta \right)+{\frac {1}{r\sin \theta }}{\partial \_{\varphi }u\_{\varphi }}\right)\\&\qquad +\rho g\_{\varphi }\\[8px]\end{aligned}}}

θ
:
 

ρ

(

∂

t

u

θ
+

u

r

∂

r

u

θ
+

u

φ

r
sin
⁡
θ

∂

φ

u

θ
+

u

θ
r

∂

θ

u

θ
+

u

r

u

θ
−

u

φ

2
cot
⁡
θ
r
)

=
−

1
r

∂

θ
p

+
μ

(

1

r

2

∂

r

(

r

2

∂

r

u

θ
)
+

1

r

2

sin

2
⁡
θ

∂

φ

2

u

θ
+

1

r

2
sin
⁡
θ

∂

θ

(

sin
⁡
θ

∂

θ

u

θ
)
+

2

r

2

∂

θ

u

r
−

u

θ
+
2
cos
⁡
θ

∂

φ

u

φ

r

2

sin

2
⁡
θ
)

+

1
3
μ

1
r

∂

θ

(

1

r

2

∂

r

(

r

2

u

r
)
+

1

r
sin
⁡
θ

∂

θ

(

u

θ
sin
⁡
θ
)
+

1

r
sin
⁡
θ

∂

φ

u

φ
)

+
ρ

g

θ
.
{\displaystyle {\begin{aligned}\theta :\ &\rho \left({\partial \_{t}u\_{\theta }}+u\_{r}{\partial \_{r}u\_{\theta }}+{\frac {u\_{\varphi }}{r\sin \theta }}{\partial \_{\varphi }u\_{\theta }}+{\frac {u\_{\theta }}{r}}{\partial \_{\theta }u\_{\theta }}+{\frac {u\_{r}u\_{\theta }-u\_{\varphi }^{2}\cot \theta }{r}}\right)\\&\quad =-{\frac {1}{r}}{\partial \_{\theta }p}\\&\qquad +\mu \left({\frac {1}{r^{2}}}\partial \_{r}\left(r^{2}{\partial \_{r}u\_{\theta }}\right)+{\frac {1}{r^{2}\sin ^{2}\theta }}{\partial \_{\varphi }^{2}u\_{\theta }}+{\frac {1}{r^{2}\sin \theta }}\partial \_{\theta }\left(\sin \theta {\partial \_{\theta }u\_{\theta }}\right)+{\frac {2}{r^{2}}}{\partial \_{\theta }u\_{r}}-{\frac {u\_{\theta }+2\cos \theta {\partial \_{\varphi }u\_{\varphi }}}{r^{2}\sin ^{2}\theta }}\right)\\&\qquad +{\frac {1}{3}}\mu {\frac {1}{r}}\partial \_{\theta }\left({\frac {1}{r^{2}}}\partial \_{r}\left(r^{2}u\_{r}\right)+{\frac {1}{r\sin \theta }}\partial \_{\theta }\left(u\_{\theta }\sin \theta \right)+{\frac {1}{r\sin \theta }}{\partial \_{\varphi }u\_{\varphi }}\right)\\&\qquad +\rho g\_{\theta }.\end{aligned}}}

Mass continuity will read:

∂

t
ρ
+

1

r

2

∂

r

(

ρ

r

2

u

r
)
+

1

r
sin
⁡
θ

∂

φ
(
ρ

u

φ
)
+

1

r
sin
⁡
θ

∂

θ

(

sin
⁡
θ
ρ

u

θ
)
=
0.
{\displaystyle {\partial \_{t}\rho }+{\frac {1}{r^{2}}}\partial \_{r}\left(\rho r^{2}u\_{r}\right)+{\frac {1}{r\sin \theta }}{\partial \_{\varphi }(\rho u\_{\varphi })}+{\frac {1}{r\sin \theta }}\partial \_{\theta }\left(\sin \theta \rho u\_{\theta }\right)=0.}

These equations could be (slightly) compacted by, for example, factoring

1

r

2
{\textstyle {\frac {1}{r^{2}}}}
 from the viscous terms. However, doing so would undesirably alter the structure of the Laplacian and other quantities.

---

*Source: [Wikipedia — Navier–Stokes equations](https://en.wikipedia.org/wiki/Navier%E2%80%93Stokes_equations). Text licensed under [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/).*
