# Entities Enums/Maps


[Source Code](https://github.com/DerekRies/arkpy/blob/master/arkpy/entities.py)

The Entities Enums and Maps are for easily obtaining the long, complicated
paths that make up the entity path used by the game to represent items.
Entities are broken down first into two categories, `Items` and `Creatures`,
which are further broken down into the categories below.


### Example:
```python
from arkpy import entities

for trophy in entities.Trophy:
    print trophy
    print trophy.value

# Trophy.Alpha_Rex_Trophy
# BlueprintGeneratedClass ..PrimalItemTrophy_AlphaRex.PrimalItemTrophy_AlphaRex
# Trophy.Broodmother_Trophy
# BlueprintGeneratedClass ..PrimalItemTrophy_Broodmother.PrimalItemTrophy_Broodmother
# Trophy.Dragon_Trophy
# BlueprintGeneratedClass ..PrimalItemTrophy_Dragon.PrimalItemTrophy_Dragon
# Trophy.Megapithecus_Trophy
# BlueprintGeneratedClass ..PrimalItemTrophy_Gorilla.PrimalItemTrophy_Gorilla
```
- - -

# Items

- - -

## `Trophy` Class

### extends `enum.Enum`

**Path prefix:** `"BlueprintGeneratedClass /Game/PrimalEarth/CoreBlueprints/Items/Trophies`

| Name | Path (Value) |
|------|--------------|
| **Alpha_Rex_Trophy** | /PrimalItemTrophy_AlphaRex.PrimalItemTrophy_AlphaRex" |
| **Broodmother_Trophy** | /PrimalItemTrophy_Broodmother.PrimalItemTrophy_Broodmother" |
| **Megapithecus_Trophy** | /PrimalItemTrophy_Gorilla.PrimalItemTrophy_Gorilla" |
| **Dragon_Trophy** | /PrimalItemTrophy_Dragon.PrimalItemTrophy_Dragon" |


## `Consumable` Class

### extends `enum.Enum`

**Path prefix:** `"BlueprintGeneratedClass /Game/PrimalEarth/CoreBlueprints/Items/Consumables`

| Name | Path (Value) |
|------|--------------|
| **Raw_Meat** | /PrimalItemConsumable_RawMeat.PrimalItemConsumable_RawMeat" |
| **Spoiled_Meat** | /PrimalItemConsumable_SpoiledMeat.PrimalItemConsumable_SpoiledMeat" |
| **Cooked_Meat** | /PrimalItemConsumable_CookedMeat.PrimalItemConsumable_CookedMeat" |
| **Water_Jar_Empty** | /PrimalItemConsumable_WaterJarCraftable.PrimalItemConsumable_WaterJarCraftable" |
| **Water_Jar_Full** | /PrimalItemConsumable_WaterJarRefill.PrimalItemConsumable_WaterJarRefill" |
| **Waterskin_Empty** | /PrimalItemConsumable_WaterskinCraftable.PrimalItemConsumable_WaterskinCraftable" |
| **Waterskin_Filled** | /PrimalItemConsumable_WaterskinCraftable.PrimalItemRefill_WaterskinRefill" |
| **Bingleberry_Soup** | oup.PrimalItemConsumable_BerrySoup" |
| **Medical_Brew** | /PrimalItemConsumable_HealSoup.PrimalItemConsumable_HealSoup" |
| **Energy_Brew** | /PrimalItemConsumable_StaminaSoup.PrimalItemConsumable_StaminaSoup" |
| **Citronal** | /PrimalItemConsumable_Veggie_Citronal.PrimalItemConsumable_Veggie_Citronal" |
| **Amarberry** | /PrimalItemConsumable_Berry_Amarberry.PrimalItemConsumable_Berry_Amarberry" |
| **Azulberry** | /PrimalItemConsumable_Berry_Azulberry.PrimalItemConsumable_Berry_Azulberry" |
| **Tintoberry** | /PrimalItemConsumable_Berry_Tintoberry.PrimalItemConsumable_Berry_Tintoberry" |
| **Mejoberry** | /PrimalItemConsumable_Berry_Mejoberry.PrimalItemConsumable_Berry_Mejoberry" |
| **Narcoberry** | /PrimalItemConsumable_Berry_Narcoberry.PrimalItemConsumable_Berry_Narcoberry" |
| **Stimberry** | /PrimalItemConsumable_Berry_Stimberry.PrimalItemConsumable_Berry_Stimberry" |
| **Super_Test_MeatRaw** | /PrimalItemConsumable_SuperTestMeat.PrimalItemConsumable" |
| **Enduro_Stew** | /PrimalItemConsumable_Soup_EnduroStew.PrimalItemConsumable_Soup_EnduroStew" |
| **Lazarus_Chowder** | /PrimalItemConsumable_Soup_LazarusChowder.PrimalItemConsumable_Soup_LazarusChowder" |
| **Calien_Soup** | /PrimalItemConsumable_Soup_CalienSoup.PrimalItemConsumable_Soup_CalienSoup" |
| **Fria_Curry** | /PrimalItemConsumable_Soup_FriaCurry.PrimalItemConsumable_Soup_FriaCurry" |
| **Focal_Chili** | /PrimalItemConsumable_Soup_FocalChili.PrimalItemConsumable_Soup_FocalChili" |
| **Savoroot** | /PrimalItemConsumable_Veggie_Savoroot.PrimalItemConsumable_Veggie_Savoroot" |
| **Longrass** | /PrimalItemConsumable_Veggie_Longrass.PrimalItemConsumable_Veggie_Longrass" |
| **Rockarrot** | /PrimalItemConsumable_Veggie_Rockarrot.PrimalItemConsumable_Veggie_Rockarrot" |
| **Raw_Prime_Meat** | /PrimalItemConsumable_RawPrimeMeat.PrimalItemConsumable_RawPrimeMeat" |
| **Cooked_Prime_Meat** | /PrimalItemConsumable_CookedPrimeMeat.PrimalItemConsumable_CookedPrimeMeat" |
| **Battle_Tartare** | /PrimalItemConsumable_Soup_BattleTartare.PrimalItemConsumable_Soup_BattleTartare" |
| **Shadow_Steak_Saute** | /PrimalItemConsumable_Soup_ShadowSteak.PrimalItemConsumable_Soup_ShadowSteak" |
| **Cooked_Meat_Jerky** | /PrimalItemConsumable_CookedMeat_Jerky.PrimalItemConsumable_CookedMeat_Jerky" |
| **Prime_Meat_Jerky** | /PrimalItemConsumable_CookedPrimeMeat_Jerky.PrimalItemConsumable_CookedPrimeMeat_Jerky" |
| **Kibble_Ankylo_Egg** | /PrimalItemConsumable_Kibble_AnkyloEgg.PrimalItemConsumable_Kibble_AnkyloEgg" |
| **Kibble_Argentavis_Egg** | /PrimalItemConsumable_Kibble_ArgentEgg.PrimalItemConsumable_Kibble_ArgentEgg" |
| **Kibble_Titanoboa_Egg** | /PrimalItemConsumable_Kibble_BoaEgg.PrimalItemConsumable_Kibble_BoaEgg" |
| **Kibble_Carno_Egg** | /PrimalItemConsumable_Kibble_CarnoEgg.PrimalItemConsumable_Kibble_CarnoEgg" |
| **Kibble_Dilo_Egg** | /PrimalItemConsumable_Kibble_DiloEgg.PrimalItemConsumable_Kibble_DiloEgg" |
| **Kibble_Dodo_Egg** | /PrimalItemConsumable_Kibble_DodoEgg.PrimalItemConsumable_Kibble_DodoEgg" |
| **Kibble_Parasaur_Egg** | /PrimalItemConsumable_Kibble_ParaEgg.PrimalItemConsumable_Kibble_ParaEgg" |
| **Kibble_Pteranodon_Egg** | /PrimalItemConsumable_Kibble_PteroEgg.PrimalItemConsumable_Kibble_PteroEgg" |
| **Kibble_Raptor_Egg** | /PrimalItemConsumable_Kibble_RaptorEgg.PrimalItemConsumable_Kibble_RaptorEgg" |
| **Kibble_Rex_Egg** | /PrimalItemConsumable_Kibble_RexEgg.PrimalItemConsumable_Kibble_RexEgg" |
| **Kibble_Sarco_Egg** | /PrimalItemConsumable_Kibble_SarcoEgg.PrimalItemConsumable_Kibble_SarcoEgg" |
| **Kibble_Bronto_Egg** | /PrimalItemConsumable_Kibble_SauroEgg.PrimalItemConsumable_Kibble_SauroEgg" |
| **Kibble_Pulmonoscorpius_Egg** | /PrimalItemConsumable_Kibble_ScorpionEgg.PrimalItemConsumable_Kibble_ScorpionEgg" |
| **Kibble_Araneo_Egg** | /PrimalItemConsumable_Kibble_SpiderEgg.PrimalItemConsumable_Kibble_SpiderEgg" |
| **Kibble_Spino_Egg** | /PrimalItemConsumable_Kibble_SpinoEgg.PrimalItemConsumable_Kibble_SpinoEgg" |
| **Kibble_Stego_Egg** | /PrimalItemConsumable_Kibble_StegoEgg.PrimalItemConsumable_Kibble_StegoEgg" |
| **Kibble_Trike_Egg** | /PrimalItemConsumable_Kibble_TrikeEgg.PrimalItemConsumable_Kibble_TrikeEgg" |
| **Kibble_Carbonemys_Egg** | /PrimalItemConsumable_Kibble_TurtleEgg.PrimalItemConsumable_Kibble_TurtleEgg" |
| **Canteen_Empty** | /PrimalItemConsumable_CanteenCraftable.PrimalItemConsumable_CanteenCraftable" |
| **Canteen_Full** | /PrimalItemConsumable_CanteenRefill.PrimalItemConsumable_CanteenRefill" |
| **Plant_Species_X_Seed** | /Seeds/PrimalItemConsumable_Seed_DefensePlant.PrimalItemConsumable_Seed_DefensePlant" |
| **Plant_Species_X_Seed_Instant_grow** | /Seeds/PrimalItemConsumable_Seed_DefensePlant_SpeedHack.PrimalItemConsumable_Seed_DefensePlant_SpeedHack" |
| **Mindwipe_Tonic** | /BaseBPs/PrimalItemConsumableRespecSoup.PrimalItemConsumableRespecSoup" |
| **Kibble_Pachy_Egg** | /PrimalItemConsumable_Kibble_PachyEgg.PrimalItemConsumable_Kibble_PachyEgg" |
| **Kibble_Dimorph_Egg** | /PrimalItemConsumable_Kibble_DimorphEgg.PrimalItemConsumable_Kibble_DimorphEgg" |
| **Broth_of_Enlightenment** | /PrimalItemConsumable_TheHorn.PrimalItemConsumable_TheHorn_C" |
| **Bug_Repellant** | /PrimalItemConsumable_BugRepellant.PrimalItemConsumable_BugRepellant" |
| **Kibble_Quetzal_Egg** | /PrimalItemConsumable_Kibble_QuetzEgg.PrimalItemConsumable_Kibble_QuetzEgg" |
| **Soap** | /BaseBPs/PrimalItemConsumableSoap.PrimalItemConsumableSoap" |
| **Kibble_Kairuku_Egg** | /PrimalItemConsumable_Kibble_KairukuEgg.PrimalItemConsumable_Kibble_KairukuEgg" |
| **Beer_Jar** | /PrimalItemConsumable_BeerJar.PrimalItemConsumable_BeerJar" |
| **Beer_Jar_alt** | /PrimalItemConsumable_BeerJarAlt.PrimalItemConsumable_BeerJarAlt" |
| **Kibble_Dimetrodon_Egg** | /PrimalItemConsumable_Kibble_DimetroEgg.PrimalItemConsumable_Kibble_DimetroEgg" |
| **Box_o_Chocolates** | /Vday/PrimalItemConsumable_ValentinesChocolate.PrimalItemConsumable_ValentinesChocolate" |
| **Kibble_Terror_Bird_Egg** | /PrimalItemConsumable_Kibble_TerrorBirdEgg.PrimalItemConsumable_Kibble_TerrorBirdEgg" |
| **Kibble_Gallimimus_Egg** | /PrimalItemConsumable_Kibble_GalliEgg.PrimalItemConsumable_Kibble_GalliEgg" |
| **Raw_Fish_Meat** | /PrimalItemConsumable_RawMeat_Fish.PrimalItemConsumable_RawMeat_Fish" |
| **Cooked_Fish_Meat** | /PrimalItemConsumable_CookedMeat_Fish.PrimalItemConsumable_CookedMeat_Fish" |
| **Raw_Prime_Fish_Meat** | /PrimalItemConsumable_RawPrimeMeat_Fish.PrimalItemConsumable_RawPrimeMeat_Fish" |
| **Cooked_Prime_Fish_Meat** | /PrimalItemConsumable_CookedPrimeMeat_Fish.PrimalItemConsumable_CookedPrimeMeat_Fish" |
| **Diplo_Egg** | plo.PrimalItemConsumable_Egg_Diplo" |
| **Kibble_Diplo_Egg** | /PrimalItemConsumable_Kibble_DiploEgg.PrimalItemConsumable_Kibble_DiploEgg" |
| **Lystro_Egg** | stro.PrimalItemConsumable_Egg_Lystro" |
| **Kibble_Lystrosaurus_Egg** | /PrimalItemConsumable_Kibble_LystroEgg.PrimalItemConsumable_Kibble_LystroEgg" |
| **Lesser_Antidote** | /BaseBPs/PrimalItemConsumable_CureLow.PrimalItemConsumable_CureLow" |
| **Sweet_Veggie_Cake** | /PrimalItemConsumable_SweetVeggieCake.PrimalItemConsumable_SweetVeggieCake" |


## `Resource` Class

### extends `enum.Enum`

**Path prefix:** `"BlueprintGeneratedClass /Game/PrimalEarth/CoreBlueprints/Resources`

| Name | Path (Value) |
|------|--------------|
| **Wood** | /PrimalItemResource_Wood.PrimalItemResource_Wood" |
| **Stone** | /PrimalItemResource_Stone.PrimalItemResource_Stone" |
| **Metal** | /PrimalItemResource_Metal.PrimalItemResource_Metal" |
| **Hide** | /PrimalItemResource_Hide.PrimalItemResource_Hide" |
| **Chitin** | /PrimalItemResource_Chitin.PrimalItemResource_Chitin" |
| **Blood_Pack** | sumables/PrimalItemConsumable_BloodPack.PrimalItemConsumable_BloodPack" |
| **Fertilizer** | sumables/PrimalItemConsumable_Fertilizer_Compost.PrimalItemConsumable_Fertilizer_Compost" |
| **Flint** | /PrimalItemResource_Flint.PrimalItemResource_Flint" |
| **Metal_Ingot** | /PrimalItemResource_MetalIngot.PrimalItemResource_MetalIngot" |
| **Thatch** | /PrimalItemResource_Thatch.PrimalItemResource_Thatch" |
| **Fiber** | /PrimalItemResource_Fibers.PrimalItemResource_Fibers" |
| **Charcoal** | /PrimalItemResource_Charcoal.PrimalItemResource_Charcoal" |
| **Crystal** | /PrimalItemResource_Crystal.PrimalItemResource_Crystal" |
| **Sparkpowder** | /PrimalItemResource_Sparkpowder.PrimalItemResource_Sparkpowder" |
| **Gunpowder** | /PrimalItemResource_Gunpowder.PrimalItemResource_Gunpowder" |
| **Narcotic** | sumables/PrimalItemConsumable_Narcotic.PrimalItemConsumable_Narcotic" |
| **Stimulant** | sumables/PrimalItemConsumable_Stimulant.PrimalItemConsumable_Stimulant" |
| **Obsidian** | /PrimalItemResource_Obsidian.PrimalItemResource_Obsidian" |
| **Cementing_Paste** | /PrimalItemResource_ChitinPaste.PrimalItemResource_ChitinPaste" |
| **Oil** | /PrimalItemResource_Oil.PrimalItemResource_Oil" |
| **Silica_Pearls** | /PrimalItemResource_Silicon.PrimalItemResource_Silicon" |
| **Gasoline** | /PrimalItemResource_Gasoline.PrimalItemResource_Gasoline" |
| **Electronics** | /PrimalItemResource_Electronics.PrimalItemResource_Electronics" |
| **Polymer** | /PrimalItemResource_Polymer.PrimalItemResource_Polymer" |
| **Chitin_or_Keratin** | /PrimalItemResource_ChitinOrKeratin.PrimalItemResource_ChitinOrKeratin" |
| **Keratin** | /PrimalItemResource_Keratin.PrimalItemResource_Keratin" |
| **Rare_Flower** | /PrimalItemResource_RareFlower.PrimalItemResource_RareFlower" |
| **Rare_Mushroom** | /PrimalItemResource_RareMushroom.PrimalItemResource_RareMushroom" |
| **Re_Fertilizer** | sumables/BaseBPs/PrimalItemConsumableMiracleGro.PrimalItemConsumableMiracleGro" |
| **Pelt** | /PrimalItemResource_Pelt.PrimalItemResource_Pelt" |
| **Organic_Polymer** | /PrimalItemResource_Polymer_Organic.PrimalItemResource_Polymer_Organic" |
| **Angler_Gel** | /PrimalItemResource_AnglerGel.PrimalItemResource_AnglerGel" |
| **Wishbone** | /PrimalItemResource_Wishbone.PrimalItemResource_Wishbone" |
| **Mistletoe** | /PrimalItemResource_MistleToe.PrimalItemResource_MistleToe" |
| **Coal** | /PrimalItemResource_Coal.PrimalItemResource_Coal" |
| **Black_Pearl** | /PrimalItemResource_BlackPearl.PrimalItemResource_BlackPearl_C" |
| **Woolly_Rhino_Horn** | /PrimalItemResource_Horn.PrimalItemResource_Horn_C" |
| **Birthday_Candle** | /PrimalItemResource_BirthdayCandle.PrimalItemResource_BirthdayCandle" |
| **Birthday_Cake** | uctures/Halloween/PrimalItemStructure_BirthdayCake.PrimalItemStructure_BirthdayCake" |
| **Leech_Blood** | /PrimalItemResource_LeechBlood.PrimalItemResource_LeechBlood" |
| **Sap** | /PrimalItemResource_Sap.PrimalItemResource_Sap" |
| **Absorbent_Substrate** | /PrimalItemResource_SubstrateAbsorbent.PrimalItemResource_SubstrateAbsorbent" |


## `Saddle` Class

### extends `enum.Enum`

**Path prefix:** `"BlueprintGeneratedClass /Game/PrimalEarth/CoreBlueprints/Items/Armor/Saddles`

| Name | Path (Value) |
|------|--------------|
| **Rex_Saddle** | /PrimalItemArmor_RexSaddle.PrimalItemArmor_RexSaddle" |
| **Parasaur_Saddle** | /PrimalItemArmor_ParaSaddle.PrimalItemArmor_ParaSaddle" |
| **Raptor_Saddle** | /PrimalItemArmor_RaptorSaddle.PrimalItemArmor_RaptorSaddle" |
| **Stego_Saddle** | /PrimalItemArmor_StegoSaddle.PrimalItemArmor_StegoSaddle" |
| **Trike_Saddle** | /PrimalItemArmor_TrikeSaddle.PrimalItemArmor_TrikeSaddle" |
| **Pulmonoscorpius_Saddle** | /PrimalItemArmor_ScorpionSaddle.PrimalItemArmor_ScorpionSaddle" |
| **Pteranodon_Saddle** | /PrimalItemArmor_PteroSaddle.PrimalItemArmor_PteroSaddle" |
| **Bronto_Saddle** | /PrimalItemArmor_SauroSaddle.PrimalItemArmor_SauroSaddle" |
| **Carbonemys_Saddle** | /PrimalItemArmor_TurtleSaddle.PrimalItemArmor_TurtleSaddle" |
| **Sarco_Saddle** | /PrimalItemArmor_SarcoSaddle.PrimalItemArmor_SarcoSaddle" |
| **Ankylo_Saddle** | /PrimalItemArmor_AnkyloSaddle.PrimalItemArmor_AnkyloSaddle" |
| **Mammoth_Saddle** | /PrimalItemArmor_MammothSaddle.PrimalItemArmor_MammothSaddle" |
| **Megalodon_Saddle** | /PrimalItemArmor_MegalodonSaddle.PrimalItemArmor_MegalodonSaddle" |
| **Sabertooth_Saddle** | /PrimalItemArmor_SaberSaddle.PrimalItemArmor_SaberSaddle" |
| **Carno_Saddle** | /PrimalItemArmor_CarnoSaddle.PrimalItemArmor_CarnoSaddle" |
| **Argentavis_Saddle** | /PrimalItemArmor_ArgentavisSaddle.PrimalItemArmor_ArgentavisSaddle" |
| **Phiomia_Saddle** | /PrimalItemArmor_PhiomiaSaddle.PrimalItemArmor_PhiomiaSaddle" |
| **Spino_Saddle** | /PrimalItemArmor_SpinoSaddle.PrimalItemArmor_SpinoSaddle" |
| **Plesiosaur_Saddle** | /PrimalItemArmor_PlesiaSaddle.PrimalItemArmor_PlesiaSaddle" |
| **Ichthyosaurus_Saddle** | /PrimalItemArmor_DolphinSaddle.PrimalItemArmor_DolphinSaddle" |
| **Doedicurus_Saddle** | /PrimalItemArmor_DoedSaddle.PrimalItemArmor_DoedSaddle" |
| **Bronto_Platform_Saddle** | /PrimalItemArmor_SauroSaddle_Platform.PrimalItemArmor_SauroSaddle_Platform" |
| **Pachy_Saddle** | /PrimalItemArmor_PachySaddle.PrimalItemArmor_PachySaddle" |
| **Paracer_Saddle** | /PrimalItemArmor_Paracer_Saddle.PrimalItemArmor_Paracer_Saddle" |
| **Paracer_Platform_Saddle** | /PrimalItemArmor_ParacerSaddle_Platform.PrimalItemArmor_ParacerSaddle_Platform" |
| **Beelzebufo_Saddle** | /PrimalItemArmor_ToadSaddle.PrimalItemArmor_ToadSaddle" |
| **Megaloceros_Saddle** | /PrimalItemArmor_StagSaddle.PrimalItemArmor_StagSaddle" |
| **Plesiosaur_Platform_Saddle** | /PrimalItemArmor_PlesiSaddle_Platform.PrimalItemArmor_PlesiSaddle_Platform" |
| **Quetz_Platform_Saddle** | /PrimalItemArmor_QuetzSaddle_Platform.PrimalItemArmor_QuetzSaddle_Platform" |
| **Mosasaurus_Platform_Saddle** | /PrimalItemArmor_MosaSaddle_Platform.PrimalItemArmor_MosaSaddle_Platform" |
| **Mosasaurus_Saddle** | /PrimalItemArmor_MosaSaddle.PrimalItemArmor_MosaSaddle" |
| **Quetz_Saddle** | /PrimalItemArmor_QuetzSaddle.PrimalItemArmor_QuetzSaddle" |
| **Araneo_Saddle** | /PrimalItemArmor_SpiderSaddle.PrimalItemArmor_SpiderSaddle" |
| **Giganotosaurus_Saddle** | /PrimalItemArmor_GigantSaddle.PrimalItemArmor_GigantSaddle" |
| **Procoptodon_Saddle** | /PrimalItemArmor_ProcoptodonSaddle.PrimalItemArmor_ProcoptodonSaddle" |
| **Gallimimus_Saddle** | /PrimalItemArmor_Gallimimus.PrimalItemArmor_Gallimimus" |
| **Terror_Bird_Saddle** | /PrimalItemArmor_TerrorBirdSaddle.PrimalItemArmor_TerrorBirdSaddle" |
| **Castoroides_Saddle** | /PrimalItemArmor_BeaverSaddle.PrimalItemArmor_BeaverSaddle" |
| **Woolly_Rhino_Saddle** | /PrimalItemArmor_RhinoSaddle.PrimalItemArmor_RhinoSaddle" |
| **Dunkleosteus_Saddle** | /PrimalItemArmor_DunkleosteusSaddle.PrimalItemArmor_DunkleosteusSaddle" |
| **Direbear_Saddle** | /PrimalItemArmor_DireBearSaddle.PrimalItemArmor_DireBearSaddle" |
| **Manta_Saddle** | /PrimalItemArmor_MantaSaddle.PrimalItemArmor_MantaSaddle" |
| **Arthropluera_Saddle** | /PrimalItemArmor_ArthroSaddle.PrimalItemArmor_ArthroSaddle" |
| **Diplodocus_Saddle** | /PrimalItemArmor_DiplodocusSaddle.PrimalItemArmor_DiplodocusSaddle" |
| **Titanosaur_Platform_Saddle** | /PrimalItemArmor_TitanSaddle_Platform.PrimalItemArmor_TitanSaddle_Platform" |


## `Armor` Class

### extends `enum.Enum`

**Path prefix:** `"BlueprintGeneratedClass /Game/PrimalEarth/CoreBlueprints/Items/Armor/Cloth`

| Name | Path (Value) |
|------|--------------|
| **Cloth_Pants** | /PrimalItemArmor_ClothPants.PrimalItemArmor_ClothPants" |
| **Cloth_Shirt** | /PrimalItemArmor_ClothShirt.PrimalItemArmor_ClothShirt" |
| **Cloth_Hat** | /PrimalItemArmor_ClothHelmet.PrimalItemArmor_ClothHelmet" |
| **Cloth_Boots** | /PrimalItemArmor_ClothBoots.PrimalItemArmor_ClothBoots" |
| **Cloth_Gloves** | /PrimalItemArmor_ClothGloves.PrimalItemArmor_ClothGloves" |
| **Hide_Pants** | PrimalItemArmor_HidePants.PrimalItemArmor_HidePants" |
| **Hide_Shirt** | PrimalItemArmor_HideShirt.PrimalItemArmor_HideShirt" |
| **Hide_Hat** | PrimalItemArmor_HideHelmet.PrimalItemArmor_HideHelmet" |
| **Hide_Boots** | PrimalItemArmor_HideBoots.PrimalItemArmor_HideBoots" |
| **Hide_Gloves** | PrimalItemArmor_HideGloves.PrimalItemArmor_HideGloves" |
| **Chitin_Leggings** | /PrimalItemArmor_ChitinPants.PrimalItemArmor_ChitinPants" |
| **Chitin_Chestpiece** | /PrimalItemArmor_ChitinShirt.PrimalItemArmor_ChitinShirt" |
| **Chitin_Helmet** | n/PrimalItemArmor_ChitinHelmet.PrimalItemArmor_ChitinHelmet" |
| **Chitin_Boots** | n/PrimalItemArmor_ChitinBoots.PrimalItemArmor_ChitinBoots" |
| **Chitin_Gauntlets** | n/PrimalItemArmor_ChitinGloves.PrimalItemArmor_ChitinGloves" |
| **Parachute** | /BaseBPs/PrimalItemConsumableBuff_Parachute.PrimalItemConsumableBuff_Parachute" |
| **Flak_Leggings** | /PrimalItemArmor_MetalPants.PrimalItemArmor_MetalPants" |
| **Flak_Chestpiece** | /PrimalItemArmor_MetalShirt.PrimalItemArmor_MetalShirt" |
| **Flak_Helmet** | /PrimalItemArmor_MetalHelmet.PrimalItemArmor_MetalHelmet" |
| **Flak_Boots** | /PrimalItemArmor_MetalBoots.PrimalItemArmor_MetalBoots" |
| **Flak_Gauntlets** | /PrimalItemArmor_MetalGloves.PrimalItemArmor_MetalGloves" |
| **Heavy_Miners_Helmet** | /PrimalItemArmor_MinersHelmet.PrimalItemArmor_MinersHelmet" |
| **SCUBA_Tank** | /PrimalItemArmor_ScubaShirt_SuitWithTank.PrimalItemArmor_ScubaShirt_SuitWithTank" |
| **SCUBA_Mask** | /PrimalItemArmor_ScubaHelmet_Goggles.PrimalItemArmor_ScubaHelmet_Goggles" |
| **SCUBA_Flippers** | /PrimalItemArmor_ScubaBoots_Flippers.PrimalItemArmor_ScubaBoots_Flippers" |
| **Fur_Leggings** | rimalItemArmor_FurPants.PrimalItemArmor_FurPants" |
| **Fur_Chestpiece** | rimalItemArmor_FurShirt.PrimalItemArmor_FurShirt" |
| **Fur_Cap** | rimalItemArmor_FurHelmet.PrimalItemArmor_FurHelmet" |
| **Fur_Boots** | rimalItemArmor_FurBoots.PrimalItemArmor_FurBoots" |
| **Fur_Gauntlets** | rimalItemArmor_FurGloves.PrimalItemArmor_FurGloves" |
| **Riot_Leggings** | PrimalItemArmor_RiotPants.PrimalItemArmor_RiotPants" |
| **Riot_Chestpiece** | PrimalItemArmor_RiotShirt.PrimalItemArmor_RiotShirt" |
| **Riot_Gauntlets** | PrimalItemArmor_RiotGloves.PrimalItemArmor_RiotGloves" |
| **Riot_Boots** | PrimalItemArmor_RiotBoots.PrimalItemArmor_RiotBoots" |
| **Riot_Helmet** | PrimalItemArmor_RiotHelmet.PrimalItemArmor_RiotHelmet" |
| **SCUBA_Leggings** | /PrimalItemArmor_ScubaPants.PrimalItemArmor_ScubaPants" |
| **Wooden_Shield** | ds/PrimalItemArmor_WoodShield.PrimalItemArmor_WoodShield" |
| **Metal_Shield** | ds/PrimalItemArmor_MetalShield.PrimalItemArmor_MetalShield" |
| **Riot_Shield** | ds/PrimalItemArmor_TransparentRiotShield.PrimalItemArmor_TransparentRiotShield" |
| **Ghillie_Boots** | ie/PrimalItemArmor_GhillieBoots.PrimalItemArmor_GhillieBoots" |
| **Ghillie_Chestpiece** | ie/PrimalItemArmor_GhillieShirt.PrimalItemArmor_GhillieShirt" |
| **Ghillie_Gauntlets** | ie/PrimalItemArmor_GhillieGloves.PrimalItemArmor_GhillieGloves" |
| **Ghillie_Leggings** | ie/PrimalItemArmor_GhilliePants.PrimalItemArmor_GhilliePants" |
| **Ghillie_Mask** | ie/PrimalItemArmor_GhillieHelmet.PrimalItemArmor_GhillieHelmet" |
| **Gas_Mask** | /PrimalItemArmor_GasMask.PrimalItemArmor_GasMask" |


## `Tool` Class

### extends `enum.Enum`

**Path prefix:** `"BlueprintGeneratedClass /Game/PrimalEarth/CoreBlueprints/Weapons`

| Name | Path (Value) |
|------|--------------|
| **Stone_Pick** | /PrimalItem_WeaponStonePick.PrimalItem_WeaponStonePick" |
| **Stone_Hatchet** | /PrimalItem_WeaponStoneHatchet.PrimalItem_WeaponStoneHatchet" |
| **Metal_Pick** | /PrimalItem_WeaponMetalPick.PrimalItem_WeaponMetalPick" |
| **Metal_Hatchet** | /PrimalItem_WeaponMetalHatchet.PrimalItem_WeaponMetalHatchet" |
| **Torch** | /PrimalItem_WeaponTorch.PrimalItem_WeaponTorch" |
| **Paintbrush** | /PrimalItem_WeaponPaintbrush.PrimalItem_WeaponPaintbrush" |
| **Blood_Extraction_Syringe** | xtractor.PrimalItem_BloodExtractor" |
| **GPS** | GPS.PrimalItem_WeaponGPS" |
| **Compass** | Compass.PrimalItem_WeaponCompass" |
| **Radio** | /PrimalItemRadio.PrimalItemRadio" |
| **Spyglass** | Spyglass.PrimalItem_WeaponSpyglass" |


## `Recipe` Class

### extends `enum.Enum`

**Path prefix:** `"BlueprintGeneratedClass /Game/PrimalEarth/CoreBlueprints/Items/Notes`

| Name | Path (Value) |
|------|--------------|
| **Rockwell_Recipes__Enduro_Stew** | /PrimalItem_RecipeNote_EnduroStew.PrimalItem_RecipeNote_EnduroStew" |
| **BluePrint_Note** |  |
| **Rockwell_Recipes__Lazarus_Chowder** | /PrimalItem_RecipeNote_LazarusChowder.PrimalItem_RecipeNote_LazarusChowder" |
| **Rockwell_Recipes__Calien_Soup** | /PrimalItem_RecipeNote_CalienSoup.PrimalItem_RecipeNote_CalienSoup" |
| **Rockwell_Recipes__Fria_Curry** | /PrimalItem_RecipeNote_FriaCurry.PrimalItem_RecipeNote_FriaCurry" |
| **Rockwell_Recipes__Focal_Chili** | /PrimalItem_RecipeNote_FocalChili.PrimalItem_RecipeNote_FocalChili" |
| **Rockwell_Recipes__Battle_Tartare** | /PrimalItem_RecipeNote_BattleTartare.PrimalItem_RecipeNote_BattleTartare" |
| **Rockwell_Recipes__Shadow_Steak_Saute** | /PrimalItem_RecipeNote_ShadowSteak.PrimalItem_RecipeNote_ShadowSteak" |
| **Notes_on_Rockwell_Recipes** | /PrimalItem_RecipeNote_Measurements.PrimalItem_RecipeNote_Measurements" |
| **Rockwell_Recipes__Medical_Brew** | /PrimalItem_RecipeNote_HealSoup.PrimalItem_RecipeNote_HealSoup" |
| **Rockwell_Recipes__Energy_Brew** | /PrimalItem_RecipeNote_StaminaSoup.PrimalItem_RecipeNote_StaminaSoup" |
| **Rockwell_Recipes__Meat_Jerky** | /PrimalItem_RecipeNote_Jerky.PrimalItem_RecipeNote_Jerky" |
| **Rockwell_Recipes__Egg_based_Kibble** | /PrimalItem_RecipeNote_Kibble.PrimalItem_RecipeNote_Kibble" |
| **Rockwell_Recipes__Decorative_Coloring** | /PrimalItem_RecipeNote_Dye.PrimalItem_RecipeNote_Dye" |
| **Rockwell_Recipes__Mindwipe_Tonic** | /PrimalItem_RecipeNote_RespecSoup.PrimalItem_RecipeNote_RespecSoup" |


## `Artifact` Class

### extends `enum.Enum`

**Path prefix:** `"BlueprintGeneratedClass /Game/PrimalEarth/CoreBlueprints/Items/Notes`

| Name | Path (Value) |
|------|--------------|
| **Specimen_Implant** | /PrimalItem_StartingNote.PrimalItem_StartingNote" |
| **Summon_Broodmother** | /Cloth/PrimalItem_BossTribute1.PrimalItem_BossTribute1" |
| **Artifact_Of_The_Hunter** | acts/PrimalItemArtifact_01.PrimalItemArtifact_01" |
| **Artifact_Of_The_Pack** | acts/PrimalItemArtifact_02.PrimalItemArtifact_02" |
| **Artifact_Of_The_Massive** | acts/PrimalItemArtifact_03.PrimalItemArtifact_03" |
| **Artifact_Of_The_Devious** | acts/PrimalItemArtifact_04.PrimalItemArtifact_04" |
| **Artifact_Of_The_Clever** | acts/PrimalItemArtifact_05.PrimalItemArtifact_05" |
| **Artifact_Of_The_Skylord** | acts/PrimalItemArtifact_06.PrimalItemArtifact_06" |
| **Artifact_Of_The_Devourer** | acts/PrimalItemArtifact_07.PrimalItemArtifact_07" |
| **Artifact_Of_The_Immune** | acts/PrimalItemArtifact_08.PrimalItemArtifact_08" |
| **Artifact_Of_The_Strong** | acts/PrimalItemArtifact_09.PrimalItemArtifact_09" |
| **Artifact_Of_The_Flamekeeper** | acts/PrimalItemArtifact_10.PrimalItemArtifact_10" |
| **Argentavis_Talon** | rimalItemResource_ApexDrop_Argentavis.PrimalItemResource_ApexDrop_Argentavis" |
| **Megalodon_Tooth** | rimalItemResource_ApexDrop_Megalodon.PrimalItemResource_ApexDrop_Megalodon" |
| **Tyrannosaurus_Arm** | rimalItemResource_ApexDrop_Rex.PrimalItemResource_ApexDrop_Rex" |
| **Sauropod_Vertebra** | rimalItemResource_ApexDrop_Sauro.PrimalItemResource_ApexDrop_Sauro" |


## `Weapons` Class

### extends `enum.Enum`

**Path prefix:** `"BlueprintGeneratedClass /Game/PrimalEarth/CoreBlueprints/Weapons`

| Name | Path (Value) |
|------|--------------|
| **Simple_Pistol** | /PrimalItem_WeaponGun.PrimalItem_WeaponGun" |
| **Assault_Rifle** | /PrimalItem_WeaponRifle.PrimalItem_WeaponRifle" |
| **Rocket_Launcher** | /PrimalItem_WeaponRocketLauncher.PrimalItem_WeaponRocketLauncher" |
| **Bow** | /PrimalItem_WeaponBow.PrimalItem_WeaponBow" |
| **Grenade** | /PrimalItem_WeaponGrenade.PrimalItem_WeaponGrenade" |
| **C4_Remote_Detonator** | /PrimalItem_WeaponC4.PrimalItem_WeaponC4" |
| **Improvised_Explosive_Device** | /PrimalItem_WeaponTripwireC4.PrimalItem_WeaponTripwireC4" |
| **Spear** | /PrimalItem_WeaponSpear.PrimalItem_WeaponSpear" |
| **Longneck_Rifle** | /PrimalItem_WeaponOneShotRifle.PrimalItem_WeaponOneShotRifle" |
| **Slingshot** | /PrimalItem_WeaponSlingshot.PrimalItem_WeaponSlingshot" |
| **Pike** | /PrimalItem_WeaponPike.PrimalItem_WeaponPike" |
| **Flare_Gun** | /PrimalItem_WeaponFlareGun.PrimalItem_WeaponFlareGun" |
| **Fabricated_Pistol** | /PrimalItem_WeaponMachinedPistol.PrimalItem_WeaponMachinedPistol" |
| **Shotgun** | /PrimalItem_WeaponShotgun.PrimalItem_WeaponShotgun" |
| **Tripwire_Narcotic_Trap** | /PrimalItem_WeaponPoisonTrap.PrimalItem_WeaponPoisonTrap" |
| **Tripwire_Alarm_Trap** | /PrimalItem_WeaponAlarmTrap.PrimalItem_WeaponAlarmTrap" |
| **Pump_Action_Shotgun** | /PrimalItem_WeaponMachinedShotgun.PrimalItem_WeaponMachinedShotgun" |
| **Crossbow** | /PrimalItem_WeaponCrossbow.PrimalItem_WeaponCrossbow" |
| **Transponder_Tracker** | /PrimalItem_WeaponTransGPS.PrimalItem_WeaponTransGPS" |
| **Compound_Bow** | /PrimalItem_WeaponCompoundBow.PrimalItem_WeaponCompoundBow" |
| **Metal_Sickle** | /PrimalItem_WeaponSickle.PrimalItem_WeaponSickle" |
| **Bear_Trap** | tructures/Misc/PrimalItemStructure_BearTrap.PrimalItemStructure_BearTrap" |
| **Large_Bear_Trap** | tructures/Misc/PrimalItemStructure_BearTrap_Large.PrimalItemStructure_BearTrap_Large" |
| **Spray_Painter** | /PrimalItem_WeaponSprayPaint.PrimalItem_WeaponSprayPaint" |
| **Wooden_Club** | /PrimalItem_WeaponStoneClub.PrimalItem_WeaponStoneClub" |
| **Poison_Grenade** | /PrimalItem_PoisonGrenade.PrimalItem_PoisonGrenade" |
| **Fabricated_Sniper_Rifle** | /PrimalItem_WeaponMachinedSniper.PrimalItem_WeaponMachinedSniper" |
| **Electric_Prod** | /PrimalItem_WeaponProd.PrimalItem_WeaponProd" |
| **Handcuffs** | /PrimalItem_WeaponHandcuffs.PrimalItem_WeaponHandcuffs" |
| **Smoke_Grenade** | /PrimalItem_GasGrenade.PrimalItem_GasGrenade" |
| **Metal_Sword** | /PrimalItem_WeaponSword.PrimalItem_WeaponSword" |
| **Magnifying_Glass** | MagnifyingGlass.PrimalItem_WeaponMagnifyingGlass" |
| **Bola** | /PrimalItem_WeaponBola.PrimalItem_WeaponBola" |
| **Chain_Bola** | /PrimalItemAmmo_ChainBola.PrimalItemAmmo_ChainBola" |


## `Seed` Class

### extends `enum.Enum`

**Path prefix:** `"BlueprintGeneratedClass /Game/PrimalEarth/CoreBlueprints/Items/Consumables/Seeds`

| Name | Path (Value) |
|------|--------------|
| **Azulberry_Seed** | /PrimalItemConsumable_Seed_Azulberry.PrimalItemConsumable_Seed_Azulberry" |
| **Tintoberry_Seed** | /PrimalItemConsumable_Seed_Tintoberry.PrimalItemConsumable_Seed_Tintoberry" |
| **Mejoberry_Seed** | /PrimalItemConsumable_Seed_Mejoberry.PrimalItemConsumable_Seed_Mejoberry" |
| **Narcoberry_Seed** | /PrimalItemConsumable_Seed_Narcoberry.PrimalItemConsumable_Seed_Narcoberry" |
| **Stimberry_Seed** | /PrimalItemConsumable_Seed_Stimberry.PrimalItemConsumable_Seed_Stimberry" |
| **Savoroot_Seed** | /PrimalItemConsumable_Seed_Savoroot.PrimalItemConsumable_Seed_Savoroot" |
| **Longrass_Seed** | /PrimalItemConsumable_Seed_Longrass.PrimalItemConsumable_Seed_Longrass" |
| **Rockarrot_Seed** | /PrimalItemConsumable_Seed_Rockarrot.PrimalItemConsumable_Seed_Rockarrot" |


## `Attachment` Class

### extends `enum.Enum`

**Path prefix:** `"BlueprintGeneratedClass /Game/PrimalEarth/CoreBlueprints/Items/WeaponAttachments`

| Name | Path (Value) |
|------|--------------|
| **Scope_Attachment** | /PrimalItemWeaponAttachment_Scope.PrimalItemWeaponAttachment_Scope" |
| **Flashlight_Attachment** | /PrimalItemWeaponAttachment_Flashlight.PrimalItemWeaponAttachment_Flashlight" |
| **Silencer_Attachment** | /PrimalItemWeaponAttachment_Silencer.PrimalItemWeaponAttachment_Silencer" |
| **Holo_Scope_Attachment** | /PrimalItemWeaponAttachment_HoloScope.PrimalItemWeaponAttachment_HoloScope" |
| **Laser_Attachment** | /PrimalItemWeaponAttachment_Laser.PrimalItemWeaponAttachment_Laser" |


## `Skin` Class

### extends `enum.Enum`

**Path prefix:** ``

| Name | Path (Value) |
|------|--------------|
| **Pistol_Hat_Skins** | "" |
| **Hunter_Hat_Skin** | "BlueprintGeneratedClass /Game/PrimalEarth/CoreBlueprints/Items/Armor/Leather/PrimalItemArmor_HideHelmetAlt.PrimalItemArmor_HideHelmetAlt" |
| **Rex_Stomped_Glasses_Saddle_Skin** | "BlueprintGeneratedClass /Game/PrimalEarth/CoreBlueprints/Items/Armor/Saddles/PrimalItemArmor_RexSaddle_StompedGlasses.PrimalItemArmor_RexSaddle_StompedGlasses" |
| **Parasaur_ARK_Founder_Saddle_Skin** | "BlueprintGeneratedClass /Game/PrimalEarth/CoreBlueprints/Items/Armor/Saddles/PrimalItemArmor_ParaSaddle_Launch.PrimalItemArmor_ParaSaddle_Launch" |
| **Rex_Bone_Helmet** | "BlueprintGeneratedClass /Game/PrimalEarth/CoreBlueprints/Items/Armor/Leather/PrimalItemSkin_BoneHelmet.PrimalItemSkin_BoneHelmet" |
| **Nerdry_Glasses** | "BlueprintGeneratedClass /Game/PrimalEarth/CoreBlueprints/Items/Armor/Leather/PrimalItemSkin_Glasses.PrimalItemSkin_Glasses" |
| **Dino_Glasses** | "BlueprintGeneratedClass /Game/PrimalEarth/CoreBlueprints/Items/Armor/Leather/PrimalItemSkin_DinoSpecs.PrimalItemSkin_DinoSpecs" |
| **Fireworks_Flaregun_Skin** | "BlueprintGeneratedClass /Game/PrimalEarth/CoreBlueprints/Items/Armor/Leather/PrimalItemSkin_FlaregunFireworks.PrimalItemSkin_FlaregunFireworks" |
| **Trike_Bone_Helmet_Skin** | "BlueprintGeneratedClass /Game/PrimalEarth/CoreBlueprints/Items/Armor/Leather/PrimalItemSkin_TrikeSkullHelmet.PrimalItemSkin_TrikeSkullHelmet" |
| **DodoRex_Mask_Skin** | "BlueprintGeneratedClass /Game/PrimalEarth/CoreBlueprints/Items/Armor/Skin/PrimalItemSkin_DodorexMask.PrimalItemSkin_DodorexMask" |
| **Witch_Hat_Skin** | "BlueprintGeneratedClass /Game/PrimalEarth/CoreBlueprints/Items/Armor/Skin/PrimalItemSkin_WitchHat.PrimalItemSkin_WitchHat" |
| **Dino_Witch_Hat_Skin** | "BlueprintGeneratedClass /Game/PrimalEarth/CoreBlueprints/Items/Armor/Leather/PrimalItemSkin_DinoWitchHat.PrimalItemSkin_DinoWitchHat" |
| **Carno_Bone_Costume** | "BlueprintGeneratedClass /Game/PrimalEarth/CoreBlueprints/Items/Armor/Saddles/PrimalItemCostume_BoneCarno.PrimalItemCostume_BoneCarno" |
| **Raptor_Bone_Costume** | "BlueprintGeneratedClass /Game/PrimalEarth/CoreBlueprints/Items/Armor/Saddles/PrimalItemCostume_BoneRaptor.PrimalItemCostume_BoneRaptor" |
| **Rex_Bone_Costume** | "BlueprintGeneratedClass /Game/PrimalEarth/CoreBlueprints/Items/Armor/Saddles/PrimalItemCostume_BoneRex.PrimalItemCostume_BoneRex" |
| **Bronto_Bone_Costume** | "BlueprintGeneratedClass /Game/PrimalEarth/CoreBlueprints/Items/Armor/Saddles/PrimalItemCostume_BoneSauro.PrimalItemCostume_BoneSauro" |
| **Stego_Bone_Costume** | "BlueprintGeneratedClass /Game/PrimalEarth/CoreBlueprints/Items/Armor/Saddles/PrimalItemCostume_BoneStego.PrimalItemCostume_BoneStego" |
| **Trike_Bone_Costume** | "BlueprintGeneratedClass /Game/PrimalEarth/CoreBlueprints/Items/Armor/Saddles/PrimalItemCostume_BoneTrike.PrimalItemCostume_BoneTrike" |
| **Chieftan_Hat_Skin** | "BlueprintGeneratedClass /Game/PrimalEarth/CoreBlueprints/Items/Armor/Skin/PrimalItemSkin_TurkeyHat.PrimalItemSkin_TurkeyHat" |
| **Santa_Hat_Skin** | "BlueprintGeneratedClass /Game/PrimalEarth/CoreBlueprints/Items/Armor/Skin/PrimalItemSkin_SantaHat.PrimalItemSkin_SantaHat" |
| **Dino_Santa_Hat_Skin** | "BlueprintGeneratedClass /Game/PrimalEarth/CoreBlueprints/Items/Armor/Skin/PrimalItemSkin_DinoSantaHat.PrimalItemSkin_DinoSantaHat" |
| **Candy_Cane_Club_Skin** | "BlueprintGeneratedClass /Game/PrimalEarth/CoreBlueprints/Items/Armor/Leather/PrimalItemSkin_CandyClub.PrimalItemSkin_CandyClub" |
| **Top_Hat_Skin** | "BlueprintGeneratedClass /Game/PrimalEarth/CoreBlueprints/Items/Armor/Skin/PrimalItemSkin_TopHat.PrimalItemSkin_TopHat" |
| **Megaloceros_Reindeer_Costume** | "BlueprintGeneratedClass /Game/PrimalEarth/CoreBlueprints/Items/Armor/Saddles/PrimalItemCostume_ReindeerStag.PrimalItemCostume_ReindeerStag" |
| **ARK_Wildcard_Admin_Hat_Skin** | "BlueprintGeneratedClass /Game/PrimalEarth/CoreBlueprints/Items/Armor/Leather/PrimalItem_Skin_Account_WildcardAdmin.PrimalItem_Skin_Account_WildcardAdmin" |
| **ARK_Tester_Hat_Skin** | "BlueprintGeneratedClass /Game/PrimalEarth/CoreBlueprints/Items/Armor/Leather/PrimalItem_Skin_Account_GameTester.PrimalItem_Skin_Account_GameTester" |
| **ARK_Dev_Kit_Master_Hat_Skin** | "BlueprintGeneratedClass /Game/PrimalEarth/CoreBlueprints/Items/Armor/Leather/PrimalItem_Skin_Account_DevKitMaster.PrimalItem_Skin_Account_DevKitMaster" |
| **Bunny_Ears_Skin** | "BlueprintGeneratedClass /Game/PrimalEarth/CoreBlueprints/Items/Armor/Skin/PrimalItemSkin_BunnyHat.PrimalItemSkin_BunnyHat" |
| **Dino_Bunny_Ears_Skin** | "BlueprintGeneratedClass /Game/PrimalEarth/CoreBlueprints/Items/Armor/Leather/PrimalItemSkin_DinoBunnyHat.PrimalItemSkin_DinoBunnyHat" |
| **Procoptodon_Bunny_Costume** | "BlueprintGeneratedClass /Game/PrimalEarth/CoreBlueprints/Items/Armor/Saddles/PrimalItemCostume_ProcopBunny.PrimalItemCostume_ProcopBunny" |
| **Bionic_Rex_Skin** | "BlueprintGeneratedClass /Game/PrimalEarth/CoreBlueprints/Items/Armor/Saddles/PrimalItemCostume_BionicRex.PrimalItemCostume_BionicRex" |
| **Dino_Party_Hat_Skin** | "BlueprintGeneratedClass /Game/PrimalEarth/CoreBlueprints/Items/Armor/Leather/PrimalItemSkin_DinoPartyHat.PrimalItemSkin_DinoPartyHat" |
| **Party_Hat_Skin** | "BlueprintGeneratedClass /Game/PrimalEarth/CoreBlueprints/Items/Armor/Skin/PrimalItemSkin_PartyHat.PrimalItemSkin_PartyHat" |
| **Birthday_Suit_Pants_Skin** | "BlueprintGeneratedClass /Game/PrimalEarth/CoreBlueprints/Items/Armor/Leather/PrimalItemSkin_BirthdayPants.PrimalItemSkin_BirthdayPants" |
| **Birthday_Suit_Shirt_Skin** | "BlueprintGeneratedClass /Game/PrimalEarth/CoreBlueprints/Items/Armor/Leather/PrimalItemSkin_BirthdayShirt.PrimalItemSkin_BirthdayShirt" |
| **Fireworks_Rocket_Launcher_Skin** | "BlueprintGeneratedClass /Game/PrimalEarth/CoreBlueprints/Items/Armor/Leather/PrimalItemSkin_RocketLauncherFireworks.PrimalItemSkin_RocketLauncherFireworks" |
| **Torch_Sparkler_Skin** | "BlueprintGeneratedClass /Game/PrimalEarth/CoreBlueprints/Items/Armor/Leather/PrimalItemSkin_TorchSparkler.PrimalItemSkin_TorchSparkler" |


## `Farming` Class

### extends `enum.Enum`

**Path prefix:** `"BlueprintGeneratedClass /Game/PrimalEarth/CoreBlueprints/Items/Consumables`

| Name | Path (Value) |
|------|--------------|
| **Small_Animal_Feces** | /PrimalItemConsumable_DinoPoopSmall.PrimalItemConsumable_DinoPoopSmall" |
| **Berry_Bush_Seeds** |  |
| **Human_Feces** | /PrimalItemConsumable_HumanPoop.PrimalItemConsumable_HumanPoop" |
| **Amarberry_Seed** | /Seeds/PrimalItemConsumable_Seed_Amarberry.PrimalItemConsumable_Seed_Amarberry" |
| **Citronal_Seeds** | /Seeds/PrimalItemConsumable_Seed_Citronal.PrimalItemConsumable_Seed_Citronal" |
| **Amarberry_Seed** | /Seeds/PrimalItemConsumable_Seed_Amarberry.PrimalItemConsumable_Seed_Amarberry" |
| **Azulberry_Seed** | /Seeds/PrimalItemConsumable_Seed_Azulberry.PrimalItemConsumable_Seed_Azulberry" |
| **Tintoberry_Seed** | /Seeds/PrimalItemConsumable_Seed_Tintoberry.PrimalItemConsumable_Seed_Tintoberry" |
| **Narcoberry_Seed** | /Seeds/PrimalItemConsumable_Seed_Narcoberry.PrimalItemConsumable_Seed_Narcoberry" |
| **Stimberry_Seed** | /Seeds/PrimalItemConsumable_Seed_Stimberry.PrimalItemConsumable_Seed_Stimberry" |
| **Mejoberry_Seed** | /Seeds/PrimalItemConsumable_Seed_Mejoberry.PrimalItemConsumable_Seed_Mejoberry" |
| **Citronal_Seed** | /Seeds/PrimalItemConsumable_Seed_Citronal.PrimalItemConsumable_Seed_Citronal" |
| **Savoroot_Seed** | /Seeds/PrimalItemConsumable_Seed_Savoroot.PrimalItemConsumable_Seed_Savoroot" |
| **Longrass_Seed** | /Seeds/PrimalItemConsumable_Seed_Longrass.PrimalItemConsumable_Seed_Longrass" |
| **Rockarrot_Seed** | /Seeds/PrimalItemConsumable_Seed_Rockarrot.PrimalItemConsumable_Seed_Rockarrot" |
| **Medium_Animal_Feces** | /PrimalItemConsumable_DinoPoopMedium.PrimalItemConsumable_DinoPoopMedium" |
| **Large_Animal_Feces** | /PrimalItemConsumable_DinoPoopLarge.PrimalItemConsumable_DinoPoopLarge" |
| **Massive_Animal_Feces** | /PrimalItemConsumable_DinoPoopMassive.PrimalItemConsumable_DinoPoopMassive" |


## `Dye` Class

### extends `enum.Enum`

**Path prefix:** `"BlueprintGeneratedClass /Game/PrimalEarth/CoreBlueprints/Items`

| Name | Path (Value) |
|------|--------------|
| **Red_Coloring** | /PrimalEarthDye_Red.PrimalEarthDye_Red" |
| **Green_Coloring** | /PrimalEarthDye_Green.PrimalEarthDye_Green" |
| **Blue_Coloring** | /PrimalEarthDye_Blue.PrimalEarthDye_Blue" |
| **Yellow_Coloring** | /PrimalEarthDye_Yellow.PrimalEarthDye_Yellow" |
| **Purple_Coloring** | /PrimalEarthDye_Purple.PrimalEarthDye_Purple" |
| **Orange_Coloring** | /PrimalEarthDye_Orange.PrimalEarthDye_Orange" |
| **Black_Coloring** | /PrimalEarthDye_Black.PrimalEarthDye_Black" |
| **White_Coloring** | /PrimalEarthDye_White.PrimalEarthDye_White" |
| **Brown_Coloring** | /PrimalEarthDye_Brown.PrimalEarthDye_Brown" |
| **Cyan_Coloring** | /PrimalEarthDye_Cyan.PrimalEarthDye_Cyan" |
| **Purple_Coloring** | /PrimalEarthDye_Purple.PrimalEarthDye_Purple" |
| **Forest_Coloring** | /PrimalEarthDye_Forest.PrimalEarthDye_Forest" |
| **Parchment_Coloring** | /PrimalEarthDye_Parchment.PrimalEarthDye_Parchment" |
| **Pink_Coloring** | /PrimalEarthDye_Pink.PrimalEarthDye_Pink" |
| **Royalty_Coloring** | /PrimalEarthDye_Royalty.PrimalEarthDye_Royalty" |
| **Silver_Coloring** | /PrimalEarthDye_Silver.PrimalEarthDye_Silver" |
| **Sky_Coloring** | /PrimalEarthDye_Sky.PrimalEarthDye_Sky" |
| **Tan_Coloring** | /PrimalEarthDye_Tan.PrimalEarthDye_Tan" |
| **Tangerine_Coloring** | /PrimalEarthDye_Tangerine.PrimalEarthDye_Tangerine" |
| **Magenta_Coloring** | /PrimalEarthDye_ActuallyMagenta.PrimalEarthDye_ActuallyMagenta" |
| **Brick_Coloring** | /PrimalEarthDye_Brick.PrimalEarthDye_Brick" |
| **Cantaloupe_Coloring** | /PrimalEarthDye_Cantaloupe.PrimalEarthDye_Cantaloupe" |
| **Mud_Coloring** | /PrimalEarthDye_Mud.PrimalEarthDye_Mud" |
| **Navy_Coloring** | /PrimalEarthDye_Navy.PrimalEarthDye_Navy" |
| **Olive_Coloring** | /PrimalEarthDye_Olive.PrimalEarthDye_Olive" |
| **Slate_Coloring** | /PrimalEarthDye_Slate.PrimalEarthDye_Slate" |


## `Ammunition` Class

### extends `enum.Enum`

**Path prefix:** `"BlueprintGeneratedClass /Game/PrimalEarth/CoreBlueprints/Weapons`

| Name | Path (Value) |
|------|--------------|
| **Simple_Bullet** | /PrimalItemAmmo_SimpleBullet.PrimalItemAmmo_SimpleBullet" |
| **Stone_Arrow** | /PrimalItemAmmo_ArrowStone.PrimalItemAmmo_ArrowStone" |
| **C4_Charge** | PrimalItemC4Ammo" |
| **Tranquilizer_Arrow** | /PrimalItemAmmo_ArrowTranq.PrimalItemAmmo_ArrowTranq" |
| **Simple_Rifle_Ammo** | /PrimalItemAmmo_SimpleRifleBullet.PrimalItemAmmo_SimpleRifleBullet" |
| **Advanced_Bullet** | /PrimalItemAmmo_AdvancedBullet.PrimalItemAmmo_AdvancedBullet" |
| **Advanced_Rifle_Bullet** | /PrimalItemAmmo_AdvancedRifleBullet.PrimalItemAmmo_AdvancedRifleBullet" |
| **Rocket_Propelled_Grenade** | /PrimalItemAmmo_Rocket.PrimalItemAmmo_Rocket" |
| **Simple_Shotgun_Ammo** | /PrimalItemAmmo_SimpleShotgunBullet.PrimalItemAmmo_SimpleShotgunBullet" |
| **Transponder_Node** | SAmmo.PrimalItemTransGPSAmmo" |
| **Metal_Arrow** | /PrimalItemAmmo_CompoundBowArrow.PrimalItemAmmo_CompoundBowArrow" |
| **Ballista_Bolt** | /PrimalItemAmmo_BallistaArrow.PrimalItemAmmo_BallistaArrow" |
| **Tranquilizer_Dart** | /PrimalItemAmmo_TranqDart.PrimalItemAmmo_TranqDart" |
| **Advanced_Sniper_Bullet** | /PrimalItemAmmo_AdvancedSniperBullet.PrimalItemAmmo_AdvancedSniperBullet" |
| **Boulder** | /PrimalItemAmmo_Boulder.PrimalItemAmmo_Boulder" |
| **Grappling_Hook** | /PrimalItemAmmo_GrapplingHook.PrimalItemAmmo_GrapplingHook" |
| **Cannon_Ball** | /PrimalItemAmmo_CannonBall.PrimalItemAmmo_CannonBall" |


## `Egg` Class

### extends `enum.Enum`

**Path prefix:** `"BlueprintGeneratedClass /Game/PrimalEarth/Test`

| Name | Path (Value) |
|------|--------------|
| **Stego_Egg** | /PrimalItemConsumable_Egg_Stego.PrimalItemConsumable_Egg_Stego" |
| **Bronto_Egg** | /PrimalItemConsumable_Egg_Bronto.PrimalItemConsumable_Egg_Bronto" |
| **Parasaur_Egg** | /PrimalItemConsumable_Egg_Para.PrimalItemConsumable_Egg_Para" |
| **Raptor_Egg** | /PrimalItemConsumable_Egg_Raptor.PrimalItemConsumable_Egg_Raptor" |
| **Rex_Egg** | /PrimalItemConsumable_Egg_Rex.PrimalItemConsumable_Egg_Rex" |
| **Trike_Egg** | /PrimalItemConsumable_Egg_Trike.PrimalItemConsumable_Egg_Trike" |
| **Dodo_Egg** | /PrimalItemConsumable_Egg_Dodo.PrimalItemConsumable_Egg_Dodo" |
| **Ankylo_Egg** | /PrimalItemConsumable_Egg_Ankylo.PrimalItemConsumable_Egg_Ankylo" |
| **Argentavis_Egg** | /PrimalItemConsumable_Egg_Argent.PrimalItemConsumable_Egg_Argent" |
| **Titanoboa_Egg** | /PrimalItemConsumable_Egg_Boa.PrimalItemConsumable_Egg_Boa" |
| **Carno_Egg** | /PrimalItemConsumable_Egg_Carno.PrimalItemConsumable_Egg_Carno" |
| **Dilo_Egg** | /PrimalItemConsumable_Egg_Dilo.PrimalItemConsumable_Egg_Dilo" |
| **Pteranodon_Egg** | /PrimalItemConsumable_Egg_Ptero.PrimalItemConsumable_Egg_Ptero" |
| **Sarco_Egg** | /PrimalItemConsumable_Egg_Sarco.PrimalItemConsumable_Egg_Sarco" |
| **Pulmonoscorpius_Egg** | /PrimalItemConsumable_Egg_Scorpion.PrimalItemConsumable_Egg_Scorpion" |
| **Araneo_Egg** | /PrimalItemConsumable_Egg_Spider.PrimalItemConsumable_Egg_Spider" |
| **Spino_Egg** | /PrimalItemConsumable_Egg_Spino.PrimalItemConsumable_Egg_Spino" |
| **Turtle_Egg** | /PrimalItemConsumable_Egg_Turtle.PrimalItemConsumable_Egg_Turtle" |
| **Pachycephalosaurus_Egg** | /PrimalItemConsumable_Egg_Pachy.PrimalItemConsumable_Egg_Pachy" |
| **Dimorph_Egg** | /PrimalItemConsumable_Egg_Dimorph.PrimalItemConsumable_Egg_Dimorph" |
| **Quetzal_Egg** | /PrimalItemConsumable_Egg_Quetz.PrimalItemConsumable_Egg_Quetz" |
| **Giganotosaurus_Egg** | /PrimalItemConsumable_Egg_Gigant.PrimalItemConsumable_Egg_Gigant" |
| **Kairuku_Egg** | /PrimalItemConsumable_Egg_Kairuku.PrimalItemConsumable_Egg_Kairuku" |
| **Oviraptor_Egg** | /PrimalItemConsumable_Egg_Oviraptor.PrimalItemConsumable_Egg_Oviraptor" |
| **Dimetrodon_Egg** | /PrimalItemConsumable_Egg_Dimetrodon.PrimalItemConsumable_Egg_Dimetrodon" |
| **Terror_Bird_Egg** | /PrimalItemConsumable_Egg_TerrorBird.PrimalItemConsumable_Egg_TerrorBird" |


## `Structure` Class

### extends `enum.Enum`

**Path prefix:** `"BlueprintGeneratedClass /Game/PrimalEarth/CoreBlueprints/Items/Structures`

| Name | Path (Value) |
|------|--------------|
| **Campfire** | /PrimalItemStructure_Campfire.PrimalItemStructure_Campfire" |
| **Standing_Torch** | /Misc/PrimalItemStructure_StandingTorch.PrimalItemStructure_StandingTorch" |
| **Hide_Sleeping_Bag** | /PrimalItemStructure_SleepingBag_Hide.PrimalItemStructure_SleepingBag_Hide" |
| **Thatch_Roof** | /Thatch/PrimalItemStructure_ThatchCeiling.PrimalItemStructure_ThatchCeiling" |
| **Thatch_Door** | /Thatch/PrimalItemStructure_ThatchDoor.PrimalItemStructure_ThatchDoor" |
| **Thatch_Foundation** | /Thatch/PrimalItemStructure_ThatchFloor.PrimalItemStructure_ThatchFloor" |
| **Thatch_Wall** | /Thatch/PrimalItemStructure_ThatchWall.PrimalItemStructure_ThatchWall" |
| **Thatch_Doorframe** | /Thatch/PrimalItemStructure_ThatchWallWithDoor.PrimalItemStructure_ThatchWallWithDoor" |
| **Wooden_Catwalk** | /Wooden/PrimalItemStructure_WoodCatwalk.PrimalItemStructure_WoodCatwalk" |
| **Wooden_Ceiling** | /Wooden/PrimalItemStructure_WoodCeiling.PrimalItemStructure_WoodCeiling" |
| **Wooden_Hatchframe** | /Wooden/PrimalItemStructure_WoodCeilingWithTrapdoor.PrimalItemStructure_WoodCeilingWithTrapdoor" |
| **Wooden_Door** | /Wooden/PrimalItemStructure_WoodDoor.PrimalItemStructure_WoodDoor" |
| **Wooden_Foundation** | /Wooden/PrimalItemStructure_WoodFloor.PrimalItemStructure_WoodFloor" |
| **Wooden_Ladder** | /Wooden/PrimalItemStructure_WoodLadder.PrimalItemStructure_WoodLadder" |
| **Wooden_Pillar** | /Wooden/PrimalItemStructure_WoodPillar.PrimalItemStructure_WoodPillar" |
| **Wooden_Ramp** | /Wooden/PrimalItemStructure_WoodRamp.PrimalItemStructure_WoodRamp" |
| **Wooden_Trapdoor** | /Wooden/PrimalItemStructure_WoodTrapdoor.PrimalItemStructure_WoodTrapdoor" |
| **Wooden_Wall** | /Wooden/PrimalItemStructure_WoodWall.PrimalItemStructure_WoodWall" |
| **Wooden_Doorframe** | /Wooden/PrimalItemStructure_WoodWallWithDoor.PrimalItemStructure_WoodWallWithDoor" |
| **Wooden_Windowframe** | /Wooden/PrimalItemStructure_WoodWallWithWindow.PrimalItemStructure_WoodWallWithWindow" |
| **Wooden_Window** | /Wooden/PrimalItemStructure_WoodWindow.PrimalItemStructure_WoodWindow" |
| **Wooden_Sign** | /Wooden/PrimalItemStructure_WoodSign.PrimalItemStructure_WoodSign" |
| **Storage_Box** | /Misc/PrimalItemStructure_StorageBox_Small.PrimalItemStructure_StorageBox_Small" |
| **Large_Storage_Box** | /Misc/PrimalItemStructure_StorageBox_Large.PrimalItemStructure_StorageBox_Large" |
| **Mortar_And_Pestle** | /Misc/PrimalItemStructure_MortarAndPestle.PrimalItemStructure_MortarAndPestle" |
| **Stone_Irrigation_Pipe___Intake** | /Pipes/PrimalItemStructure_StonePipeIntake.PrimalItemStructure_StonePipeIntake" |
| **Stone_Irrigation_Pipe___Straight** | /Pipes/PrimalItemStructure_StonePipeStraight.PrimalItemStructure_StonePipeStraight" |
| **Stone_Irrigation_Pipe___Inclined** | /Pipes/PrimalItemStructure_StonePipeIncline.PrimalItemStructure_StonePipeIncline" |
| **Stone_Irrigation_Pipe___Intersection** | /Pipes/PrimalItemStructure_StonePipeIntersection.PrimalItemStructure_StonePipeIntersection" |
| **Stone_Irrigation_Pipe___Vertical** | /Pipes/PrimalItemStructure_StonePipeVertical.PrimalItemStructure_StonePipeVertical" |
| **Stone_Irrigation_Pipe___Tap** | /Pipes/PrimalItemStructure_StonePipeTap.PrimalItemStructure_StonePipeTap" |
| **Refining_Forge** | /Misc/PrimalItemStructure_Forge.PrimalItemStructure_Forge" |
| **Smithy** | /Misc/PrimalItemStructure_AnvilBench.PrimalItemStructure_AnvilBench" |
| **Compost_Bin** | /Misc/PrimalItemStructure_CompostBin.PrimalItemStructure_CompostBin" |
| **Cooking_Pot** | /Misc/PrimalItemStructure_CookingPot.PrimalItemStructure_CookingPot" |
| **Simple_Bed** | /Misc/PrimalItemStructure_Bed_Simple.PrimalItemStructure_Bed_Simple" |
| **Small_Crop_Plot** | /Misc/PrimalItemStructure_CropPlot_Small.PrimalItemStructure_CropPlot_Small" |
| **Wooden_Fence_Foundation** | /Wooden/PrimalItemStructure_WoodFenceFoundation.PrimalItemStructure_WoodFenceFoundation" |
| **Dinosaur_Gateway** | /Wooden/PrimalItemStructure_WoodGateframe.PrimalItemStructure_WoodGateframe" |
| **Dinosaur_Gate** | /Wooden/PrimalItemStructure_WoodGate.PrimalItemStructure_WoodGate" |
| **Metal_Catwalk** | /Metal/PrimalItemStructure_MetalCatwalk.PrimalItemStructure_MetalCatwalk" |
| **Metal_Ceiling** | /Metal/PrimalItemStructure_MetalCeiling.PrimalItemStructure_MetalCeiling" |
| **Metal_Hatchframe** | /Metal/PrimalItemStructure_MetalCeilingWithTrapdoor.PrimalItemStructure_MetalCeilingWithTrapdoor" |
| **Metal_Door** | /Metal/PrimalItemStructure_MetalDoor.PrimalItemStructure_MetalDoor" |
| **Metal_Fence_Foundation** | /Metal/PrimalItemStructure_MetalFenceFoundation.PrimalItemStructure_MetalFenceFoundation" |
| **Metal_Foundation** | /Metal/PrimalItemStructure_MetalFloor.PrimalItemStructure_MetalFloor" |
| **Behemoth_Gate** | /Metal/PrimalItemStructure_MetalGate_Large.PrimalItemStructure_MetalGate_Large" |
| **Behemoth_Gateway** | /Metal/PrimalItemStructure_MetalGateframe_Large.PrimalItemStructure_MetalGateframe_Large" |
| **Metal_Ladder** | /Metal/PrimalItemStructure_MetalLadder.PrimalItemStructure_MetalLadder" |
| **Metal_Pillar** | /Metal/PrimalItemStructure_MetalPillar.PrimalItemStructure_MetalPillar" |
| **Metal_Ramp** | /Metal/PrimalItemStructure_MetalRamp.PrimalItemStructure_MetalRamp" |
| **Metal_Trapdoor** | /Metal/PrimalItemStructure_MetalTrapdoor.PrimalItemStructure_MetalTrapdoor" |
| **Metal_Wall** | /Metal/PrimalItemStructure_MetalWall.PrimalItemStructure_MetalWall" |
| **Metal_Doorframe** | /Metal/PrimalItemStructure_MetalWallWithDoor.PrimalItemStructure_MetalWallWithDoor" |
| **Metal_Windowframe** | /Metal/PrimalItemStructure_MetalWallWithWindow.PrimalItemStructure_MetalWallWithWindow" |
| **Metal_Window** | /Metal/PrimalItemStructure_MetalWindow.PrimalItemStructure_MetalWindow" |
| **Fabricator** | /Misc/PrimalItemStructure_Fabricator.PrimalItemStructure_Fabricator" |
| **Water_Tank** | /Pipes/PrimalItemStructure_WaterTank.PrimalItemStructure_WaterTank" |
| **Air_Conditioner** | /Misc/PrimalItemStructure_AirConditioner.PrimalItemStructure_AirConditioner" |
| **Electrical_Generator** | /Pipes/PrimalItemStructure_PowerGenerator.PrimalItemStructure_PowerGenerator" |
| **Electrical_Outlet** | /Pipes/PrimalItemStructure_PowerOutlet.PrimalItemStructure_PowerOutlet" |
| **Inclined_Electrical_Cable** | /Pipes/PrimalItemStructure_PowerCableIncline.PrimalItemStructure_PowerCableIncline" |
| **Electrical_Cable_Intersection** | /Pipes/PrimalItemStructure_PowerCableIntersection.PrimalItemStructure_PowerCableIntersection" |
| **Straight_Electrical_Cable** | /Pipes/PrimalItemStructure_PowerCableStraight.PrimalItemStructure_PowerCableStraight" |
| **Vertical_Electrical_Cable** | /Pipes/PrimalItemStructure_PowerCableVertical.PrimalItemStructure_PowerCableVertical" |
| **Lamppost** | /Misc/PrimalItemStructure_Lamppost.PrimalItemStructure_Lamppost" |
| **Refrigerator** | /Misc/PrimalItemStructure_IceBox.PrimalItemStructure_IceBox" |
| **Auto_Turret** | /Misc/PrimalItemStructure_Turret.PrimalItemStructure_Turret" |
| **Remote_Keypad** | /Misc/PrimalItemStructure_Keypad.PrimalItemStructure_Keypad" |
| **Metal_Irrigation_Pipe___Inclined** | /Pipes/PrimalItemStructure_MetalPipeIncline.PrimalItemStructure_MetalPipeIncline" |
| **Metal_Irrigation_Pipe___TapIntake** | /Pipes/PrimalItemStructure_MetalPipeIntake.PrimalItemStructure_MetalPipeIntake" |
| **Metal_Irrigation_Pipe___Intersection** | /Pipes/PrimalItemStructure_MetalPipeIntersection.PrimalItemStructure_MetalPipeIntersection" |
| **Metal_Irrigation_Pipe___Straight** | /Pipes/PrimalItemStructure_MetalPipeStraight.PrimalItemStructure_MetalPipeStraight" |
| **Metal_Irrigation_Pipe___Tap** | /Pipes/PrimalItemStructure_MetalPipeTap.PrimalItemStructure_MetalPipeTap" |
| **Metal_Irrigation_Pipe___Vertical** | /Pipes/PrimalItemStructure_MetalPipeVertical.PrimalItemStructure_MetalPipeVertical" |
| **Metal_Sign** | /Metal/PrimalItemStructure_MetalSign.PrimalItemStructure_MetalSign" |
| **Wooden_Billboard** | /Wooden/PrimalItemStructure_WoodSign_Large.PrimalItemStructure_WoodSign_Large" |
| **Metal_Billboard** | /Metal/PrimalItemStructure_MetalSign_Large.PrimalItemStructure_MetalSign_Large" |
| **Medium_Crop_Plot** | /Misc/PrimalItemStructure_CropPlot_Medium.PrimalItemStructure_CropPlot_Medium" |
| **Large_Crop_Plot** | /Misc/PrimalItemStructure_CropPlot_Large.PrimalItemStructure_CropPlot_Large" |
| **Wooden_Wall_Sign** | /Wooden/PrimalItemStructure_WoodSign_Wall.PrimalItemStructure_WoodSign_Wall" |
| **Metal_Dinosaur_Gateway** | /Metal/PrimalItemStructure_MetalGateframe.PrimalItemStructure_MetalGateframe" |
| **Metal_Dinosaur_Gate** | /Metal/PrimalItemStructure_MetalGate.PrimalItemStructure_MetalGate" |
| **Metal_Wall_Sign** | /Metal/PrimalItemStructure_MetalSign_Wall.PrimalItemStructure_MetalSign_Wall" |
| **Multi_Panel_Flag** | /Misc/PrimalItemStructure_Flag.PrimalItemStructure_Flag" |
| **Spider_Flag** | /Misc/PrimalItemStructure_Flag_Spider.PrimalItemStructure_Flag_Spider" |
| **Preserving_Bin** | /Misc/PrimalItemStructure_PreservingBin.PrimalItemStructure_PreservingBin" |
| **Metal_Spike_Wall** | /Metal/PrimalItemStructure_MetalSpikeWall.PrimalItemStructure_MetalSpikeWall" |
| **Vault** | /Misc/PrimalItemStructure_StorageBox_Huge.PrimalItemStructure_StorageBox_Huge" |
| **Wooden_Spike_Wall** | /Wooden/PrimalItemStructure_WoodSpikeWall.PrimalItemStructure_WoodSpikeWall" |
| **Bookshelf** | /Misc/PrimalItemStructure_Bookshelf.PrimalItemStructure_Bookshelf" |
| **Stone_Fence_Foundation** | /Stone/PrimalItemStructure_StoneFenceFoundation.PrimalItemStructure_StoneFenceFoundation" |
| **Stone_Wall** | /Stone/PrimalItemStructure_StoneWall.PrimalItemStructure_StoneWall" |
| **Metal_Water_Reservoir** | /Pipes/PrimalItemStructure_WaterTankMetal.PrimalItemStructure_WaterTankMetal" |
| **Stone_Ceiling** | /Stone/PrimalItemStructure_StoneCeiling.PrimalItemStructure_StoneCeiling" |
| **Stone_Hatchframe** | /Stone/PrimalItemStructure_StoneCeilingWithTrapdoor.PrimalItemStructure_StoneCeilingWithTrapdoor" |
| **Reinforced_Wooden_Door** | /Stone/PrimalItemStructure_StoneDoor.PrimalItemStructure_StoneDoor" |
| **Stone_Foundation** | /Stone/PrimalItemStructure_StoneFloor.PrimalItemStructure_StoneFloor" |
| **Reinforced_Dinosaur_Gate** | /Stone/PrimalItemStructure_StoneGate.PrimalItemStructure_StoneGate" |
| **Stone_Dinosaur_Gateway** | /Stone/PrimalItemStructure_StoneGateframe.PrimalItemStructure_StoneGateframe" |
| **Stone_Pillar** | /Stone/PrimalItemStructure_StonePillar.PrimalItemStructure_StonePillar" |
| **Stone_Doorframe** | /Stone/PrimalItemStructure_StoneWallWithDoor.PrimalItemStructure_StoneWallWithDoor" |
| **Stone_Windowframe** | /Stone/PrimalItemStructure_StoneWallWithWindow.PrimalItemStructure_StoneWallWithWindow" |
| **Reinforced_Window** | /Wooden/PrimalItemStructure_StoneWindow.PrimalItemStructure_StoneWindow" |
| **Reinforced_Trapdoor** | /Wooden/PrimalItemStructure_StoneTrapdoor.PrimalItemStructure_StoneTrapdoor" |
| **Omnidirectional_lamppost** | /Misc/PrimalItemStructure_LamppostOmni.PrimalItemStructure_LamppostOmni" |
| **Industrial_Grill** | /Misc/PrimalItemStructure_Grill.PrimalItemStructure_Grill" |
| **Single_Panel_Flag** | /Misc/PrimalItemStructure_Flag_Single.PrimalItemStructure_Flag_Single" |
| **Feeding_Trough** | /Misc/PrimalItemStructure_FeedingTrough.PrimalItemStructure_FeedingTrough" |
| **Behemoth_Stone_Dinosaur_Gateway** | /Stone/PrimalItemStructure_StoneGateframe_Large.PrimalItemStructure_StoneGateframe_Large" |
| **Behemoth_Reinforced_Dinosaur_Gate** | /Stone/PrimalItemStructure_StoneGateLarge.PrimalItemStructure_StoneGateLarge" |
| **Sloped_Thatch_Roof** | /Roofs/Thatch/PrimalItemStructure_ThatchRoof.PrimalItemStructure_ThatchRoof" |
| **Sloped_Thatch_Wall_Left** | /Roofs/Thatch/PrimalItemStructure_ThatchWall_Sloped_Left.PrimalItemStructure_ThatchWall_Sloped_Left" |
| **Sloped_Thatch_Wall_Right** | /Roofs/Thatch/PrimalItemStructure_ThatchWall_Sloped_Right.PrimalItemStructure_ThatchWall_Sloped_Right" |
| **Wooden_Roof** | /Roofs/Wood/PrimalItemStructure_WoodRoof.PrimalItemStructure_WoodRoof" |
| **Sloped_Wood_Wall_Left** | /Roofs/Wood/PrimalItemStructure_WoodWall_Sloped_Left.PrimalItemStructure_WoodWall_Sloped_Left" |
| **Sloped_Wood_Wall_Right** | /Roofs/Wood/PrimalItemStructure_WoodWall_Sloped_Right.PrimalItemStructure_WoodWall_Sloped_Right" |
| **Stone_Roof** | /Roofs/Stone/PrimalItemStructure_StoneRoof.PrimalItemStructure_StoneRoof" |
| **Sloped_Stone_Wall_Left** | /Roofs/Stone/PrimalItemStructure_StoneWall_Sloped_Left.PrimalItemStructure_StoneWall_Sloped_Left" |
| **Sloped_Stone_Wall_Right** | /Roofs/Stone/PrimalItemStructure_StoneWall_Sloped_Right.PrimalItemStructure_StoneWall_Sloped_Right" |
| **Metal_Roof** | /Roofs/Metal/PrimalItemStructure_MetalRoof.PrimalItemStructure_MetalRoof" |
| **Sloped_Metal_Wall_Left** | /Roofs/Metal/PrimalItemStructure_MetalWall_Sloped_Left.PrimalItemStructure_MetalWall_Sloped_Left" |
| **Sloped_Metal_Wall_Right** | /Roofs/Metal/PrimalItemStructure_MetalWall_Sloped_Right.PrimalItemStructure_MetalWall_Sloped_Right" |
| **Wooden_Raft** | lItemRaft" |
| **Dune_Buggy_Vehicle_Test** | malItemVHBuggy.PrimalItemVHBuggy" |
| **Painting_Canvas** | /Misc/PrimalItemStructure_PaintingCanvas.PrimalItemStructure_PaintingCanvas" |
| **Greenhouse_Wall** | /Greenhouse/PrimalItemStructure_GreenhouseWall.PrimalItemStructure_GreenhouseWall" |
| **Greenhouse_Ceiling** | /Greenhouse/PrimalItemStructure_GreenhouseCeiling.PrimalItemStructure_GreenhouseCeiling" |
| **Greenhouse_Doorframe** | /Greenhouse/PrimalItemStructure_GreenhouseWallWithDoor.PrimalItemStructure_GreenhouseWallWithDoor" |
| **Greenhouse_Door** | /Greenhouse/PrimalItemStructure_GreenhouseDoor.PrimalItemStructure_GreenhouseDoor" |
| **Sloped_Greenhouse_Wall_Left** | /Greenhouse/PrimalItemStructure_GreenhouseWall_Sloped_Left.PrimalItemStructure_GreenhouseWall_Sloped_Left" |
| **Sloped_Greenhouse_Wall_Right** | /Greenhouse/PrimalItemStructure_GreenhouseWall_Sloped_Right.PrimalItemStructure_GreenhouseWall_Sloped_Right" |
| **Sloped_Greenhouse_Roof** | /Greenhouse/PrimalItemStructure_GreenhouseRoof.PrimalItemStructure_GreenhouseRoof" |
| **Greenhouse_Window** | /Greenhouse/PrimalItemStructure_GreenhouseWindow.PrimalItemStructure_GreenhouseWindow" |
| **Elevator_Track** | /BuildingBases/PrimalItemStructure_ElevatorTrackBase.PrimalItemStructure_ElevatorTrackBase" |
| **Small_Elevator_Platform** | /BuildingBases/PrimalItemStructure_ElevatorPlatformSmall.PrimalItemStructure_ElevatorPlatformSmall" |
| **Medium_Elevator_Platform** | /BuildingBases/PrimalItemStructure_ElevatorPlatfromMedium.PrimalItemStructure_ElevatorPlatfromMedium" |
| **Large_Elevator_Platform** | /BuildingBases/PrimalItemStructure_ElevatorPlatformLarge.PrimalItemStructure_ElevatorPlatformLarge" |
| **Ballista_Turret** | /Misc/PrimalItemStructure_TurretBallista.PrimalItemStructure_TurretBallista" |
| **Wooden_Chair** | /Wooden/PrimalItemStructure_Furniture_WoodChair.PrimalItemStructure_Furniture_WoodChair" |
| **Wooden_Bench** | /Wooden/PrimalItemStructure_Furniture_WoodBench.PrimalItemStructure_Furniture_WoodBench" |
| **Basic_Gravestone** | /Wooden/PrimalItemStructure_Furniture_Gravestone.PrimalItemStructure_Furniture_Gravestone" |
| **Trophy_Base** | /Misc/PrimalItemStructure_TrophyBase.PrimalItemStructure_TrophyBase" |
| **Survival_of_the_Fittest_Trophy__1st_Place** | rimalItemTrophy_SotF_1st.PrimalItemTrophy_SotF_1st" |
| **Survival_of_the_Fittest_Trophy__2nd_Place** | rimalItemTrophy_SotF_2nd.PrimalItemTrophy_SotF_2nd" |
| **Survival_of_the_Fittest_Trophy__3rd_Place** | rimalItemTrophy_SotF_3rd.PrimalItemTrophy_SotF_3rd" |
| **SotF__Unnatural_Selection_Trophy__1st_Place** | rimalItemTrophy_SotFUS_1st.PrimalItemTrophy_SotFUS_1st" |
| **SotF__Unnatural_Selection_Trophy__2nd_Place** | rimalItemTrophy_SotFUS_2nd.PrimalItemTrophy_SotFUS_2nd" |
| **SotF__Unnatural_Selection_Trophy__3rd_Place** | rimalItemTrophy_SotFUS_3rd.PrimalItemTrophy_SotFUS_3rd" |
| **SotF__The_Last_Stand_Trophy__1st_Place** |  |
| **SotF__The_Last_Stand_Trophy__2nd_Place** |  |
| **SotF__The_Last_Stand_Trophy__3rd_Place** |  |
| **Wardrums** | /Wooden/PrimalItemStructure_Wardrums.PrimalItemStructure_Wardrums" |
| **War_Map** | /Wooden/PrimalItemStructure_WarMap.PrimalItemStructure_WarMap" |
| **Wooden_Railing** | /Wooden/PrimalItemStructure_WoodRailing.PrimalItemStructure_WoodRailing" |
| **Stone_Railing** | /Stone/PrimalItemStructure_StoneRailing.PrimalItemStructure_StoneRailing" |
| **Metal_Railing** | /Metal/PrimalItemStructure_MetalRailing.PrimalItemStructure_MetalRailing" |
| **Pumpkin** | /halloween/PrimalItemStructure_Pumpkin.PrimalItemStructure_Pumpkin" |
| **Scarecrow** | /halloween/PrimalItemStructure_Scarecrow.PrimalItemStructure_Scarecrow" |
| **Trophy_Wall_Mount** | /Misc/PrimalItemStructure_TrophyWall.PrimalItemStructure_TrophyWall" |
| **Minigun_Turret** | /Misc/PrimalItemStructure_TurretMinigun.PrimalItemStructure_TurretMinigun" |
| **Catapult_Turret** | /Misc/PrimalItemStructure_TurretCatapult.PrimalItemStructure_TurretCatapult" |
| **Rocket_Turret** | /Misc/PrimalItemStructure_TurretRocket.PrimalItemStructure_TurretRocket" |
| **Homing_Underwater_Mine** | /Misc/PrimalItemStructure_SeaMine.PrimalItemStructure_SeaMine" |
| **Wall_Torch** | /Misc/PrimalItemStructure_WallTorch.PrimalItemStructure_WallTorch" |
| **Industrial_Forge** | /Misc/PrimalItemStructure_IndustrialForge.PrimalItemStructure_IndustrialForge" |
| **Industrial_Cooker** | /Misc/PrimalItemStructure_IndustrialCookingPot.PrimalItemStructure_IndustrialCookingPot" |
| **Bunk_Bed** | /Misc/PrimalItemStructure_Bed_Modern.PrimalItemStructure_Bed_Modern" |
| **Wooden_Table** | /Wooden/PrimalItemStructure_Furniture_WoodTable.PrimalItemStructure_Furniture_WoodTable" |
| **Stone_Fireplace** | /Misc/PrimalItemStructure_Fireplace.PrimalItemStructure_Fireplace" |
| **Wooden_Cage** | /Wooden/PrimalItemStructure_WoodCage.PrimalItemStructure_WoodCage" |
| **Wreath** | /Christmas/PrimalItemStructure_Wreath.PrimalItemStructure_Wreath" |
| **Holiday_Tree** | /Christmas/PrimalItemStructure_ChristmasTree.PrimalItemStructure_ChristmasTree" |
| **Holiday_Lights** | /Christmas/PrimalItemStructure_XmasLights.PrimalItemStructure_XmasLights" |
| **Snowman** | /Christmas/PrimalItemStructure_Snowman.PrimalItemStructure_Snowman" |
| **Holiday_Stocking** | /Christmas/PrimalItemStructure_Stocking.PrimalItemStructure_Stocking" |
| **Gift_Box** | /Christmas/PrimalItemStructure_StorageBox_ChristmasGift.PrimalItemStructure_StorageBox_ChristmasGift" |
| **Beer_Barrel** | /Misc/PrimalItemStructure_BeerBarrel.PrimalItemStructure_BeerBarrel" |
| **Bunny_Egg** | /Halloween/PrimalItemStructure_EasterEgg.PrimalItemStructure_EasterEgg" |
| **Chemistry_Bench** | /Misc/PrimalItemStructure_ChemBench.PrimalItemStructure_ChemBench" |
| **Primitive_Cannon** | /Misc/PrimalItemStructure_Cannon.PrimalItemStructure_Cannon" |
| **Gorilla_Flag** | /Misc/PrimalItemStructure_Flag_Gorilla.PrimalItemStructure_Flag_Gorilla" |
| **Dragon_Flag** | /Misc/PrimalItemStructure_Flag_Dragon.PrimalItemStructure_Flag_Dragon" |
| **Training_Dummy** | /Halloween/PrimalItemStructure_TrainingDummy.PrimalItemStructure_TrainingDummy" |
| **Rope_Ladder** | /Wooden/PrimalItemStructure_RopeLadder.PrimalItemStructure_RopeLadder" |
| **Wooden_Tree_Platform** | /Wooden/PrimalItemStructure_TreePlatform_Wood.PrimalItemStructure_TreePlatform_Wood" |
| **Metal_Tree_Platform** | /Wooden/PrimalItemStructure_TreePlatform_Metal.PrimalItemStructure_TreePlatform_Metal" |
| **Tree_Sap_Tap** | /Pipes/PrimalItemStructure_TreeTap.PrimalItemStructure_TreeTap" |


