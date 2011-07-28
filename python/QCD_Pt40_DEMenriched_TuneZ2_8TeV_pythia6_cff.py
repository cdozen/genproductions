import FWCore.ParameterSet.Config as cms
 
source = cms.Source("EmptySource")
 
 
from Configuration.Generator.PythiaUEZ2Settings_cfi import *
 
generator = cms.EDFilter("Pythia6GeneratorFilter",
                   pythiaHepMCVerbosity = cms.untracked.bool(False),
                   maxEventsToPrint = cms.untracked.int32(0),
                   pythiaPylistVerbosity = cms.untracked.int32(0),
                   filterEfficiency = cms.untracked.double(0.00196),
                   comEnergy = cms.double(8000.0),
                   crossSection = cms.untracked.double(2.37e+07),
     PythiaParameters = cms.PSet(
            pythiaUESettingsBlock,
            processParameters = cms.vstring(
            'MSEL=1',
            'CKIN(3)=40.          ! minimum pt hat for hard interactions', 
            'CKIN(4)=-1          ! maximum pt hat for hard interactions'),
 
 
 
 
 
            parameterSets = cms.vstring('pythiaUESettings',
                       'processParameters')
                   )
)

gj_filter = cms.EDFilter("PythiaFilterGammaGamma",
    PtSeedThr = cms.untracked.double(5.0),
    EtaSeedThr = cms.untracked.double(2.8),
    PtGammaThr = cms.untracked.double(0.0),
    EtaGammaThr = cms.untracked.double(2.8),
    PtElThr = cms.untracked.double(2.0),
    EtaElThr = cms.untracked.double(2.8),
    dRSeedMax = cms.untracked.double(0.0),
    dPhiSeedMax = cms.untracked.double(0.2),
    dEtaSeedMax = cms.untracked.double(0.12),
    dRNarrowCone = cms.untracked.double(0.02),
    PtTkThr = cms.untracked.double(1.6),
    EtaTkThr = cms.untracked.double(2.2),
    dRTkMax = cms.untracked.double(0.2),
    PtMinCandidate1 = cms.untracked.double(15.),
    PtMinCandidate2 = cms.untracked.double(15.),
    EtaMaxCandidate = cms.untracked.double(3.0),
    NTkConeMax = cms.untracked.int32(2),
    NTkConeSum = cms.untracked.int32(4),
    InvMassWide = cms.untracked.double(80.0),
    InvMassNarrow = cms.untracked.double(14000.0),
    AcceptPrompts = cms.untracked.bool(True),
    PromptPtThreshold = cms.untracked.double(15.0)                     
 
)
 
ProductionFilterSequence = cms.Sequence(generator*gj_filter)

 
