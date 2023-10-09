import FWCore.ParameterSet.Config as cms

from Configuration.Eras.Era_Run3_2023_cff import Run3_2023
from Configuration.Eras.Modifier_highBetaStar_2023_cff import highBetaStar_2023

Run3_2023_highBetaStar = cms.ModifierChain(Run3_2023, highBetaStar_2023)