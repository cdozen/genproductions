# Auto generated configuration file
# using: 
# Revision: 1.77.2.1 
# Source: /cvs_server/repositories/CMSSW/CMSSW/Configuration/PyReleaseValidation/python/ConfigBuilder.py,v 
# with command line options: Configuration/GenProduction/python/Herwigpp_QCD_Pt_1400.py -s GEN,SIM,DIGI,L1,DIGI2RAW,HLT --eventcontent RAWSIM --datatier GEN-SIM-RAW --conditions FrontierConditions_GlobalTag,IDEAL_V9::All -n 10 --no_exec --customise Configuration/GenProduction/Herwigpp_custom.py
import FWCore.ParameterSet.Config as cms

process = cms.Process('HLT')

# import of standard configurations
process.load('Configuration/StandardSequences/Services_cff')
process.load('FWCore/MessageService/MessageLogger_cfi')
process.load('Configuration/StandardSequences/MixingNoPileUp_cff')
process.load('Configuration/StandardSequences/GeometryPilot2_cff')
process.load('Configuration/StandardSequences/MagneticField_38T_cff')
process.load('Configuration/StandardSequences/Generator_cff')
process.load('Configuration/StandardSequences/VtxSmearedEarly10TeVCollision_cff')
process.load('Configuration/StandardSequences/Sim_cff')
process.load('Configuration/StandardSequences/Digi_cff')
process.load('Configuration/StandardSequences/SimL1Emulator_cff')
process.load('L1TriggerConfig/L1GtConfigProducers/Luminosity/lumi1030.L1Menu2008_2E30_Unprescaled_cff')
process.load('Configuration/StandardSequences/DigiToRaw_cff')
process.load('HLTrigger/Configuration/HLT_2E30_cff')
process.load('Configuration/StandardSequences/FrontierConditions_GlobalTag_cff')
process.load('Configuration/EventContent/EventContent_cff')

process.configurationMetadata = cms.untracked.PSet(
    version = cms.untracked.string('$Revision: 1.1 $'),
    annotation = cms.untracked.string('Summer08 CSA: Herwig++ generation of QCD events, MRST2001 used, MinKT=1400 GeV'),
    name = cms.untracked.string('$Source: /cvs_server/repositories/CMSSW/CMSSW/Configuration/GenProduction/python/Herwigpp_mkrun.template,v $')
)
process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(10)
)
process.options = cms.untracked.PSet(
    Rethrow = cms.untracked.vstring('ProductNotFound')
)
# Input source
process.source = cms.Source("ThePEGSource",
    cm10TeV = cms.vstring('set /Herwig/Generators/LHCGenerator:EventHandler:LuminosityFunction:Energy 10000.0', 
        'set /Herwig/Shower/Evolver:IntrinsicPtGaussian 2.1*GeV'),
    run = cms.string('LHC'),
    repository = cms.string('HerwigDefaults.rpo'),
    QCDCSAParameters = cms.vstring('cd /Herwig/MatrixElements/', 
        'insert SimpleQCD:MatrixElements[0] MEQCD2to2', 
        'cd /', 
        'set /Herwig/Cuts/JetKtCut:MinKT 1400*GeV', 
        'set /Herwig/UnderlyingEvent/MPIHandler:Algorithm 1'),
    dataLocation = cms.string('${HERWIGPATH}'),
    filterEfficiency = cms.untracked.double(1.0),
    configFiles = cms.vstring(),
    disableCtau10mmDecays = cms.vstring('cd /Herwig/Particles', 
        'set K-/K-->nu_ebar,e-;:OnOff Off', 
        'set K+/K+->nu_e,e+;:OnOff Off', 
        'set K-/K-->nu_mubar,mu-;:OnOff Off', 
        'set K+/K+->nu_mu,mu+;:OnOff Off', 
        'set K-/K-->pi0,nu_ebar,e-;:OnOff Off', 
        'set K+/K+->pi0,nu_e,e+;:OnOff Off', 
        'set K-/K-->pi0,nu_mubar,mu-;:OnOff Off', 
        'set K+/K+->pi0,nu_mu,mu+;:OnOff Off', 
        'set K-/K-->pi0,pi0,nu_ebar,e-;:OnOff Off', 
        'set K+/K+->pi0,pi0,nu_e,e+;:OnOff Off', 
        'set K-/K-->pi-,gamma,gamma;:OnOff Off', 
        'set K+/K+->pi+,gamma,gamma;:OnOff Off', 
        'set K-/K-->pi-,pi0;:OnOff Off', 
        'set K+/K+->pi+,pi0;:OnOff Off', 
        'set K-/K-->pi-,pi0,pi0;:OnOff Off', 
        'set K+/K+->pi+,pi0,pi0;:OnOff Off', 
        'set K-/K-->pi+,pi-,nu_ebar,e-;:OnOff Off', 
        'set K+/K+->pi+,pi-,nu_e,e+;:OnOff Off', 
        'set K-/K-->pi+,pi-,nu_mubar,mu-;:OnOff Off', 
        'set K+/K+->pi+,pi-,nu_mu,mu+;:OnOff Off', 
        'set K-/K-->pi+,pi-,pi-;:OnOff Off', 
        'set K+/K+->pi+,pi+,pi-;:OnOff Off', 
        'set K_L0/K_L0->gamma,e-,e+;:OnOff Off', 
        'set K_L0/K_L0->gamma,gamma;:OnOff Off', 
        'set K_L0/K_L0->pi0,gamma,gamma;:OnOff Off', 
        'set K_L0/K_L0->pi0,pi0;:OnOff Off', 
        'set K_L0/K_L0->pi0,pi0,pi0;:OnOff Off', 
        'set K_L0/K_L0->pi+,nu_ebar,e-;:OnOff Off', 
        'set K_L0/K_L0->pi-,nu_e,e+;:OnOff Off', 
        'set K_L0/K_L0->pi+,nu_mubar,mu-;:OnOff Off', 
        'set K_L0/K_L0->pi-,nu_mu,mu+;:OnOff Off', 
        'set K_L0/K_L0->pi+,pi0,nu_ebar,e-;:OnOff Off', 
        'set K_L0/K_L0->pi-,pi0,nu_e,e+;:OnOff Off', 
        'set K_L0/K_L0->pi+,pi-;:OnOff Off', 
        'set K_L0/K_L0->pi+,pi-,pi0;:OnOff Off', 
        'set K_S0/K_S0->gamma,gamma;:OnOff Off', 
        'set K_S0/K_S0->pi0,pi0;:OnOff Off', 
        'set K_S0/K_S0->pi+,nu_ebar,e-;:OnOff Off', 
        'set K_S0/K_S0->pi-,nu_e,e+;:OnOff Off', 
        'set K_S0/K_S0->pi+,pi-,e-,e+;:OnOff Off', 
        'set K_S0/K_S0->pi+,pi-;:OnOff Off', 
        'set Lambda0/Lambda0->n0,gamma;:OnOff Off', 
        'set Lambda0/Lambda0->n0,pi0;:OnOff Off', 
        'set Lambda0/Lambda0->p+,nu_ebar,e-;:OnOff Off', 
        'set Lambda0/Lambda0->p+,pi-,gamma;:OnOff Off', 
        'set Lambda0/Lambda0->p+,pi-;:OnOff Off', 
        'set Lambdabar0/Lambdabar0->nbar0,gamma;:OnOff Off', 
        'set Lambdabar0/Lambdabar0->nbar0,pi0;:OnOff Off', 
        'set Lambdabar0/Lambdabar0->pbar-,nu_e,e+;:OnOff Off', 
        'set Lambdabar0/Lambdabar0->pbar-,pi+,gamma;:OnOff Off', 
        'set Lambdabar0/Lambdabar0->pbar-,pi+;:OnOff Off', 
        'set mu+/mu+->nu_mubar,nu_e,e+;:OnOff Off', 
        'set mu-/mu-->nu_mu,nu_ebar,e-;:OnOff Off', 
        'set Omegabar+/Omegabar+->Lambdabar0,K+;:OnOff Off', 
        'set Omegabar+/Omegabar+->Xibar0,nu_e,e+;:OnOff Off', 
        'set Omegabar+/Omegabar+->Xibar0,pi+;:OnOff Off', 
        'set Omegabar+/Omegabar+->Xibar+,pi0;:OnOff Off', 
        'set Omega-/Omega-->Lambda0,K-;:OnOff Off', 
        'set Omega-/Omega-->Xi0,nu_ebar,e-;:OnOff Off', 
        'set Omega-/Omega-->Xi0,pi-;:OnOff Off', 
        'set Omega-/Omega-->Xi-,pi0;:OnOff Off', 
        'set pi-/pi-->nu_ebar,e-;:OnOff Off', 
        'set pi+/pi+->nu_e,e+;:OnOff Off', 
        'set pi-/pi-->nu_mubar,mu-;:OnOff Off', 
        'set pi+/pi+->nu_mu,mu+;:OnOff Off', 
        'set Sigmabar+/Sigmabar+->nbar0,nu_e,e+;:OnOff Off', 
        'set Sigmabar+/Sigmabar+->nbar0,pi+,gamma;:OnOff Off', 
        'set Sigmabar-/Sigmabar-->nbar0,pi-;:OnOff Off', 
        'set Sigmabar+/Sigmabar+->nbar0,pi+;:OnOff Off', 
        'set Sigmabar-/Sigmabar-->pbar-,gamma;:OnOff Off', 
        'set Sigmabar-/Sigmabar-->pbar-,pi0;:OnOff Off', 
        'set Sigma-/Sigma-->n0,nu_ebar,e-;:OnOff Off', 
        'set Sigma-/Sigma-->n0,pi-,gamma;:OnOff Off', 
        'set Sigma-/Sigma-->n0,pi-;:OnOff Off', 
        'set Sigma+/Sigma+->n0,pi+;:OnOff Off', 
        'set Sigma+/Sigma+->p+,gamma;:OnOff Off', 
        'set Sigma+/Sigma+->p+,pi0;:OnOff Off', 
        'set Xi0/Xi0->Lambda0,gamma;:OnOff Off', 
        'set Xi0/Xi0->Lambda0,pi0;:OnOff Off', 
        'set Xi0/Xi0->Sigma0,gamma;:OnOff Off', 
        'set Xibar0/Xibar0->Lambdabar0,gamma;:OnOff Off', 
        'set Xibar0/Xibar0->Lambdabar0,pi0;:OnOff Off', 
        'set Xibar0/Xibar0->Sigmabar0,gamma;:OnOff Off', 
        'set Xibar+/Xibar+->Lambdabar0,nu_e,e+;:OnOff Off', 
        'set Xibar+/Xibar+->Lambdabar0,pi+;:OnOff Off', 
        'set Xi-/Xi-->Lambda0,nu_ebar,e-;:OnOff Off', 
        'set Xi-/Xi-->Lambda0,pi-;:OnOff Off', 
        'cd /'),
    generatorModule = cms.string('/Herwig/Generators/LHCGenerator'),
    crossSection = cms.untracked.double(1.84505e-07),
    eventHandlers = cms.string('/Herwig/EventHandlers'),
    parameterSets = cms.vstring('cm10TeV', 
        'QCDCSAParameters', 
        'basicSetup', 
        'disableCtau10mmDecays'),
    basicSetup = cms.vstring('cd /Herwig/Generators', 
        'set LHCGenerator:NumberOfEvents 10000000', 
        'set LHCGenerator:DebugLevel 1', 
        'set LHCGenerator:PrintEvent 0', 
        'set LHCGenerator:MaxErrors 10000', 
        'cd /')
)

# Output definition
process.output = cms.OutputModule("PoolOutputModule",
    outputCommands = process.RAWSIMEventContent.outputCommands,
    fileName = cms.untracked.string('Herwigpp_QCD_Pt_1400_GEN_SIM_DIGI_L1_DIGI2RAW_HLT.root'),
    dataset = cms.untracked.PSet(
        dataTier = cms.untracked.string('GEN-SIM-RAW'),
        filterName = cms.untracked.string('')
    ),
    SelectEvents = cms.untracked.PSet(
        SelectEvents = cms.vstring('generation_step')
    )
)

# Additional output definition

# Other statements
process.GlobalTag.globaltag = 'IDEAL_V9::All'

# Path and EndPath definitions
process.generation_step = cms.Path(process.pgen)
process.simulation_step = cms.Path(process.psim)
process.digitisation_step = cms.Path(process.pdigi)
process.L1simulation_step = cms.Path(process.SimL1Emulator)
process.digi2raw_step = cms.Path(process.DigiToRaw)
process.out_step = cms.EndPath(process.output)

# Schedule definition
process.schedule = cms.Schedule(process.generation_step,process.simulation_step,process.digitisation_step,process.L1simulation_step,process.digi2raw_step,process.HLTriggerFirstPath,process.HLT_L1Jet15,process.HLT_Jet30,process.HLT_Jet50,process.HLT_Jet80,process.HLT_Jet110,process.HLT_Jet180,process.HLT_Jet250,process.HLT_FwdJet20,process.HLT_DoubleJet150,process.HLT_DoubleJet125_Aco,process.HLT_DoubleFwdJet50,process.HLT_DiJetAve15,process.HLT_DiJetAve30,process.HLT_DiJetAve50,process.HLT_DiJetAve70,process.HLT_DiJetAve130,process.HLT_DiJetAve220,process.HLT_TripleJet85,process.HLT_QuadJet30,process.HLT_QuadJet60,process.HLT_SumET120,process.HLT_L1MET20,process.HLT_MET25,process.HLT_MET35,process.HLT_MET50,process.HLT_MET65,process.HLT_MET75,process.HLT_MET35_HT350,process.HLT_Jet180_MET60,process.HLT_Jet60_MET70_Aco,process.HLT_Jet100_MET60_Aco,process.HLT_DoubleJet125_MET60,process.HLT_DoubleFwdJet40_MET60,process.HLT_DoubleJet60_MET60_Aco,process.HLT_DoubleJet50_MET70_Aco,process.HLT_DoubleJet40_MET70_Aco,process.HLT_TripleJet60_MET60,process.HLT_QuadJet35_MET60,process.HLT_IsoEle15_L1I,process.HLT_IsoEle18_L1R,process.HLT_IsoEle15_LW_L1I,process.HLT_LooseIsoEle15_LW_L1R,process.HLT_Ele10_SW_L1R,process.HLT_Ele15_SW_L1R,process.HLT_Ele15_LW_L1R,process.HLT_EM80,process.HLT_EM200,process.HLT_DoubleIsoEle10_L1I,process.HLT_DoubleIsoEle12_L1R,process.HLT_DoubleIsoEle10_LW_L1I,process.HLT_DoubleIsoEle12_LW_L1R,process.HLT_DoubleEle5_SW_L1R,process.HLT_DoubleEle10_LW_OnlyPixelM_L1R,process.HLT_DoubleEle10_Z,process.HLT_DoubleEle6_Exclusive,process.HLT_IsoPhoton30_L1I,process.HLT_IsoPhoton10_L1R,process.HLT_IsoPhoton15_L1R,process.HLT_IsoPhoton20_L1R,process.HLT_IsoPhoton25_L1R,process.HLT_IsoPhoton40_L1R,process.HLT_Photon15_L1R,process.HLT_Photon25_L1R,process.HLT_DoubleIsoPhoton20_L1I,process.HLT_DoubleIsoPhoton20_L1R,process.HLT_DoublePhoton10_Exclusive,process.HLT_L1Mu,process.HLT_L1MuOpen,process.HLT_L2Mu9,process.HLT_IsoMu9,process.HLT_IsoMu11,process.HLT_IsoMu13,process.HLT_IsoMu15,process.HLT_Mu3,process.HLT_Mu5,process.HLT_Mu7,process.HLT_Mu9,process.HLT_Mu11,process.HLT_Mu13,process.HLT_Mu15,process.HLT_Mu15_L1Mu7,process.HLT_Mu15_Vtx2cm,process.HLT_Mu15_Vtx2mm,process.HLT_DoubleIsoMu3,process.HLT_DoubleMu3,process.HLT_DoubleMu3_Vtx2cm,process.HLT_DoubleMu3_Vtx2mm,process.HLT_DoubleMu3_JPsi,process.HLT_DoubleMu3_Upsilon,process.HLT_DoubleMu7_Z,process.HLT_DoubleMu3_SameSign,process.HLT_DoubleMu3_Psi2S,process.HLT_BTagIP_Jet180,process.HLT_BTagIP_Jet120_Relaxed,process.HLT_BTagIP_DoubleJet120,process.HLT_BTagIP_DoubleJet60_Relaxed,process.HLT_BTagIP_TripleJet70,process.HLT_BTagIP_TripleJet40_Relaxed,process.HLT_BTagIP_QuadJet40,process.HLT_BTagIP_QuadJet30_Relaxed,process.HLT_BTagIP_HT470,process.HLT_BTagIP_HT320_Relaxed,process.HLT_BTagMu_DoubleJet120,process.HLT_BTagMu_DoubleJet60_Relaxed,process.HLT_BTagMu_TripleJet70,process.HLT_BTagMu_TripleJet40_Relaxed,process.HLT_BTagMu_QuadJet40,process.HLT_BTagMu_QuadJet30_Relaxed,process.HLT_BTagMu_HT370,process.HLT_BTagMu_HT250_Relaxed,process.HLT_DoubleMu3_BJPsi,process.HLT_DoubleMu4_BJPsi,process.HLT_TripleMu3_TauTo3Mu,process.HLT_IsoTau_MET65_Trk20,process.HLT_IsoTau_MET35_Trk15_L1MET,process.HLT_LooseIsoTau_MET30,process.HLT_LooseIsoTau_MET30_L1MET,process.HLT_DoubleIsoTau_Trk3,process.HLT_DoubleLooseIsoTau,process.HLT_IsoEle8_IsoMu7,process.HLT_IsoEle10_Mu10_L1R,process.HLT_IsoEle12_IsoTau_Trk3,process.HLT_IsoEle10_BTagIP_Jet35,process.HLT_IsoEle12_Jet40,process.HLT_IsoEle12_DoubleJet80,process.HLT_IsoEle5_TripleJet30,process.HLT_IsoEle12_TripleJet60,process.HLT_IsoEle12_QuadJet35,process.HLT_IsoMu14_IsoTau_Trk3,process.HLT_IsoMu7_BTagIP_Jet35,process.HLT_IsoMu7_BTagMu_Jet20,process.HLT_IsoMu7_Jet40,process.HLT_NoL2IsoMu8_Jet40,process.HLT_Mu14_Jet50,process.HLT_Mu5_TripleJet30,process.HLT_BTagMu_Jet20_Calib,process.HLT_ZeroBias,process.HLT_MinBias,process.HLT_MinBiasHcal,process.HLT_MinBiasEcal,process.HLT_MinBiasPixel,process.HLT_MinBiasPixel_Trk5,process.HLT_BackwardBSC,process.HLT_ForwardBSC,process.HLT_CSCBeamHalo,process.HLT_CSCBeamHaloOverlapRing1,process.HLT_CSCBeamHaloOverlapRing2,process.HLT_CSCBeamHaloRing2or3,process.HLT_TrackerCosmics,process.AlCa_IsoTrack,process.AlCa_EcalPhiSym,process.AlCa_EcalPi0,process.HLTriggerFinalPath,process.out_step)


# Automatic addition of the customisation function

def customise(process):

	process.genParticles.abortOnUnknownPDGCode = False

	return(process)


# End of customisation function definition

process = customise(process)