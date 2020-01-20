# Spirent TestCenter Logic Script
# Generated on Wed Dec 11 15:24:52 2019 by thinkpalm
# Framework ver. 4.94.6346.0000
#
# Comments: 
# 
#
# This logic script contains the following routines invoked from the
# STC_Traffic.py script.



# Load Spirent TestCenter
from StcPython import StcPython
stc = StcPython()

#    init - set the logging level and logging location (stdout).
#           Possible logLevel values are: 
#             DEBUG - Display DEBUG, INFO, WARN, and ERROR messages
#             INFO  - Display INFO, WARN, and ERROR messages
#             WARN  - Display WARN and ERROR messages
#             ERROR - Display only ERROR messages
#
#           Possible values for logTo are "stdout" or a file name (can include
#           the path). Use forward slashes between directory names.
def init():
    stc.config('automationoptions', logTo='stdout', logLevel='WARN')

#    config - load the configuration into memory. The port locations
#             are taken from the XML file but may be passed in from the
#             launcher script. The XML config file may be passed in from
#             the launcher script as well.
#
#           - set the location for results files.
#             Possible values are: 
#               INSTALL_DIR - Spirent TestCenter installation directory.
#               CURRENT_WORKING_DIR - Current working directory. This 
#                   is the directory that Spirent TestCenter currently
#                   has open.
#               USER_WORKING_DIR - User working directory.
#               CURRENT_CONFIG_DIR - Current configuration directory. 
#                   This is the directory where the saved or loaded
#                   .xml or .tcc file is located. If no .xml or .tcc 
#                   file has been saved or loaded, files are saved
#                   to the user working directory.
#
#             The location of the results files can be modified in the
#             launcher file. The saveResultsRelativeTo parameter sets a path 
#             that is prepended to the value of the ResultsDirectory 
#             parameter. To set an fully qualified (absolute) path for 
#             results, set the ResultsDirectory parameter and set 
#             SaveResultsRelativeTo to NONE.
#
#           - set up the sequencer. Currently sets the sequencer
#             to stop on any error.  Other options are IGNORE_ERROR and 
#             PAUSE_ON_ERROR.
def config(resultsDir, portLocations):
    stc.config('system1',IsLoadingFromConfiguration='true')

    system1 = "system1"
    stc.config('system1', \
    InSimulationMode="FALSE", \
    UseSmbMessaging="FALSE", \
    ApplicationName="TestCenter", \
    TSharkPath="", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="StcSystem 1")

    Project_1 = stc.create("Project", \
    TableViewData="", \
    TestMode="L2L3", \
    SelectedTechnologyProfiles="", \
    ConfigurationFileName="STC_Traffic.py", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="Project 1")

    Port_1 = stc.create("Port",under = Project_1, \
    location= portLocations[0], \
    UseDefaultHost="TRUE", \
    AppendLocationToPortName="TRUE", \
    Layer3Type="IPV4", \
    PortGroupSize="1", \
    TestModuleProfile="Default", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="Port //2/2")

    Port_2 = stc.create("Port",under = Project_1, \
    location= portLocations[1], \
    UseDefaultHost="TRUE", \
    AppendLocationToPortName="TRUE", \
    Layer3Type="IPV4", \
    PortGroupSize="1", \
    TestModuleProfile="Default", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="Port //2/3")

    Tags_1 = (stc.get( Project_1, 'children-Tags' )).split(' ')[0]
    stc.config(Tags_1, \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="Tags 1")

    Tag_1 = stc.create("Tag",under = Tags_1, \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="Host")

    Tag_2 = stc.create("Tag",under = Tags_1, \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="Router")

    Tag_3 = stc.create("Tag",under = Tags_1, \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="Client")

    Tag_4 = stc.create("Tag",under = Tags_1, \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="Server")

    Tag_5 = stc.create("Tag",under = Tags_1, \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="Core")

    Tag_6 = stc.create("Tag",under = Tags_1, \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="Edge")

    TestInfo_1 = (stc.get( Project_1, 'children-TestInfo' )).split(' ')[0]
    stc.config(TestInfo_1, \
    OwnerDisplayName="", \
    TestName="", \
    Description="", \
    UserTags="", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="TestInfo 1")

    DeviceAddrOptions_1 = (stc.get( Project_1, 'children-DeviceAddrOptions' )).split(' ')[0]
    stc.config(DeviceAddrOptions_1, \
    NextIpv4="192.85.1.9", \
    Ipv4Increment="0.0.0.1", \
    DefaultIpv4Prefix="24", \
    NextIpv6="2001::2", \
    Ipv6Increment="::1", \
    DefaultIpv6Prefix="64", \
    NextMac="00:10:94:00:00:07", \
    MacIncrement="00:00:00:00:00:01", \
    NextRouterId="192.0.0.7", \
    RouterIdIncrement="0.0.0.1", \
    NextIpv6RouterId="2000::7", \
    Ipv6RouterIdIncrement="::1", \
    NextWwn="20:00:10:85:00:00:00:01", \
    WwnIncrement="00:00:00:00:00:00:00:01", \
    UseForDeviceGenConfigExpand="TRUE", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="DeviceAddrOptions 2")

    Ieee80211PhyOptions_1 = (stc.get( Project_1, 'children-Ieee80211PhyOptions' )).split(' ')[0]
    stc.config(Ieee80211PhyOptions_1, \
    SelectedRegion="USA", \
    AutoConnect="FALSE", \
    ScanDuration="10", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="Ieee80211PhyOptions 2")

    PhyOptions_1 = (stc.get( Project_1, 'children-PhyOptions' )).split(' ')[0]
    stc.config(PhyOptions_1, \
    EnableCompensationMode="FALSE", \
    Enable8023brSwitch="FALSE", \
    EnableL1RegisterAccess="FALSE", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="PhyOptions 2")

    TestResultSetting_1 = (stc.get( Project_1, 'children-TestResultSetting' )).split(' ')[0]
    stc.config(TestResultSetting_1, \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="TestResultSetting 2")

    PortOptions_1 = (stc.get( Project_1, 'children-PortOptions' )).split(' ')[0]
    stc.config(PortOptions_1, \
    ReleaseMode="FULL_RESET", \
    AggregatorResult="AGGREGATED", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="Port Options 2")

    RealismOptions_1 = (stc.get( Project_1, 'children-RealismOptions' )).split(' ')[0]
    stc.config(RealismOptions_1, \
    RealismMode="NORMAL", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="Realism Options 2")

    TrafficOptions_1 = (stc.get( Project_1, 'children-TrafficOptions' )).split(' ')[0]
    stc.config(TrafficOptions_1, \
    TrafficStartMode="ASYNCHRONOUS", \
    TrafficStartInterval="0", \
    TrafficStartIntervalUnit="UNITOF64US", \
    TrafficStreamIDStartIndex="1", \
    DeleteInactiveStreamsFromMemory="FALSE", \
    EnableGlobalAnalyzerPreload="FALSE", \
    TSharkPath="None", \
    ExcludeEthernetFcs="TRUE", \
    SmoothenRandomLength="FALSE", \
    UniqueRandomLengthSeedPerPort="FALSE", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="TrafficOptions 2")

    GroupHistogram_1 = (stc.get( Project_1, 'children-GroupHistogram' )).split(' ')[0]
    stc.config(GroupHistogram_1, \
    ActiveGroupHistogramMode="DISABLED_MODE", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="Group Histogram 2")

    ResultOptions_1 = (stc.get( Project_1, 'children-ResultOptions' )).split(' ')[0]
    stc.config(ResultOptions_1, \
    ResultViewMode="BASIC", \
    ColumnFilterMode="BASIC", \
    ShowWarningMessage="TRUE", \
    StopTrafficBeforeClearingResults="FALSE", \
    StopAnalyzerBeforeClearingResults="FALSE", \
    SyncClearResults="FALSE", \
    TimedRefreshResultViewMode="PERIODIC", \
    TimedRefreshInterval="1", \
    CollectStrayFrame="FALSE", \
    PreambleByteLength="8", \
    IfgByteLength="12", \
    JitterMode="RFC3393ABSOLUTEVALUE", \
    DeleteAllAnalyzerStreams="FALSE", \
    SaveAtEotProperties="", \
    TxPortExpectMCastTrafficSentFromSelf="FALSE", \
    SaveOnlyCountersFromResultViewMode="FALSE", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="ResultOptions 2")

    LabelBindingGlobalConfig_1 = (stc.get( Project_1, 'children-LabelBindingGlobalConfig' )).split(' ')[0]
    stc.config(LabelBindingGlobalConfig_1, \
    SubscriptionInterval="5", \
    LabelResolutionMode="PER_SESSION_LABEL_RESOLUTION", \
    SelectDeactivedTunnelForData="TRUE", \
    EnableTransmitUnresolvedStream="TRUE", \
    EnableStaticPwAttachmentGroupId="FALSE", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="LabelBindingGlobalConfig 2")

    MplsTpGlobalConfig_1 = (stc.get( Project_1, 'children-MplsTpGlobalConfig' )).split(' ')[0]
    stc.config(MplsTpGlobalConfig_1, \
    FMChannelType="88", \
    PWChannelType="34", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="MplsTpGlobalConfig 2")

    L2LearningConfig_1 = (stc.get( Project_1, 'children-L2LearningConfig' )).split(' ')[0]
    stc.config(L2LearningConfig_1, \
    Rate="1000", \
    RepeatCount="3", \
    LearningStartDelay="1", \
    L2FrameSize="SAME_AS_STREAM", \
    L2FrameSizeFixed="128", \
    EncapOption="USE_TX_ENCAP", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="L2LearningConfig 2")

    ArpNdConfig_1 = (stc.get( Project_1, 'children-ArpNdConfig' )).split(' ')[0]
    stc.config(ArpNdConfig_1, \
    LearningRate="250", \
    MaxBurst="16", \
    EnableCyclicArp="TRUE", \
    DuplicateGatewayDetection="TRUE", \
    RetryCount="3", \
    TimeOut="1000", \
    EnableUniqueMacAddrInReply="FALSE", \
    EnableUniqueMacPattern="2222", \
    ProcessGratuitousArpRequests="TRUE", \
    UpdateDestMacUponNonGratuitousArpRequestsReceived="FALSE", \
    ProcessUnsolicitedArpReplies="TRUE", \
    EnableAutoArp="FALSE", \
    ApplyConfiguredGatewayMac="FALSE", \
    SetArpNdNoExpire="FALSE", \
    IgnoreFailures="TRUE", \
    UseLinkLocalAddrForNeighborDiscovery="FALSE", \
    UseConfiguredLinkLocalAddrForNeighborDiscovery="FALSE", \
    UseLinklayerCacheInStack="FALSE", \
    UseGatewayForTarget="FALSE", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="ArpNdConfig 2")

    BgpGlobalConfig_1 = (stc.get( Project_1, 'children-BgpGlobalConfig' )).split(' ')[0]
    stc.config(BgpGlobalConfig_1, \
    SequentialStartup="DISABLE", \
    StaggerOpen="100", \
    StaggerClose="100", \
    ConnectionRetryInterval="30", \
    ConnectionRetryCount="100", \
    UpdateCount="2000", \
    UpdateDelay="1", \
    VplsDraftVersion="VERSION_VPLS_4761", \
    ScalabilityMode="NORMAL", \
    EnableTcpNoDelay="FALSE", \
    EnablePackUpdates="TRUE", \
    TxTcpBufferSize="TCPBUFFER_32KB", \
    RxTcpBufferSize="TCPBUFFER_32KB", \
    TcpMaxSegmentSize="1460", \
    EnableStraightforwardUpdate="FALSE", \
    IgnoreAttributeErrors="FALSE", \
    MvpnAutoAdvertiseDelay="1000", \
    IsEvpnIRB="FALSE", \
    EvpnIRBMode="ASYMMETRIC", \
    NextHopFilterMode="DISABLED", \
    EnableDiscardUpdates="FALSE", \
    DisablePathMtuDiscovery="FALSE", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="BgpGlobalConfig 2")

    BgpSrGlobalConfig_1 = (stc.get( BgpGlobalConfig_1, 'children-BgpSrGlobalConfig' )).split(' ')[0]
    stc.config(BgpSrGlobalConfig_1, \
    SrDraftVersion="VERSION_00", \
    PrefixSidAttrType="40", \
    Srv6TlvType="4", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="BgpSrGlobalConfig 2")

    BgpSrGlobalBlock_1 = (stc.get( BgpSrGlobalConfig_1, 'children-BgpSrGlobalBlock' )).split(' ')[0]
    stc.config(BgpSrGlobalBlock_1, \
    BlockBase="16000", \
    BlockRange="1000", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="BgpSrGlobalBlock 2")

    PimGlobalConfig_1 = (stc.get( Project_1, 'children-PimGlobalConfig' )).split(' ')[0]
    stc.config(PimGlobalConfig_1, \
    TriggerHelloDelay="5", \
    EnablingPruningDelayOption="FALSE", \
    Tbit="FALSE", \
    LanPruneDelay="500", \
    OverrideInterval="2500", \
    EnablePackGroupRecord="TRUE", \
    EnableMsgRate="FALSE", \
    MsgRate="100", \
    MsgInterval="1", \
    DisableHelloExpireTimer="FALSE", \
    DisableHelloRxInNeighborState="FALSE", \
    DisableIncomingMsgProcessing="FALSE", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="PimGlobalConfig 2")

    IsisGlobalConfig_1 = (stc.get( Project_1, 'children-IsisGlobalConfig' )).split(' ')[0]
    stc.config(IsisGlobalConfig_1, \
    ScalabilityMode="NORMAL", \
    UseSameSrgb="FALSE", \
    SrmsPreferenceSubTlvType="24", \
    Srv6CapabilitySubTlvType="25", \
    Srv6LocatorTlvType="27", \
    Srv6EndSidSubTlvType="5", \
    Srv6EndXSidSubTlvType="43", \
    Srv6LanEndXSidSubTlvType="44", \
    SrNodeMsdSubTlvType="23", \
    SrLinkMsdSubTlvType="15", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="IsisGlobalConfig 2")

    IsisPlsbGlobalConfig_1 = (stc.get( Project_1, 'children-IsisPlsbGlobalConfig' )).split(' ')[0]
    stc.config(IsisPlsbGlobalConfig_1, \
    PlsbNlpid="143", \
    PlsbInstanceTlvType="180", \
    PlsbIsidAddrTlvType="181", \
    PlsbLinkMetricSubTlvType="17", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="IsisPlsbGlobalConfig 2")

    OtvOptions_1 = (stc.get( Project_1, 'children-OtvOptions' )).split(' ')[0]
    stc.config(OtvOptions_1, \
    UnicastOnlyTransport="FALSE", \
    OverlayEncapMode="MPLS_GRE", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="OTV Project-Level Options 2")

    VxlanGlobalConfig_1 = (stc.get( Project_1, 'children-VxlanGlobalConfig' )).split(' ')[0]
    stc.config(VxlanGlobalConfig_1, \
    EnableVxlanScale="TRUE", \
    EnableTrafficScaleForEvpnLearning="FALSE", \
    EnableVxlanFlowBasedTraffic="FALSE", \
    EnableEvpnOverlayIRB="FALSE", \
    EvpnOverlayIRBMode="ASYMMETRIC", \
    DiscardEvpnLearning="FALSE", \
    EnableDRVForVxlanBindings="FALSE", \
    EnableEvpnType5VA="FALSE", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="VxlanGlobalConfig 2")

    PcepGlobalConfig_1 = (stc.get( Project_1, 'children-PcepGlobalConfig' )).split(' ')[0]
    stc.config(PcepGlobalConfig_1, \
    SessionOutStanding="100", \
    SessionRetryCount="5", \
    SessionRetryInterval="10", \
    LSPPerMessage="100", \
    TCPInterval="500", \
    PacketAlignToMTU="FALSE", \
    EnableTCPNoDelay="FALSE", \
    UseSRDraft5="FALSE", \
    AssociationTypeListTlvType="200", \
    PpagAssociationType="100", \
    PpagTlvType="100", \
    ScaleMode="FALSE", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="PcepGlobalConfig 2")

    Ieee8021asGlobalConfig_1 = (stc.get( Project_1, 'children-Ieee8021asGlobalConfig' )).split(' ')[0]
    stc.config(Ieee8021asGlobalConfig_1, \
    ManagementId="12292", \
    TlvType="32772", \
    SlaveInfoSetCount="1", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="Ieee8021asGlobalConfig 2")

    Dhcpv4Options_1 = (stc.get( Project_1, 'children-Dhcpv4Options' )).split(' ')[0]
    stc.config(Dhcpv4Options_1, \
    TrafficBehavior="REQUIRE_ALL_SESSIONS_BOUND", \
    EnableServerRouting="FALSE", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="Dhcpv4Options 2")

    Dhcpv6Options_1 = (stc.get( Project_1, 'children-Dhcpv6Options' )).split(' ')[0]
    stc.config(Dhcpv6Options_1, \
    TrafficBehavior="REQUIRE_ALL_SESSIONS_BOUND", \
    EnableServerRouting="FALSE", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="Dhcpv6Options 2")

    PppoxOptions_1 = (stc.get( Project_1, 'children-PppoxOptions' )).split(' ')[0]
    stc.config(PppoxOptions_1, \
    TrafficBehavior="REQUIRE_ALL_SESSIONS_CONNECTED", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="PppoxOptions 2")

    MplsTpOamGlobalConfig_1 = (stc.get( Project_1, 'children-MplsTpOamGlobalConfig' )).split(' ')[0]
    stc.config(MplsTpOamGlobalConfig_1, \
    LmrRxFCfStart="1", \
    LmrRxFCfStep="1", \
    LmrTxFCbStart="1", \
    LmrTxFCbStep="1", \
    LmmTxFCfOffset="0", \
    LmrRxFCfOffset="0", \
    LmrTxFCbOffset="0", \
    CcOptionalTlvs="<frame><config><pdus /></config></frame>", \
    LbmOptionalTlvs="<frame><config><pdus /></config></frame>", \
    LbrOptionalTlvs="<frame><config><pdus /></config></frame>", \
    TstOptionalTlvs="<frame><config><pdus><pdu name=\"proto1\" pdu=\"MPLSTPOAMTLV:TestTLV\"><Length>0040</Length></pdu></pdus></config></frame>", \
    ChannelType="8902", \
    EchoTlvsInLmr="FALSE", \
    EchoTlvsInDmr="FALSE", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="MplsTpOamGlobalConfig 2")

    EoamGlobalConfig_1 = (stc.get( Project_1, 'children-EoamGlobalConfig' )).split(' ')[0]
    stc.config(EoamGlobalConfig_1, \
    DmCommonTimeSource="FALSE", \
    LmrRxFCfStart="1", \
    LmrRxFCfStep="1", \
    LmrTxFCbStart="1", \
    LmrTxFCbStep="1", \
    LmmTxFCfOffset="0", \
    LmrRxFCfOffset="0", \
    LmrTxFCbOffset="0", \
    SlrTxFCbStart="1", \
    SlrTxFCbStep="1", \
    SlmTxFCfOffset="0", \
    SlrTxFCbOffset="0", \
    CcOptionalTlvs="<frame><config><pdus /></config></frame>", \
    LbmOptionalTlvs="<frame><config><pdus /></config></frame>", \
    LbrOptionalTlvs="<frame><config><pdus /></config></frame>", \
    LtmOptionalTlvs="<frame><config><pdus><pdu name=\"proto1\" pdu=\"EOAMTLV:LTMEgrID\"><Length>0000</Length></pdu></pdus></config></frame>", \
    LtrOptionalTlvs="<frame><config><pdus><pdu name=\"proto1\" pdu=\"EOAMTLV:LTREgrID\"><Length>0000</Length></pdu><pdu name=\"RplyEgr_1\" pdu=\"EOAMTLV:RplyEgr\"><Length>0000</Length></pdu></pdus></config></frame>", \
    DmmOptionalTlvs="<frame><config><pdus /></config></frame>", \
    DmrOptionalTlvs="<frame><config><pdus /></config></frame>", \
    LmmOptionalTlvs="<frame><config><pdus /></config></frame>", \
    LmrOptionalTlvs="<frame><config><pdus /></config></frame>", \
    SlmOptionalTlvs="<frame><config><pdus /></config></frame>", \
    SlrOptionalTlvs="<frame><config><pdus /></config></frame>", \
    ResultTimeUnit="MILLISECONDS", \
    TestModeType="NORMAL", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="EoamGlobalConfig 2")

    VqAnalyzerOptions_1 = (stc.get( Project_1, 'children-VqAnalyzerOptions' )).split(' ')[0]
    stc.config(VqAnalyzerOptions_1, \
    SamplingPeriod="10", \
    DatabaseFileName="vqAnalyzerTest.db", \
    AppendDateTime="TRUE", \
    EnableEotDatabase="TRUE", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="VqAnalyzerOptions 2")

    ExternalDeviceOption_1 = (stc.get( Project_1, 'children-ExternalDeviceOption' )).split(' ')[0]
    stc.config(ExternalDeviceOption_1, \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="ExternalDeviceOption 2")

    Dot1xOptions_1 = (stc.get( Project_1, 'children-Dot1xOptions' )).split(' ')[0]
    stc.config(Dot1xOptions_1, \
    TrafficStartOption="REQUIRE_ALL_SUPPLICANT_AUTH", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="Dot1xOptions 2")

    VicGlobalConfig_1 = (stc.get( Project_1, 'children-VicGlobalConfig' )).split(' ')[0]
    stc.config(VicGlobalConfig_1, \
    OpenRequestTlvs="<frame><config><pdus><pdu name=\"ccc1\" pdu=\"VICTLV:CtrlChanCapTLV\"></pdu><pdu name=\"mta1\" pdu=\"VICTLV:MsgTypeArrayTLV\"></pdu><pdu name=\"rlc1\" pdu=\"VICTLV:ResourceLimitCapTLV\"></pdu><pdu name=\"ec1\" pdu=\"VICTLV:EthernetCapTLV\"></pdu><pdu name=\"fc1\" pdu=\"VICTLV:FcoeCapTLV\"></pdu></pdus></config></frame>", \
    CreateRequestTlvs="<frame><config><pdus><pdu name=\"pi1\" pdu=\"VICTLV:ProvisioningInfoTLV\"><Type>12</Type><Length>0</Length><ProvisioningInfoTypeSpace>00000C</ProvisioningInfoTypeSpace><Info><ProvList name=\"ProvList_0\"><Fixed><NumOfTlvs>0</NumOfTlvs><SubTlvs><FixedSubTlvList name=\"FixedSubTlvList_0\"><ProfileNameTlv><Type>1</Type><Length>0</Length></ProfileNameTlv></FixedSubTlvList><FixedSubTlvList name=\"FixedSubTlvList_1\"><vNicUuidTlv><Type>2</Type><Length>0</Length></vNicUuidTlv></FixedSubTlvList></SubTlvs></Fixed></ProvList></Info></pdu></pdus></config></frame>", \
    EnableRequestTlvs="<frame><config><pdus></pdus></config></frame>", \
    SpirentOpenRequestTlvs="<frame><config><pdus><pdu name=\"ccc1\" pdu=\"VICTLV:CtrlChanCapTLV\"></pdu><pdu name=\"mta1\" pdu=\"VICTLV:MsgTypeArrayTLV\"></pdu><pdu name=\"rlc1\" pdu=\"VICTLV:ResourceLimitCapTLV\"></pdu><pdu name=\"ec1\" pdu=\"VICTLV:EthernetCapTLV\"></pdu><pdu name=\"fc1\" pdu=\"VICTLV:FcoeCapTLV\"></pdu></pdus></config></frame>", \
    SpirentCreateRequestTlvs="<frame><config><pdus><pdu name=\"pi1\" pdu=\"VICTLV:ProvisioningInfoTLV\"></pdu></pdus></config></frame>", \
    SpirentEnableRequestTlvs="<frame><config><pdus></pdus></config></frame>", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="VIC 2")

    MsdpGlobalConfig_1 = (stc.get( Project_1, 'children-MsdpGlobalConfig' )).split(' ')[0]
    stc.config(MsdpGlobalConfig_1, \
    SessionOutstanding="100", \
    SessionRetryCount="5", \
    SessionRetryInterval="10", \
    SourceActiveAdvertisementTimer="60", \
    SourceActiveStateTimer="100", \
    PacketAlignToMTU="FALSE", \
    ScaleMode="FALSE", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="MsdpGlobalConfig 2")

    FrameLengthDistribution_1 = stc.create("FrameLengthDistribution",under = Project_1, \
    Seed="10900842", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="Default")

    FrameLengthDistributionSlot_1 = (stc.get( FrameLengthDistribution_1, 'children-FrameLengthDistributionSlot' )).split(' ')[0]
    stc.config(FrameLengthDistributionSlot_1, \
    FrameLengthMode="FIXED", \
    FixedFrameLength="40", \
    MinFrameLength="40", \
    MaxFrameLength="41", \
    Weight="7", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="FrameLengthDistributionSlot 5")

    FrameLengthDistributionSlot_2 = stc.create("FrameLengthDistributionSlot",under = FrameLengthDistribution_1, \
    FrameLengthMode="FIXED", \
    FixedFrameLength="576", \
    MinFrameLength="575", \
    MaxFrameLength="577", \
    Weight="4", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="FrameLengthDistributionSlot 6")

    FrameLengthDistributionSlot_3 = stc.create("FrameLengthDistributionSlot",under = FrameLengthDistribution_1, \
    FrameLengthMode="FIXED", \
    FixedFrameLength="1500", \
    MinFrameLength="1499", \
    MaxFrameLength="1500", \
    Weight="1", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="FrameLengthDistributionSlot 7")

    FrameLengthDistribution_2 = stc.create("FrameLengthDistribution",under = Project_1, \
    Seed="10900842", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="Spirent")

    FrameLengthDistributionSlot_4 = (stc.get( FrameLengthDistribution_2, 'children-FrameLengthDistributionSlot' )).split(' ')[0]
    stc.config(FrameLengthDistributionSlot_4, \
    FrameLengthMode="FIXED", \
    FixedFrameLength="40", \
    MinFrameLength="40", \
    MaxFrameLength="41", \
    Weight="5867", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="FrameLengthDistributionSlot 13")

    FrameLengthDistributionSlot_5 = stc.create("FrameLengthDistributionSlot",under = FrameLengthDistribution_2, \
    FrameLengthMode="FIXED", \
    FixedFrameLength="44", \
    MinFrameLength="43", \
    MaxFrameLength="45", \
    Weight="200", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="FrameLengthDistributionSlot 14")

    FrameLengthDistributionSlot_6 = stc.create("FrameLengthDistributionSlot",under = FrameLengthDistribution_2, \
    FrameLengthMode="FIXED", \
    FixedFrameLength="576", \
    MinFrameLength="575", \
    MaxFrameLength="577", \
    Weight="2366", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="FrameLengthDistributionSlot 15")

    FrameLengthDistributionSlot_7 = stc.create("FrameLengthDistributionSlot",under = FrameLengthDistribution_2, \
    FrameLengthMode="FIXED", \
    FixedFrameLength="1500", \
    MinFrameLength="1499", \
    MaxFrameLength="1500", \
    Weight="1567", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="FrameLengthDistributionSlot 16")

    FrameLengthDistribution_3 = stc.create("FrameLengthDistribution",under = Project_1, \
    Seed="10900842", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="4-Point")

    FrameLengthDistributionSlot_8 = (stc.get( FrameLengthDistribution_3, 'children-FrameLengthDistributionSlot' )).split(' ')[0]
    stc.config(FrameLengthDistributionSlot_8, \
    FrameLengthMode="FIXED", \
    FixedFrameLength="40", \
    MinFrameLength="40", \
    MaxFrameLength="41", \
    Weight="55", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="FrameLengthDistributionSlot 8")

    FrameLengthDistributionSlot_9 = stc.create("FrameLengthDistributionSlot",under = FrameLengthDistribution_3, \
    FrameLengthMode="FIXED", \
    FixedFrameLength="576", \
    MinFrameLength="575", \
    MaxFrameLength="577", \
    Weight="15", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="FrameLengthDistributionSlot 9")

    FrameLengthDistributionSlot_10 = stc.create("FrameLengthDistributionSlot",under = FrameLengthDistribution_3, \
    FrameLengthMode="FIXED", \
    FixedFrameLength="1500", \
    MinFrameLength="1499", \
    MaxFrameLength="1500", \
    Weight="10", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="FrameLengthDistributionSlot 10")

    FrameLengthDistributionSlot_11 = stc.create("FrameLengthDistributionSlot",under = FrameLengthDistribution_3, \
    FrameLengthMode="RANDOM", \
    FixedFrameLength="730", \
    MinFrameLength="40", \
    MaxFrameLength="1500", \
    Weight="20", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="FrameLengthDistributionSlot 11")

    FrameLengthDistribution_4 = stc.create("FrameLengthDistribution",under = Project_1, \
    Seed="10900842", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="TCPv4")

    FrameLengthDistributionSlot_12 = (stc.get( FrameLengthDistribution_4, 'children-FrameLengthDistributionSlot' )).split(' ')[0]
    stc.config(FrameLengthDistributionSlot_12, \
    FrameLengthMode="FIXED", \
    FixedFrameLength="72", \
    MinFrameLength="71", \
    MaxFrameLength="73", \
    Weight="5867", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="FrameLengthDistributionSlot 17")

    FrameLengthDistributionSlot_13 = stc.create("FrameLengthDistributionSlot",under = FrameLengthDistribution_4, \
    FrameLengthMode="FIXED", \
    FixedFrameLength="74", \
    MinFrameLength="73", \
    MaxFrameLength="75", \
    Weight="200", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="FrameLengthDistributionSlot 18")

    FrameLengthDistributionSlot_14 = stc.create("FrameLengthDistributionSlot",under = FrameLengthDistribution_4, \
    FrameLengthMode="FIXED", \
    FixedFrameLength="576", \
    MinFrameLength="575", \
    MaxFrameLength="577", \
    Weight="2366", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="FrameLengthDistributionSlot 19")

    FrameLengthDistributionSlot_15 = stc.create("FrameLengthDistributionSlot",under = FrameLengthDistribution_4, \
    FrameLengthMode="FIXED", \
    FixedFrameLength="1500", \
    MinFrameLength="1499", \
    MaxFrameLength="1500", \
    Weight="1567", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="FrameLengthDistributionSlot 20")

    FrameLengthDistribution_5 = stc.create("FrameLengthDistribution",under = Project_1, \
    Seed="10900842", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="IPSEC")

    FrameLengthDistributionSlot_16 = (stc.get( FrameLengthDistribution_5, 'children-FrameLengthDistributionSlot' )).split(' ')[0]
    stc.config(FrameLengthDistributionSlot_16, \
    FrameLengthMode="FIXED", \
    FixedFrameLength="72", \
    MinFrameLength="71", \
    MaxFrameLength="73", \
    Weight="5867", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="FrameLengthDistributionSlot 21")

    FrameLengthDistributionSlot_17 = stc.create("FrameLengthDistributionSlot",under = FrameLengthDistribution_5, \
    FrameLengthMode="FIXED", \
    FixedFrameLength="74", \
    MinFrameLength="73", \
    MaxFrameLength="75", \
    Weight="200", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="FrameLengthDistributionSlot 22")

    FrameLengthDistributionSlot_18 = stc.create("FrameLengthDistributionSlot",under = FrameLengthDistribution_5, \
    FrameLengthMode="FIXED", \
    FixedFrameLength="576", \
    MinFrameLength="575", \
    MaxFrameLength="577", \
    Weight="2366", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="FrameLengthDistributionSlot 23")

    FrameLengthDistributionSlot_19 = stc.create("FrameLengthDistributionSlot",under = FrameLengthDistribution_5, \
    FrameLengthMode="FIXED", \
    FixedFrameLength="1400", \
    MinFrameLength="1399", \
    MaxFrameLength="1401", \
    Weight="1567", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="FrameLengthDistributionSlot 24")

    FrameLengthDistribution_6 = stc.create("FrameLengthDistribution",under = Project_1, \
    Seed="10900842", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="JMIX Downstream")

    FrameLengthDistributionSlot_20 = (stc.get( FrameLengthDistribution_6, 'children-FrameLengthDistributionSlot' )).split(' ')[0]
    stc.config(FrameLengthDistributionSlot_20, \
    FrameLengthMode="FIXED", \
    FixedFrameLength="60", \
    MinFrameLength="59", \
    MaxFrameLength="61", \
    Weight="3", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="FrameLengthDistributionSlot 53")

    FrameLengthDistributionSlot_21 = stc.create("FrameLengthDistributionSlot",under = FrameLengthDistribution_6, \
    FrameLengthMode="FIXED", \
    FixedFrameLength="120", \
    MinFrameLength="119", \
    MaxFrameLength="121", \
    Weight="4", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="FrameLengthDistributionSlot 54")

    FrameLengthDistributionSlot_22 = stc.create("FrameLengthDistributionSlot",under = FrameLengthDistribution_6, \
    FrameLengthMode="FIXED", \
    FixedFrameLength="576", \
    MinFrameLength="575", \
    MaxFrameLength="577", \
    Weight="1", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="FrameLengthDistributionSlot 55")

    FrameLengthDistributionSlot_23 = stc.create("FrameLengthDistributionSlot",under = FrameLengthDistribution_6, \
    FrameLengthMode="FIXED", \
    FixedFrameLength="1500", \
    MinFrameLength="1499", \
    MaxFrameLength="1500", \
    Weight="5", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="FrameLengthDistributionSlot 56")

    FrameLengthDistribution_7 = stc.create("FrameLengthDistribution",under = Project_1, \
    Seed="10900842", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="JMIX Upstream")

    FrameLengthDistributionSlot_24 = (stc.get( FrameLengthDistribution_7, 'children-FrameLengthDistributionSlot' )).split(' ')[0]
    stc.config(FrameLengthDistributionSlot_24, \
    FrameLengthMode="FIXED", \
    FixedFrameLength="60", \
    MinFrameLength="59", \
    MaxFrameLength="61", \
    Weight="7", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="FrameLengthDistributionSlot 49")

    FrameLengthDistributionSlot_25 = stc.create("FrameLengthDistributionSlot",under = FrameLengthDistribution_7, \
    FrameLengthMode="FIXED", \
    FixedFrameLength="120", \
    MinFrameLength="119", \
    MaxFrameLength="121", \
    Weight="8", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="FrameLengthDistributionSlot 50")

    FrameLengthDistributionSlot_26 = stc.create("FrameLengthDistributionSlot",under = FrameLengthDistribution_7, \
    FrameLengthMode="FIXED", \
    FixedFrameLength="576", \
    MinFrameLength="575", \
    MaxFrameLength="577", \
    Weight="1", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="FrameLengthDistributionSlot 51")

    FrameLengthDistributionSlot_27 = stc.create("FrameLengthDistributionSlot",under = FrameLengthDistribution_7, \
    FrameLengthMode="FIXED", \
    FixedFrameLength="1500", \
    MinFrameLength="1499", \
    MaxFrameLength="1500", \
    Weight="3", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="FrameLengthDistributionSlot 52")

    CustomFillPattern_1 = stc.create("CustomFillPattern",under = Project_1, \
    PatternData="0", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="Pattern 1")

    ExposedConfig_1 = stc.create("ExposedConfig",under = Project_1, \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="ExposedConfig 1")

    ResultDataSet_1 = stc.create("ResultDataSet",under = Project_1, \
    PrimaryClass="Port", \
    InternalXmlFormatString="", \
    ResultFilterMode="1", \
    ResultViewDataOutput="FALSE", \
    PageNumber="1", \
    RecordsPerPage="100", \
    NotifyInterval="1000", \
    Identifier="Port Traffic\\Basic Traffic Results", \
    Persistent="TRUE", \
    CreatorId="", \
    IsDeprecated="FALSE", \
    Path="Port Traffic", \
    ResultViewOwner="SYSTEM", \
    Description="object://core/Port", \
    CustomDisplayName="", \
    CustomDisplayPath="Port Traffic and Counters", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="Basic Traffic Results")

    ResultQuery_1 = stc.create("ResultQuery",under = ResultDataSet_1, \
    ConfigClassId="generator", \
    ResultClassId="generatorportresults", \
    PropertyIdArray="generatorportresults.totalframecount generatorportresults.generatorframecount generatorportresults.generatorsigframecount generatorportresults.generatorundersizeframecount generatorportresults.generatoroversizeframecount generatorportresults.generatorjumboframecount generatorportresults.totalframerate generatorportresults.generatorframerate generatorportresults.generatoroctetrate generatorportresults.generatorsigframerate generatorportresults.generatorundersizeframerate generatorportresults.generatoroversizeframerate generatorportresults.generatorjumboframerate generatorportresults.generatorcrcerrorframecount generatorportresults.generatorl3checksumerrorcount generatorportresults.generatorl4checksumerrorcount generatorportresults.generatorcrcerrorframerate generatorportresults.generatorl3checksumerrorrate generatorportresults.generatorl4checksumerrorrate generatorportresults.totalipv4framecount generatorportresults.totalipv6framecount generatorportresults.totalmplsframecount generatorportresults.generatoripv4framecount generatorportresults.generatoripv6framecount generatorportresults.generatorvlanframecount generatorportresults.generatormplsframecount generatorportresults.totalipv4framerate generatorportresults.totalipv6framerate generatorportresults.totalmplsframerate generatorportresults.generatoripv4framerate generatorportresults.generatoripv6framerate generatorportresults.generatorvlanframerate generatorportresults.generatormplsframerate generatorportresults.totalbitrate generatorportresults.generatorbitrate generatorportresults.l1bitcount generatorportresults.l1bitrate generatorportresults.pfcframecount generatorportresults.pfcpri0framecount generatorportresults.pfcpri1framecount generatorportresults.pfcpri2framecount generatorportresults.pfcpri3framecount generatorportresults.pfcpri4framecount generatorportresults.pfcpri5framecount generatorportresults.pfcpri6framecount generatorportresults.pfcpri7framecount generatorportresults.l1bitratepercent generatorportresults.totalbitcount", \
    ResultOptions="", \
    ArchivingOption="NONE", \
    InternalCookie="", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="ResultQuery 32")

    ResultQuery_2 = stc.create("ResultQuery",under = ResultDataSet_1, \
    ConfigClassId="analyzer", \
    ResultClassId="analyzerportresults", \
    PropertyIdArray="analyzerportresults.totalframecount analyzerportresults.sigframecount analyzerportresults.undersizeframecount analyzerportresults.oversizeframecount analyzerportresults.jumboframecount analyzerportresults.pauseframecount analyzerportresults.totalframerate analyzerportresults.sigframerate analyzerportresults.undersizeframerate analyzerportresults.oversizeframerate analyzerportresults.jumboframerate analyzerportresults.pauseframerate analyzerportresults.fcserrorframecount analyzerportresults.ipv4checksumerrorcount analyzerportresults.tcpchecksumerrorcount analyzerportresults.udpchecksumerrorcount analyzerportresults.prbsfilloctetcount analyzerportresults.prbsbiterrorcount analyzerportresults.fcserrorframerate analyzerportresults.ipv4checksumerrorrate analyzerportresults.tcpchecksumerrorrate analyzerportresults.udpchecksumerrorrate analyzerportresults.prbsbiterrorrate analyzerportresults.ipv4framecount analyzerportresults.ipv6framecount analyzerportresults.tcpframecount analyzerportresults.udpframecount analyzerportresults.mplsframecount analyzerportresults.icmpframecount analyzerportresults.vlanframecount analyzerportresults.ipv4framerate analyzerportresults.ipv6framerate analyzerportresults.tcpframerate analyzerportresults.udpframerate analyzerportresults.mplsframerate analyzerportresults.icmpframerate analyzerportresults.vlanframerate analyzerportresults.trigger1count analyzerportresults.trigger1rate analyzerportresults.trigger2count analyzerportresults.trigger2rate analyzerportresults.trigger3count analyzerportresults.trigger3rate analyzerportresults.trigger4count analyzerportresults.trigger4rate analyzerportresults.trigger5count analyzerportresults.trigger5rate analyzerportresults.trigger6count analyzerportresults.trigger6rate analyzerportresults.trigger7count analyzerportresults.trigger7rate analyzerportresults.trigger8count analyzerportresults.trigger8rate analyzerportresults.combotriggercount analyzerportresults.combotriggerrate analyzerportresults.totalbitrate analyzerportresults.prbsbiterrorratio analyzerportresults.vlanframerate analyzerportresults.l1bitcount analyzerportresults.l1bitrate analyzerportresults.pfcframecount analyzerportresults.fcoeframecount analyzerportresults.pfcframerate analyzerportresults.fcoeframerate analyzerportresults.pfcpri0framecount analyzerportresults.pfcpri1framecount analyzerportresults.pfcpri2framecount analyzerportresults.pfcpri3framecount analyzerportresults.pfcpri4framecount analyzerportresults.pfcpri5framecount analyzerportresults.pfcpri6framecount analyzerportresults.pfcpri7framecount analyzerportresults.prbserrorframecount analyzerportresults.prbserrorframerate analyzerportresults.userdefinedframecount1 analyzerportresults.userdefinedframerate1 analyzerportresults.userdefinedframecount2 analyzerportresults.userdefinedframerate2 analyzerportresults.userdefinedframecount3 analyzerportresults.userdefinedframerate3 analyzerportresults.userdefinedframecount4 analyzerportresults.userdefinedframerate4 analyzerportresults.userdefinedframecount5 analyzerportresults.userdefinedframerate5 analyzerportresults.userdefinedframecount6 analyzerportresults.userdefinedframerate6 analyzerportresults.l1bitratepercent analyzerportresults.outseqframecount analyzerportresults.droppedframecount analyzerportresults.inorderframecount analyzerportresults.reorderedframecount analyzerportresults.duplicateframecount analyzerportresults.lateframecount analyzerportresults.correctedrsfecerrorcount analyzerportresults.uncorrectedrsfecerrorcount analyzerportresults.correctedbaserfecerrorcount analyzerportresults.uncorrectedbaserfecerrorcount analyzerportresults.correctedrsfecsymbols analyzerportresults.prersfecserrate analyzerportresults.postrsfecserrate analyzerportresults.prebaserfecserrate analyzerportresults.postbaserfecserrate analyzerportresults.totalbitcount", \
    ResultOptions="", \
    ArchivingOption="NONE", \
    InternalCookie="", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="ResultQuery 33")

    RealTimeResultColumnDefinition_1 = stc.create("RealTimeResultColumnDefinition",under = ResultDataSet_1, \
    ColumnClassName="Port", \
    ColumnPropertyName="PortName", \
    ColumnDescription="DescribeMe", \
    ColumnWidth="70", \
    ColumnUnits="0", \
    ColumnPrecision="2", \
    ColumnSortType="NONE", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="RealTimeResultColumnDefinition 671")

    RealTimeResultColumnDefinition_2 = stc.create("RealTimeResultColumnDefinition",under = ResultDataSet_1, \
    ColumnClassName="GeneratorPortResults", \
    ColumnPropertyName="TotalFrameCount", \
    ColumnDescription="DescribeMe", \
    ColumnWidth="92", \
    ColumnUnits="16", \
    ColumnPrecision="2", \
    ColumnSortType="NONE", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="RealTimeResultColumnDefinition 672")

    RealTimeResultColumnDefinition_3 = stc.create("RealTimeResultColumnDefinition",under = ResultDataSet_1, \
    ColumnClassName="AnalyzerPortResults", \
    ColumnPropertyName="TotalFrameCount", \
    ColumnDescription="DescribeMe", \
    ColumnWidth="92", \
    ColumnUnits="16", \
    ColumnPrecision="2", \
    ColumnSortType="NONE", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="RealTimeResultColumnDefinition 673")

    RealTimeResultColumnDefinition_4 = stc.create("RealTimeResultColumnDefinition",under = ResultDataSet_1, \
    ColumnClassName="GeneratorPortResults", \
    ColumnPropertyName="TotalBitCount", \
    ColumnDescription="DescribeMe", \
    ColumnWidth="122", \
    ColumnUnits="1", \
    ColumnPrecision="2", \
    ColumnSortType="NONE", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="RealTimeResultColumnDefinition 674")

    RealTimeResultColumnDefinition_5 = stc.create("RealTimeResultColumnDefinition",under = ResultDataSet_1, \
    ColumnClassName="AnalyzerPortResults", \
    ColumnPropertyName="TotalBitCount", \
    ColumnDescription="DescribeMe", \
    ColumnWidth="122", \
    ColumnUnits="1", \
    ColumnPrecision="2", \
    ColumnSortType="NONE", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="RealTimeResultColumnDefinition 675")

    RealTimeResultColumnDefinition_6 = stc.create("RealTimeResultColumnDefinition",under = ResultDataSet_1, \
    ColumnClassName="GeneratorPortResults", \
    ColumnPropertyName="TotalBitRate", \
    ColumnDescription="DescribeMe", \
    ColumnWidth="122", \
    ColumnUnits="7", \
    ColumnPrecision="2", \
    ColumnSortType="NONE", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="RealTimeResultColumnDefinition 676")

    RealTimeResultColumnDefinition_7 = stc.create("RealTimeResultColumnDefinition",under = ResultDataSet_1, \
    ColumnClassName="AnalyzerPortResults", \
    ColumnPropertyName="TotalBitRate", \
    ColumnDescription="DescribeMe", \
    ColumnWidth="123", \
    ColumnUnits="7", \
    ColumnPrecision="2", \
    ColumnSortType="NONE", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="RealTimeResultColumnDefinition 677")

    RealTimeResultColumnDefinition_8 = stc.create("RealTimeResultColumnDefinition",under = ResultDataSet_1, \
    ColumnClassName="GeneratorPortResults", \
    ColumnPropertyName="L1BitCount", \
    ColumnDescription="DescribeMe", \
    ColumnWidth="122", \
    ColumnUnits="1", \
    ColumnPrecision="2", \
    ColumnSortType="NONE", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="RealTimeResultColumnDefinition 678")

    RealTimeResultColumnDefinition_9 = stc.create("RealTimeResultColumnDefinition",under = ResultDataSet_1, \
    ColumnClassName="AnalyzerPortResults", \
    ColumnPropertyName="L1BitCount", \
    ColumnDescription="DescribeMe", \
    ColumnWidth="122", \
    ColumnUnits="1", \
    ColumnPrecision="2", \
    ColumnSortType="NONE", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="RealTimeResultColumnDefinition 679")

    RealTimeResultColumnDefinition_10 = stc.create("RealTimeResultColumnDefinition",under = ResultDataSet_1, \
    ColumnClassName="GeneratorPortResults", \
    ColumnPropertyName="L1BitRate", \
    ColumnDescription="DescribeMe", \
    ColumnWidth="122", \
    ColumnUnits="7", \
    ColumnPrecision="2", \
    ColumnSortType="NONE", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="RealTimeResultColumnDefinition 680")

    RealTimeResultColumnDefinition_11 = stc.create("RealTimeResultColumnDefinition",under = ResultDataSet_1, \
    ColumnClassName="AnalyzerPortResults", \
    ColumnPropertyName="L1BitRate", \
    ColumnDescription="DescribeMe", \
    ColumnWidth="122", \
    ColumnUnits="7", \
    ColumnPrecision="2", \
    ColumnSortType="NONE", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="RealTimeResultColumnDefinition 681")

    RealTimeResultColumnDefinition_12 = stc.create("RealTimeResultColumnDefinition",under = ResultDataSet_1, \
    ColumnClassName="GeneratorPortResults", \
    ColumnPropertyName="L1BitRatePercent", \
    ColumnDescription="DescribeMe", \
    ColumnWidth="122", \
    ColumnUnits="0", \
    ColumnPrecision="3", \
    ColumnSortType="NONE", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="RealTimeResultColumnDefinition 680")

    RealTimeResultColumnDefinition_13 = stc.create("RealTimeResultColumnDefinition",under = ResultDataSet_1, \
    ColumnClassName="AnalyzerPortResults", \
    ColumnPropertyName="L1BitRatePercent", \
    ColumnDescription="DescribeMe", \
    ColumnWidth="122", \
    ColumnUnits="0", \
    ColumnPrecision="3", \
    ColumnSortType="NONE", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="RealTimeResultColumnDefinition 681")

    RealTimeResultColumnDefinition_14 = stc.create("RealTimeResultColumnDefinition",under = ResultDataSet_1, \
    ColumnClassName="GeneratorPortResults", \
    ColumnPropertyName="GeneratorFrameCount", \
    ColumnDescription="DescribeMe", \
    ColumnWidth="148", \
    ColumnUnits="16", \
    ColumnPrecision="2", \
    ColumnSortType="NONE", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="RealTimeResultColumnDefinition 682")

    RealTimeResultColumnDefinition_15 = stc.create("RealTimeResultColumnDefinition",under = ResultDataSet_1, \
    ColumnClassName="GeneratorPortResults", \
    ColumnPropertyName="GeneratorSigFrameCount", \
    ColumnDescription="DescribeMe", \
    ColumnWidth="167", \
    ColumnUnits="16", \
    ColumnPrecision="2", \
    ColumnSortType="NONE", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="RealTimeResultColumnDefinition 683")

    RealTimeResultColumnDefinition_16 = stc.create("RealTimeResultColumnDefinition",under = ResultDataSet_1, \
    ColumnClassName="AnalyzerPortResults", \
    ColumnPropertyName="SigFrameCount", \
    ColumnDescription="DescribeMe", \
    ColumnWidth="130", \
    ColumnUnits="16", \
    ColumnPrecision="2", \
    ColumnSortType="NONE", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="RealTimeResultColumnDefinition 684")

    RealTimeResultColumnDefinition_17 = stc.create("RealTimeResultColumnDefinition",under = ResultDataSet_1, \
    ColumnClassName="GeneratorPortResults", \
    ColumnPropertyName="TotalFrameRate", \
    ColumnDescription="DescribeMe", \
    ColumnWidth="111", \
    ColumnUnits="17", \
    ColumnPrecision="2", \
    ColumnSortType="NONE", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="RealTimeResultColumnDefinition 685")

    RealTimeResultColumnDefinition_18 = stc.create("RealTimeResultColumnDefinition",under = ResultDataSet_1, \
    ColumnClassName="AnalyzerPortResults", \
    ColumnPropertyName="TotalFrameRate", \
    ColumnDescription="DescribeMe", \
    ColumnWidth="111", \
    ColumnUnits="17", \
    ColumnPrecision="2", \
    ColumnSortType="NONE", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="RealTimeResultColumnDefinition 686")

    RealTimeResultColumnDefinition_19 = stc.create("RealTimeResultColumnDefinition",under = ResultDataSet_1, \
    ColumnClassName="GeneratorPortResults", \
    ColumnPropertyName="GeneratorFrameRate", \
    ColumnDescription="DescribeMe", \
    ColumnWidth="120", \
    ColumnUnits="17", \
    ColumnPrecision="2", \
    ColumnSortType="NONE", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="RealTimeResultColumnDefinition 687")

    RealTimeResultColumnDefinition_20 = stc.create("RealTimeResultColumnDefinition",under = ResultDataSet_1, \
    ColumnClassName="GeneratorPortResults", \
    ColumnPropertyName="GeneratorOctetRate", \
    ColumnDescription="DescribeMe", \
    ColumnWidth="123", \
    ColumnUnits="18", \
    ColumnPrecision="2", \
    ColumnSortType="NONE", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="RealTimeResultColumnDefinition 688")

    RealTimeResultColumnDefinition_21 = stc.create("RealTimeResultColumnDefinition",under = ResultDataSet_1, \
    ColumnClassName="GeneratorPortResults", \
    ColumnPropertyName="GeneratorBitRate", \
    ColumnDescription="DescribeMe", \
    ColumnWidth="131", \
    ColumnUnits="7", \
    ColumnPrecision="2", \
    ColumnSortType="NONE", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="RealTimeResultColumnDefinition 689")

    RealTimeResultColumnDefinition_22 = stc.create("RealTimeResultColumnDefinition",under = ResultDataSet_1, \
    ColumnClassName="GeneratorPortResults", \
    ColumnPropertyName="GeneratorSigFrameRate", \
    ColumnDescription="DescribeMe", \
    ColumnWidth="139", \
    ColumnUnits="17", \
    ColumnPrecision="2", \
    ColumnSortType="NONE", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="RealTimeResultColumnDefinition 690")

    RealTimeResultColumnDefinition_23 = stc.create("RealTimeResultColumnDefinition",under = ResultDataSet_1, \
    ColumnClassName="AnalyzerPortResults", \
    ColumnPropertyName="SigFrameRate", \
    ColumnDescription="DescribeMe", \
    ColumnWidth="102", \
    ColumnUnits="17", \
    ColumnPrecision="2", \
    ColumnSortType="NONE", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="RealTimeResultColumnDefinition 691")

    RealTimeResultColumnDefinition_24 = stc.create("RealTimeResultColumnDefinition",under = ResultDataSet_1, \
    ColumnClassName="AnalyzerPortResults", \
    ColumnPropertyName="FcsErrorFrameCount", \
    ColumnDescription="DescribeMe", \
    ColumnWidth="197", \
    ColumnUnits="16", \
    ColumnPrecision="2", \
    ColumnSortType="NONE", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="RealTimeResultColumnDefinition 692")

    RealTimeResultColumnDefinition_25 = stc.create("RealTimeResultColumnDefinition",under = ResultDataSet_1, \
    ColumnClassName="GeneratorPortResults", \
    ColumnPropertyName="GeneratorCrcErrorFrameCount", \
    ColumnDescription="DescribeMe", \
    ColumnWidth="201", \
    ColumnUnits="16", \
    ColumnPrecision="2", \
    ColumnSortType="NONE", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="RealTimeResultColumnDefinition 693")

    RealTimeResultColumnDefinition_26 = stc.create("RealTimeResultColumnDefinition",under = ResultDataSet_1, \
    ColumnClassName="GeneratorPortResults", \
    ColumnPropertyName="GeneratorL3ChecksumErrorCount", \
    ColumnDescription="DescribeMe", \
    ColumnWidth="198", \
    ColumnUnits="0", \
    ColumnPrecision="2", \
    ColumnSortType="NONE", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="RealTimeResultColumnDefinition 694")

    RealTimeResultColumnDefinition_27 = stc.create("RealTimeResultColumnDefinition",under = ResultDataSet_1, \
    ColumnClassName="GeneratorPortResults", \
    ColumnPropertyName="GeneratorL4ChecksumErrorCount", \
    ColumnDescription="DescribeMe", \
    ColumnWidth="198", \
    ColumnUnits="0", \
    ColumnPrecision="2", \
    ColumnSortType="NONE", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="RealTimeResultColumnDefinition 695")

    RealTimeResultColumnDefinition_28 = stc.create("RealTimeResultColumnDefinition",under = ResultDataSet_1, \
    ColumnClassName="AnalyzerPortResults", \
    ColumnPropertyName="Ipv4ChecksumErrorCount", \
    ColumnDescription="DescribeMe", \
    ColumnWidth="171", \
    ColumnUnits="0", \
    ColumnPrecision="2", \
    ColumnSortType="NONE", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="RealTimeResultColumnDefinition 696")

    RealTimeResultColumnDefinition_29 = stc.create("RealTimeResultColumnDefinition",under = ResultDataSet_1, \
    ColumnClassName="AnalyzerPortResults", \
    ColumnPropertyName="TcpChecksumErrorCount", \
    ColumnDescription="DescribeMe", \
    ColumnWidth="168", \
    ColumnUnits="0", \
    ColumnPrecision="2", \
    ColumnSortType="NONE", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="RealTimeResultColumnDefinition 697")

    RealTimeResultColumnDefinition_30 = stc.create("RealTimeResultColumnDefinition",under = ResultDataSet_1, \
    ColumnClassName="AnalyzerPortResults", \
    ColumnPropertyName="UdpChecksumErrorCount", \
    ColumnDescription="DescribeMe", \
    ColumnWidth="170", \
    ColumnUnits="0", \
    ColumnPrecision="2", \
    ColumnSortType="NONE", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="RealTimeResultColumnDefinition 698")

    RealTimeResultColumnDefinition_31 = stc.create("RealTimeResultColumnDefinition",under = ResultDataSet_1, \
    ColumnClassName="AnalyzerPortResults", \
    ColumnPropertyName="PrbsFillOctetCount", \
    ColumnDescription="DescribeMe", \
    ColumnWidth="148", \
    ColumnUnits="12", \
    ColumnPrecision="2", \
    ColumnSortType="NONE", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="RealTimeResultColumnDefinition 699")

    RealTimeResultColumnDefinition_32 = stc.create("RealTimeResultColumnDefinition",under = ResultDataSet_1, \
    ColumnClassName="AnalyzerPortResults", \
    ColumnPropertyName="PrbsBitErrorCount", \
    ColumnDescription="DescribeMe", \
    ColumnWidth="137", \
    ColumnUnits="0", \
    ColumnPrecision="2", \
    ColumnSortType="NONE", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="RealTimeResultColumnDefinition 700")

    RealTimeResultColumnDefinition_33 = stc.create("RealTimeResultColumnDefinition",under = ResultDataSet_1, \
    ColumnClassName="AnalyzerPortResults", \
    ColumnPropertyName="PrbsBitErrorRatio", \
    ColumnDescription="DescribeMe", \
    ColumnWidth="117", \
    ColumnUnits="0", \
    ColumnPrecision="2", \
    ColumnSortType="NONE", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="RealTimeResultColumnDefinition 701")

    RealTimeResultColumnDefinition_34 = stc.create("RealTimeResultColumnDefinition",under = ResultDataSet_1, \
    ColumnClassName="AnalyzerPortResults", \
    ColumnPropertyName="PrbsErrorFrameCount", \
    ColumnDescription="DescribeMe", \
    ColumnWidth="109", \
    ColumnUnits="16", \
    ColumnPrecision="2", \
    ColumnSortType="NONE", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="RealTimeResultColumnDefinition 702")

    RealTimeResultColumnDefinition_35 = stc.create("RealTimeResultColumnDefinition",under = ResultDataSet_1, \
    ColumnClassName="AnalyzerPortResults", \
    ColumnPropertyName="FcsErrorFrameRate", \
    ColumnDescription="DescribeMe", \
    ColumnWidth="134", \
    ColumnUnits="17", \
    ColumnPrecision="2", \
    ColumnSortType="NONE", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="RealTimeResultColumnDefinition 703")

    RealTimeResultColumnDefinition_36 = stc.create("RealTimeResultColumnDefinition",under = ResultDataSet_1, \
    ColumnClassName="GeneratorPortResults", \
    ColumnPropertyName="GeneratorCrcErrorFrameRate", \
    ColumnDescription="DescribeMe", \
    ColumnWidth="172", \
    ColumnUnits="17", \
    ColumnPrecision="2", \
    ColumnSortType="NONE", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="RealTimeResultColumnDefinition 704")

    RealTimeResultColumnDefinition_37 = stc.create("RealTimeResultColumnDefinition",under = ResultDataSet_1, \
    ColumnClassName="GeneratorPortResults", \
    ColumnPropertyName="GeneratorL3ChecksumErrorRate", \
    ColumnDescription="DescribeMe", \
    ColumnWidth="230", \
    ColumnUnits="0", \
    ColumnPrecision="2", \
    ColumnSortType="NONE", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="RealTimeResultColumnDefinition 705")

    RealTimeResultColumnDefinition_38 = stc.create("RealTimeResultColumnDefinition",under = ResultDataSet_1, \
    ColumnClassName="GeneratorPortResults", \
    ColumnPropertyName="GeneratorL4ChecksumErrorRate", \
    ColumnDescription="DescribeMe", \
    ColumnWidth="230", \
    ColumnUnits="0", \
    ColumnPrecision="2", \
    ColumnSortType="NONE", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="RealTimeResultColumnDefinition 706")

    RealTimeResultColumnDefinition_39 = stc.create("RealTimeResultColumnDefinition",under = ResultDataSet_1, \
    ColumnClassName="AnalyzerPortResults", \
    ColumnPropertyName="Ipv4ChecksumErrorRate", \
    ColumnDescription="DescribeMe", \
    ColumnWidth="164", \
    ColumnUnits="0", \
    ColumnPrecision="2", \
    ColumnSortType="NONE", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="RealTimeResultColumnDefinition 707")

    RealTimeResultColumnDefinition_40 = stc.create("RealTimeResultColumnDefinition",under = ResultDataSet_1, \
    ColumnClassName="AnalyzerPortResults", \
    ColumnPropertyName="TcpChecksumErrorRate", \
    ColumnDescription="DescribeMe", \
    ColumnWidth="162", \
    ColumnUnits="0", \
    ColumnPrecision="2", \
    ColumnSortType="NONE", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="RealTimeResultColumnDefinition 708")

    RealTimeResultColumnDefinition_41 = stc.create("RealTimeResultColumnDefinition",under = ResultDataSet_1, \
    ColumnClassName="AnalyzerPortResults", \
    ColumnPropertyName="UdpChecksumErrorRate", \
    ColumnDescription="DescribeMe", \
    ColumnWidth="163", \
    ColumnUnits="0", \
    ColumnPrecision="2", \
    ColumnSortType="NONE", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="RealTimeResultColumnDefinition 709")

    RealTimeResultColumnDefinition_42 = stc.create("RealTimeResultColumnDefinition",under = ResultDataSet_1, \
    ColumnClassName="AnalyzerPortResults", \
    ColumnPropertyName="PrbsBitErrorRate", \
    ColumnDescription="DescribeMe", \
    ColumnWidth="169", \
    ColumnUnits="7", \
    ColumnPrecision="2", \
    ColumnSortType="NONE", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="RealTimeResultColumnDefinition 710")

    RealTimeResultColumnDefinition_43 = stc.create("RealTimeResultColumnDefinition",under = ResultDataSet_1, \
    ColumnClassName="AnalyzerPortResults", \
    ColumnPropertyName="PrbsErrorFrameRate", \
    ColumnDescription="DescribeMe", \
    ColumnWidth="109", \
    ColumnUnits="17", \
    ColumnPrecision="2", \
    ColumnSortType="NONE", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="RealTimeResultColumnDefinition 711")

    RealTimeResultColumnDefinition_44 = stc.create("RealTimeResultColumnDefinition",under = ResultDataSet_1, \
    ColumnClassName="AnalyzerPortResults", \
    ColumnPropertyName="OutSeqFrameCount", \
    ColumnDescription="DescribeMe", \
    ColumnWidth="109", \
    ColumnUnits="16", \
    ColumnPrecision="2", \
    ColumnSortType="NONE", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="RealTimeResultColumnDefinition 712")

    RealTimeResultColumnDefinition_45 = stc.create("RealTimeResultColumnDefinition",under = ResultDataSet_1, \
    ColumnClassName="AnalyzerPortResults", \
    ColumnPropertyName="Trigger1Count", \
    ColumnDescription="DescribeMe", \
    ColumnWidth="70", \
    ColumnUnits="0", \
    ColumnPrecision="2", \
    ColumnSortType="NONE", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="RealTimeResultColumnDefinition 713")

    RealTimeResultColumnDefinition_46 = stc.create("RealTimeResultColumnDefinition",under = ResultDataSet_1, \
    ColumnClassName="AnalyzerPortResults", \
    ColumnPropertyName="Trigger2Count", \
    ColumnDescription="DescribeMe", \
    ColumnWidth="70", \
    ColumnUnits="0", \
    ColumnPrecision="2", \
    ColumnSortType="NONE", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="RealTimeResultColumnDefinition 714")

    RealTimeResultColumnDefinition_47 = stc.create("RealTimeResultColumnDefinition",under = ResultDataSet_1, \
    ColumnClassName="AnalyzerPortResults", \
    ColumnPropertyName="Trigger3Count", \
    ColumnDescription="DescribeMe", \
    ColumnWidth="70", \
    ColumnUnits="0", \
    ColumnPrecision="2", \
    ColumnSortType="NONE", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="RealTimeResultColumnDefinition 715")

    RealTimeResultColumnDefinition_48 = stc.create("RealTimeResultColumnDefinition",under = ResultDataSet_1, \
    ColumnClassName="AnalyzerPortResults", \
    ColumnPropertyName="Trigger4Count", \
    ColumnDescription="DescribeMe", \
    ColumnWidth="70", \
    ColumnUnits="0", \
    ColumnPrecision="2", \
    ColumnSortType="NONE", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="RealTimeResultColumnDefinition 716")

    RealTimeResultColumnDefinition_49 = stc.create("RealTimeResultColumnDefinition",under = ResultDataSet_1, \
    ColumnClassName="AnalyzerPortResults", \
    ColumnPropertyName="Trigger5Count", \
    ColumnDescription="DescribeMe", \
    ColumnWidth="70", \
    ColumnUnits="0", \
    ColumnPrecision="2", \
    ColumnSortType="NONE", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="RealTimeResultColumnDefinition 717")

    RealTimeResultColumnDefinition_50 = stc.create("RealTimeResultColumnDefinition",under = ResultDataSet_1, \
    ColumnClassName="AnalyzerPortResults", \
    ColumnPropertyName="Trigger6Count", \
    ColumnDescription="DescribeMe", \
    ColumnWidth="70", \
    ColumnUnits="0", \
    ColumnPrecision="2", \
    ColumnSortType="NONE", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="RealTimeResultColumnDefinition 718")

    RealTimeResultColumnDefinition_51 = stc.create("RealTimeResultColumnDefinition",under = ResultDataSet_1, \
    ColumnClassName="AnalyzerPortResults", \
    ColumnPropertyName="Trigger7Count", \
    ColumnDescription="DescribeMe", \
    ColumnWidth="70", \
    ColumnUnits="0", \
    ColumnPrecision="2", \
    ColumnSortType="NONE", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="RealTimeResultColumnDefinition 719")

    RealTimeResultColumnDefinition_52 = stc.create("RealTimeResultColumnDefinition",under = ResultDataSet_1, \
    ColumnClassName="AnalyzerPortResults", \
    ColumnPropertyName="Trigger8Count", \
    ColumnDescription="DescribeMe", \
    ColumnWidth="70", \
    ColumnUnits="0", \
    ColumnPrecision="2", \
    ColumnSortType="NONE", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="RealTimeResultColumnDefinition 720")

    RealTimeResultColumnDefinition_53 = stc.create("RealTimeResultColumnDefinition",under = ResultDataSet_1, \
    ColumnClassName="AnalyzerPortResults", \
    ColumnPropertyName="ComboTriggerCount", \
    ColumnDescription="DescribeMe", \
    ColumnWidth="87", \
    ColumnUnits="0", \
    ColumnPrecision="2", \
    ColumnSortType="NONE", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="RealTimeResultColumnDefinition 721")

    RealTimeResultColumnDefinition_54 = stc.create("RealTimeResultColumnDefinition",under = ResultDataSet_1, \
    ColumnClassName="AnalyzerPortResults", \
    ColumnPropertyName="Trigger1Rate", \
    ColumnDescription="DescribeMe", \
    ColumnWidth="89", \
    ColumnUnits="0", \
    ColumnPrecision="2", \
    ColumnSortType="NONE", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="RealTimeResultColumnDefinition 722")

    RealTimeResultColumnDefinition_55 = stc.create("RealTimeResultColumnDefinition",under = ResultDataSet_1, \
    ColumnClassName="AnalyzerPortResults", \
    ColumnPropertyName="Trigger2Rate", \
    ColumnDescription="DescribeMe", \
    ColumnWidth="89", \
    ColumnUnits="0", \
    ColumnPrecision="2", \
    ColumnSortType="NONE", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="RealTimeResultColumnDefinition 723")

    RealTimeResultColumnDefinition_56 = stc.create("RealTimeResultColumnDefinition",under = ResultDataSet_1, \
    ColumnClassName="AnalyzerPortResults", \
    ColumnPropertyName="Trigger3Rate", \
    ColumnDescription="DescribeMe", \
    ColumnWidth="89", \
    ColumnUnits="0", \
    ColumnPrecision="2", \
    ColumnSortType="NONE", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="RealTimeResultColumnDefinition 724")

    RealTimeResultColumnDefinition_57 = stc.create("RealTimeResultColumnDefinition",under = ResultDataSet_1, \
    ColumnClassName="AnalyzerPortResults", \
    ColumnPropertyName="Trigger4Rate", \
    ColumnDescription="DescribeMe", \
    ColumnWidth="89", \
    ColumnUnits="0", \
    ColumnPrecision="2", \
    ColumnSortType="NONE", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="RealTimeResultColumnDefinition 725")

    RealTimeResultColumnDefinition_58 = stc.create("RealTimeResultColumnDefinition",under = ResultDataSet_1, \
    ColumnClassName="AnalyzerPortResults", \
    ColumnPropertyName="Trigger5Rate", \
    ColumnDescription="DescribeMe", \
    ColumnWidth="89", \
    ColumnUnits="0", \
    ColumnPrecision="2", \
    ColumnSortType="NONE", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="RealTimeResultColumnDefinition 726")

    RealTimeResultColumnDefinition_59 = stc.create("RealTimeResultColumnDefinition",under = ResultDataSet_1, \
    ColumnClassName="AnalyzerPortResults", \
    ColumnPropertyName="Trigger6Rate", \
    ColumnDescription="DescribeMe", \
    ColumnWidth="89", \
    ColumnUnits="0", \
    ColumnPrecision="2", \
    ColumnSortType="NONE", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="RealTimeResultColumnDefinition 727")

    RealTimeResultColumnDefinition_60 = stc.create("RealTimeResultColumnDefinition",under = ResultDataSet_1, \
    ColumnClassName="AnalyzerPortResults", \
    ColumnPropertyName="Trigger7Rate", \
    ColumnDescription="DescribeMe", \
    ColumnWidth="89", \
    ColumnUnits="0", \
    ColumnPrecision="2", \
    ColumnSortType="NONE", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="RealTimeResultColumnDefinition 728")

    RealTimeResultColumnDefinition_61 = stc.create("RealTimeResultColumnDefinition",under = ResultDataSet_1, \
    ColumnClassName="AnalyzerPortResults", \
    ColumnPropertyName="Trigger8Rate", \
    ColumnDescription="DescribeMe", \
    ColumnWidth="89", \
    ColumnUnits="0", \
    ColumnPrecision="2", \
    ColumnSortType="NONE", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="RealTimeResultColumnDefinition 729")

    RealTimeResultColumnDefinition_62 = stc.create("RealTimeResultColumnDefinition",under = ResultDataSet_1, \
    ColumnClassName="AnalyzerPortResults", \
    ColumnPropertyName="ComboTriggerRate", \
    ColumnDescription="DescribeMe", \
    ColumnWidth="114", \
    ColumnUnits="0", \
    ColumnPrecision="2", \
    ColumnSortType="NONE", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="RealTimeResultColumnDefinition 730")

    RealTimeResultColumnDefinition_63 = stc.create("RealTimeResultColumnDefinition",under = ResultDataSet_1, \
    ColumnClassName="GeneratorPortResults", \
    ColumnPropertyName="TotalIpv4FrameCount", \
    ColumnDescription="DescribeMe", \
    ColumnWidth="86", \
    ColumnUnits="16", \
    ColumnPrecision="2", \
    ColumnSortType="NONE", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="RealTimeResultColumnDefinition 731")

    RealTimeResultColumnDefinition_64 = stc.create("RealTimeResultColumnDefinition",under = ResultDataSet_1, \
    ColumnClassName="GeneratorPortResults", \
    ColumnPropertyName="TotalIpv6FrameCount", \
    ColumnDescription="DescribeMe", \
    ColumnWidth="88", \
    ColumnUnits="16", \
    ColumnPrecision="2", \
    ColumnSortType="NONE", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="RealTimeResultColumnDefinition 732")

    RealTimeResultColumnDefinition_65 = stc.create("RealTimeResultColumnDefinition",under = ResultDataSet_1, \
    ColumnClassName="GeneratorPortResults", \
    ColumnPropertyName="TotalMplsFrameCount", \
    ColumnDescription="DescribeMe", \
    ColumnWidth="91", \
    ColumnUnits="16", \
    ColumnPrecision="2", \
    ColumnSortType="NONE", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="RealTimeResultColumnDefinition 733")

    RealTimeResultColumnDefinition_66 = stc.create("RealTimeResultColumnDefinition",under = ResultDataSet_1, \
    ColumnClassName="GeneratorPortResults", \
    ColumnPropertyName="GeneratorIpv4FrameCount", \
    ColumnDescription="DescribeMe", \
    ColumnWidth="129", \
    ColumnUnits="16", \
    ColumnPrecision="2", \
    ColumnSortType="NONE", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="RealTimeResultColumnDefinition 734")

    RealTimeResultColumnDefinition_67 = stc.create("RealTimeResultColumnDefinition",under = ResultDataSet_1, \
    ColumnClassName="GeneratorPortResults", \
    ColumnPropertyName="GeneratorIpv6FrameCount", \
    ColumnDescription="DescribeMe", \
    ColumnWidth="117", \
    ColumnUnits="16", \
    ColumnPrecision="2", \
    ColumnSortType="NONE", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="RealTimeResultColumnDefinition 735")

    RealTimeResultColumnDefinition_68 = stc.create("RealTimeResultColumnDefinition",under = ResultDataSet_1, \
    ColumnClassName="GeneratorPortResults", \
    ColumnPropertyName="GeneratorVlanFrameCount", \
    ColumnDescription="DescribeMe", \
    ColumnWidth="127", \
    ColumnUnits="16", \
    ColumnPrecision="2", \
    ColumnSortType="NONE", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="RealTimeResultColumnDefinition 736")

    RealTimeResultColumnDefinition_69 = stc.create("RealTimeResultColumnDefinition",under = ResultDataSet_1, \
    ColumnClassName="GeneratorPortResults", \
    ColumnPropertyName="GeneratorMplsFrameCount", \
    ColumnDescription="DescribeMe", \
    ColumnWidth="132", \
    ColumnUnits="16", \
    ColumnPrecision="2", \
    ColumnSortType="NONE", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="RealTimeResultColumnDefinition 737")

    RealTimeResultColumnDefinition_70 = stc.create("RealTimeResultColumnDefinition",under = ResultDataSet_1, \
    ColumnClassName="AnalyzerPortResults", \
    ColumnPropertyName="Ipv4FrameCount", \
    ColumnDescription="DescribeMe", \
    ColumnWidth="125", \
    ColumnUnits="16", \
    ColumnPrecision="2", \
    ColumnSortType="NONE", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="RealTimeResultColumnDefinition 738")

    RealTimeResultColumnDefinition_71 = stc.create("RealTimeResultColumnDefinition",under = ResultDataSet_1, \
    ColumnClassName="AnalyzerPortResults", \
    ColumnPropertyName="Ipv6FrameCount", \
    ColumnDescription="DescribeMe", \
    ColumnWidth="124", \
    ColumnUnits="16", \
    ColumnPrecision="2", \
    ColumnSortType="NONE", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="RealTimeResultColumnDefinition 739")

    RealTimeResultColumnDefinition_72 = stc.create("RealTimeResultColumnDefinition",under = ResultDataSet_1, \
    ColumnClassName="AnalyzerPortResults", \
    ColumnPropertyName="TcpFrameCount", \
    ColumnDescription="DescribeMe", \
    ColumnWidth="122", \
    ColumnUnits="16", \
    ColumnPrecision="2", \
    ColumnSortType="NONE", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="RealTimeResultColumnDefinition 740")

    RealTimeResultColumnDefinition_73 = stc.create("RealTimeResultColumnDefinition",under = ResultDataSet_1, \
    ColumnClassName="AnalyzerPortResults", \
    ColumnPropertyName="UdpFrameCount", \
    ColumnDescription="DescribeMe", \
    ColumnWidth="120", \
    ColumnUnits="16", \
    ColumnPrecision="2", \
    ColumnSortType="NONE", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="RealTimeResultColumnDefinition 741")

    RealTimeResultColumnDefinition_74 = stc.create("RealTimeResultColumnDefinition",under = ResultDataSet_1, \
    ColumnClassName="AnalyzerPortResults", \
    ColumnPropertyName="MplsFrameCount", \
    ColumnDescription="DescribeMe", \
    ColumnWidth="127", \
    ColumnUnits="16", \
    ColumnPrecision="2", \
    ColumnSortType="NONE", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="RealTimeResultColumnDefinition 742")

    RealTimeResultColumnDefinition_75 = stc.create("RealTimeResultColumnDefinition",under = ResultDataSet_1, \
    ColumnClassName="AnalyzerPortResults", \
    ColumnPropertyName="IcmpFrameCount", \
    ColumnDescription="DescribeMe", \
    ColumnWidth="125", \
    ColumnUnits="16", \
    ColumnPrecision="2", \
    ColumnSortType="NONE", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="RealTimeResultColumnDefinition 743")

    RealTimeResultColumnDefinition_76 = stc.create("RealTimeResultColumnDefinition",under = ResultDataSet_1, \
    ColumnClassName="AnalyzerPortResults", \
    ColumnPropertyName="VlanFrameCount", \
    ColumnDescription="DescribeMe", \
    ColumnWidth="113", \
    ColumnUnits="16", \
    ColumnPrecision="2", \
    ColumnSortType="NONE", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="RealTimeResultColumnDefinition 744")

    RealTimeResultGroupDefinition_1 = stc.create("RealTimeResultGroupDefinition",under = ResultDataSet_1, \
    GroupName="All Groups", \
    GroupId="core://allgroups/", \
    ColumnClassName="Port", \
    ColumnPropertyName="PortName", \
    CountQuery="", \
    SqlString="", \
    UseCustomSqlString="FALSE", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="RealTimeResultGroupDefinition 37")

    RealTimeResultColumnDefinition_77 = stc.create("RealTimeResultColumnDefinition",under = ResultDataSet_1, \
    ColumnClassName="AnalyzerPortResults", \
    ColumnPropertyName="FcoeFrameCount", \
    ColumnDescription="DescribeMe", \
    ColumnWidth="96", \
    ColumnUnits="16", \
    ColumnPrecision="2", \
    ColumnSortType="NONE", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="RealTimeResultColumnDefinition 38")

    RealTimeResultGroupDefinition_2 = stc.create("RealTimeResultGroupDefinition",under = ResultDataSet_1, \
    GroupName="Basic Counters", \
    GroupId="object://customgroup/cded8621-5e71-4a39-afd4-71d9faf37273/Basic Counters", \
    ColumnClassName="GeneratorPortResults AnalyzerPortResults GeneratorPortResults AnalyzerPortResults GeneratorPortResults AnalyzerPortResults GeneratorPortResults AnalyzerPortResults GeneratorPortResults AnalyzerPortResults GeneratorPortResults AnalyzerPortResults GeneratorPortResults GeneratorPortResults AnalyzerPortResults GeneratorPortResults AnalyzerPortResults GeneratorPortResults GeneratorPortResults GeneratorPortResults GeneratorPortResults AnalyzerPortResults", \
    ColumnPropertyName="TotalFrameCount TotalFrameCount TotalBitCount TotalBitCount TotalBitRate TotalBitRate L1BitCount L1BitCount L1BitRate L1BitRate L1BitRatePercent L1BitRatePercent GeneratorFrameCount GeneratorSigFrameCount SigFrameCount TotalFrameRate TotalFrameRate GeneratorFrameRate GeneratorOctetRate GeneratorBitRate GeneratorSigFrameRate SigFrameRate", \
    CountQuery="", \
    SqlString=" SELECT Port.Name AS 'Port Name', GeneratorPortResults.TotalFrameCount AS 'Total Tx Count (Frames)', AnalyzerPortResults.TotalFrameCount AS 'Total Rx Count (Frames)', GeneratorPortResults.GeneratorFrameCount AS 'Generator Count (Frames)', GeneratorPortResults.GeneratorSigFrameCount AS 'Generator Sig Count (Frames)', AnalyzerPortResults.SigFrameCount AS 'Rx Sig Count (Frames)', (GeneratorPortResults.TotalOctetCount * 8) AS 'Total Tx  Count (bits)', (AnalyzerPortResults.TotalOctetCount * 8) AS 'Total Rx Count (bits)', GeneratorPortResults.L1BitCount AS 'Tx L1 Count (bits)', AnalyzerPortResults.L1BitCount AS 'Rx L1 Count (bits)', AnalyzerPortResults.MinFrameLength AS 'Rx Min FrameLength', AnalyzerPortResults.MaxFrameLength AS 'Rx Max FrameLength', GeneratorPortResults.TotalCellCount AS 'Total Tx Count (Cells)', AnalyzerPortResults.TotalCellCount AS 'Total Rx Count (Cells)' FROM Port, GeneratorPortResults, Generator, AnalyzerPortResults, Analyzer WHERE ( Generator.ParentHnd = Port.Handle AND Analyzer.ParentHnd = Port.Handle AND GeneratorPortResults.ParentHnd = Generator.Handle AND AnalyzerPortResults.ParentHnd = Analyzer.Handle AND Port.DataSetId = @DataSetId AND GeneratorPortResults.DataSetId = @DataSetId AND Generator.DataSetId = @DataSetId AND AnalyzerPortResults.DataSetId = @DataSetId AND Analyzer.DataSetId = @DataSetId  )", \
    UseCustomSqlString="TRUE", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="RealTimeResultGroupDefinition 39")

    RealTimeResultGroupDefinition_3 = stc.create("RealTimeResultGroupDefinition",under = ResultDataSet_1, \
    GroupName="Errors", \
    GroupId="object://customgroup/e26c15e5-fb73-46ad-a76b-45304a4e6303/Errors", \
    ColumnClassName="GeneratorPortResults AnalyzerPortResults AnalyzerPortResults GeneratorPortResults GeneratorPortResults GeneratorPortResults AnalyzerPortResults AnalyzerPortResults AnalyzerPortResults AnalyzerPortResults AnalyzerPortResults AnalyzerPortResults AnalyzerPortResults AnalyzerPortResults GeneratorPortResults GeneratorPortResults GeneratorPortResults AnalyzerPortResults AnalyzerPortResults AnalyzerPortResults AnalyzerPortResults AnalyzerPortResults AnalyzerPortResults", \
    ColumnPropertyName="TotalFrameCount TotalFrameCount FcsErrorFrameCount GeneratorCrcErrorFrameCount GeneratorL3ChecksumErrorCount GeneratorL4ChecksumErrorCount Ipv4ChecksumErrorCount TcpChecksumErrorCount UdpChecksumErrorCount PrbsFillOctetCount PrbsBitErrorCount PrbsBitErrorRatio PrbsErrorFrameCount FcsErrorFrameRate GeneratorCrcErrorFrameRate GeneratorL3ChecksumErrorRate GeneratorL4ChecksumErrorRate Ipv4ChecksumErrorRate TcpChecksumErrorRate UdpChecksumErrorRate PrbsBitErrorRate PrbsErrorFrameRate OutSeqFrameCount", \
    CountQuery="", \
    SqlString=" SELECT Port.Name AS 'Port Name', GeneratorPortResults.TotalFrameCount AS 'Total Tx Count (Frames)', AnalyzerPortResults.TotalFrameCount AS 'Total Rx Count (Frames)', AnalyzerPortResults.FcsErrorFrameCount AS 'Rx FCS Error Count (Frames)', GeneratorPortResults.GeneratorCrcErrorFrameCount AS 'Generator CRC Error Count (Frames)', GeneratorPortResults.GeneratorL3ChecksumErrorCount AS 'Generator L3 Checksum Error Count', GeneratorPortResults.GeneratorL4ChecksumErrorCount AS 'Generator L4 Checksum Error Count', AnalyzerPortResults.Ipv4ChecksumErrorCount AS 'Rx IPv4 Checksum Error Count', AnalyzerPortResults.TcpChecksumErrorCount AS 'Rx TCP Checksum Error Count', AnalyzerPortResults.UdpChecksumErrorCount AS 'Rx UDP Checksum Error Count', AnalyzerPortResults.PrbsFillOctetCount AS 'Rx PRBS Fill Octet Count', AnalyzerPortResults.PrbsBitErrorCount AS 'Rx PRBS Bit Error Count', coalesce(round(cast(AnalyzerPortResults.PrbsBitErrorCount as double)/cast((AnalyzerPortResults.PrbsFillOctetCount * 8) as double), 3), 0.0) as 'PRBS Bit Error Ratio', AnalyzerPortResults.PrbsErrorFrameCount AS 'Rx PRBS Error Frame Count' FROM Port, GeneratorPortResults, Generator, AnalyzerPortResults, Analyzer WHERE ( Generator.ParentHnd = Port.Handle AND Analyzer.ParentHnd = Port.Handle AND GeneratorPortResults.ParentHnd = Generator.Handle AND AnalyzerPortResults.ParentHnd = Analyzer.Handle AND Port.DataSetId = @DataSetId AND GeneratorPortResults.DataSetId = @DataSetId AND Generator.DataSetId = @DataSetId AND AnalyzerPortResults.DataSetId = @DataSetId AND Analyzer.DataSetId = @DataSetId  )", \
    UseCustomSqlString="TRUE", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="RealTimeResultGroupDefinition 39")

    RealTimeResultGroupDefinition_4 = stc.create("RealTimeResultGroupDefinition",under = ResultDataSet_1, \
    GroupName="Triggers", \
    GroupId="object://customgroup/ddcfebff-9e2d-49e4-8d4a-1cde4792f3c1/Triggers", \
    ColumnClassName="GeneratorPortResults AnalyzerPortResults AnalyzerPortResults AnalyzerPortResults AnalyzerPortResults AnalyzerPortResults AnalyzerPortResults AnalyzerPortResults AnalyzerPortResults AnalyzerPortResults AnalyzerPortResults AnalyzerPortResults AnalyzerPortResults AnalyzerPortResults AnalyzerPortResults AnalyzerPortResults AnalyzerPortResults AnalyzerPortResults AnalyzerPortResults AnalyzerPortResults", \
    ColumnPropertyName="TotalFrameCount TotalFrameCount Trigger1Count Trigger2Count Trigger3Count Trigger4Count Trigger5Count Trigger6Count Trigger7Count Trigger8Count ComboTriggerCount Trigger1Rate Trigger2Rate Trigger3Rate Trigger4Rate Trigger5Rate Trigger6Rate Trigger7Rate Trigger8Rate ComboTriggerRate", \
    CountQuery="", \
    SqlString="SELECT Port.Name AS 'Port Name', GeneratorPortResults.TotalFrameCount AS 'Total Tx Count (Frames)', AnalyzerPortResults.TotalFrameCount AS 'Total Rx Count (Frames)', AnalyzerPortResults.Trigger1Count AS 'Trigger 1', AnalyzerPortResults.Trigger2Count AS 'Trigger 2', AnalyzerPortResults.Trigger3Count AS 'Trigger 3', AnalyzerPortResults.Trigger4Count AS 'Trigger 4', AnalyzerPortResults.Trigger5Count AS 'Trigger 5', AnalyzerPortResults.Trigger6Count AS 'Trigger 6', AnalyzerPortResults.Trigger7Count AS 'Trigger 7', AnalyzerPortResults.Trigger8Count AS 'Trigger 8', AnalyzerPortResults.ComboTriggerCount AS 'ComboTrigger', AnalyzerPortResults.Trigger1Rate AS 'Trigger 1 Rate', AnalyzerPortResults.Trigger2Rate AS 'Trigger 2 Rate', AnalyzerPortResults.Trigger3Rate AS 'Trigger 3 Rate', AnalyzerPortResults.Trigger4Rate AS 'Trigger 4 Rate', AnalyzerPortResults.Trigger5Rate AS 'Trigger 5 Rate', AnalyzerPortResults.Trigger6Rate AS 'Trigger 6 Rate', AnalyzerPortResults.Trigger7Rate AS 'Trigger 7 Rate', AnalyzerPortResults.Trigger8Rate AS 'Trigger 8 Rate', AnalyzerPortResults.ComboTriggerRate AS 'ComboTrigger Rate' FROM Port, GeneratorPortResults, AnalyzerPortResults, Generator, Analyzer WHERE ( Generator.ParentHnd = Port.Handle AND Analyzer.ParentHnd = Port.Handle AND GeneratorPortResults.ParentHnd = Generator.Handle AND AnalyzerPortResults.ParentHnd = Analyzer.Handle AND Port.DataSetId = @DataSetId AND GeneratorPortResults.DataSetId = @DataSetId AND AnalyzerPortResults.DataSetId = @DataSetId AND Generator.DataSetId = @DataSetId AND Analyzer.DataSetId = @DataSetId  ) UNION SELECT ExternalDevicePort.Name AS 'Port Name', GeneratorPortResults.TotalFrameCount AS 'Total Tx Count (Frames)', AnalyzerPortResults.TotalFrameCount AS 'Total Rx Count (Frames)', AnalyzerPortResults.Trigger1Count AS 'Trigger 1', AnalyzerPortResults.Trigger2Count AS 'Trigger 2', AnalyzerPortResults.Trigger3Count AS 'Trigger 3', AnalyzerPortResults.Trigger4Count AS 'Trigger 4', AnalyzerPortResults.Trigger5Count AS 'Trigger 5', AnalyzerPortResults.Trigger6Count AS 'Trigger 6', AnalyzerPortResults.Trigger7Count AS 'Trigger 7', AnalyzerPortResults.Trigger8Count AS 'Trigger 8', AnalyzerPortResults.ComboTriggerCount AS 'ComboTrigger', AnalyzerPortResults.Trigger1Rate AS 'Trigger 1 Rate', AnalyzerPortResults.Trigger2Rate AS 'Trigger 2 Rate', AnalyzerPortResults.Trigger3Rate AS 'Trigger 3 Rate', AnalyzerPortResults.Trigger4Rate AS 'Trigger 4 Rate', AnalyzerPortResults.Trigger5Rate AS 'Trigger 5 Rate', AnalyzerPortResults.Trigger6Rate AS 'Trigger 6 Rate', AnalyzerPortResults.Trigger7Rate AS 'Trigger 7 Rate', AnalyzerPortResults.Trigger8Rate AS 'Trigger 8 Rate', AnalyzerPortResults.ComboTriggerRate AS 'ComboTrigger Rate' FROM ExternalDevicePort, GeneratorPortResults, AnalyzerPortResults, Port, Generator, Analyzer WHERE ( Generator.ParentHnd = Port.Handle AND Analyzer.ParentHnd = Port.Handle AND GeneratorPortResults.ParentHnd = Generator.Handle AND AnalyzerPortResults.ParentHnd = Analyzer.Handle AND ExternalDevicePort.DataSetId = @DataSetId AND GeneratorPortResults.DataSetId = @DataSetId AND AnalyzerPortResults.DataSetId = @DataSetId AND Port.DataSetId = @DataSetId AND Generator.DataSetId = @DataSetId AND Analyzer.DataSetId = @DataSetId  ) ", \
    UseCustomSqlString="FALSE", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="RealTimeResultGroupDefinition 40")

    RealTimeResultGroupDefinition_5 = stc.create("RealTimeResultGroupDefinition",under = ResultDataSet_1, \
    GroupName="Protocols", \
    GroupId="object://customgroup/3e090a0e-d3c7-413f-ad01-ccb4a21de519/Protocols", \
    ColumnClassName="GeneratorPortResults AnalyzerPortResults GeneratorPortResults GeneratorPortResults GeneratorPortResults GeneratorPortResults GeneratorPortResults GeneratorPortResults GeneratorPortResults AnalyzerPortResults AnalyzerPortResults AnalyzerPortResults AnalyzerPortResults AnalyzerPortResults AnalyzerPortResults AnalyzerPortResults AnalyzerPortResults GeneratorPortResults GeneratorPortResults GeneratorPortResults GeneratorPortResults GeneratorPortResults GeneratorPortResults GeneratorPortResults AnalyzerPortResults AnalyzerPortResults AnalyzerPortResults AnalyzerPortResults AnalyzerPortResults AnalyzerPortResults AnalyzerPortResults AnalyzerPortResults", \
    ColumnPropertyName="TotalFrameCount TotalFrameCount TotalIpv4FrameCount TotalIpv6FrameCount TotalMplsFrameCount GeneratorIpv4FrameCount GeneratorIpv6FrameCount GeneratorVlanFrameCount GeneratorMplsFrameCount Ipv4FrameCount Ipv6FrameCount TcpFrameCount UdpFrameCount MplsFrameCount IcmpFrameCount VlanFrameCount FcoeFrameCount TotalIpv4FrameRate TotalIpv6FrameRate TotalMplsFrameRate GeneratorIpv4FrameRate GeneratorIpv6FrameRate GeneratorVlanFrameRate GeneratorMplsFrameRate Ipv4FrameRate Ipv6FrameRate TcpFrameRate UdpFrameRate MplsFrameRate IcmpFrameRate VlanFrameRate FcoeFrameRate", \
    CountQuery="", \
    SqlString=" SELECT Port.Name AS 'Port Name', GeneratorPortResults.TotalFrameCount AS 'Total Tx Frame Count', AnalyzerPortResults.TotalFrameCount AS 'Total Rx Frame Count', GeneratorPortResults.TotalIpv4FrameCount AS 'Total Tx IPv4 Frame', GeneratorPortResults.TotalIpv6FrameCount AS 'Total Tx IPv6 Frame', GeneratorPortResults.TotalMplsFrameCount AS 'Total Tx MPLS Frame', GeneratorPortResults.GeneratorIpv4FrameCount AS 'Generator IPv4 Frame Count', GeneratorPortResults.GeneratorIpv6FrameCount AS 'Generator IPv6 Frame Count', GeneratorPortResults.GeneratorVlanFrameCount AS 'Generator VLAN Frame Count', GeneratorPortResults.GeneratorMplsFrameCount AS 'Generator MPLS Frame Count', AnalyzerPortResults.Ipv4FrameCount AS 'Rx IPv4 Frame Count', AnalyzerPortResults.Ipv6FrameCount AS 'Rx IPv6 Frame Count', AnalyzerPortResults.TcpFrameCount AS 'Rx TCP Frame Count', AnalyzerPortResults.UdpFrameCount AS 'Rx UDP Frame Count', AnalyzerPortResults.MplsFrameCount AS 'Rx MPLS Frame Count', AnalyzerPortResults.IcmpFrameCount AS 'Rx ICMP Frame Count', AnalyzerPortResults.VlanFrameCount AS 'Rx VLAN Frame Count', AnalyzerPortResults.FcoeFrameCount AS 'Rx FCoE Frame Count' FROM Port, GeneratorPortResults, Generator, AnalyzerPortResults, Analyzer WHERE ( Generator.ParentHnd = Port.Handle AND Analyzer.ParentHnd = Port.Handle AND GeneratorPortResults.ParentHnd = Generator.Handle AND AnalyzerPortResults.ParentHnd = Analyzer.Handle AND Port.DataSetId = @DataSetId AND GeneratorPortResults.DataSetId = @DataSetId AND Generator.DataSetId = @DataSetId AND AnalyzerPortResults.DataSetId = @DataSetId AND Analyzer.DataSetId = @DataSetId  )", \
    UseCustomSqlString="TRUE", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="RealTimeResultGroupDefinition 41")

    RealTimeResultColumnDefinition_78 = stc.create("RealTimeResultColumnDefinition",under = ResultDataSet_1, \
    ColumnClassName="GeneratorPortResults", \
    ColumnPropertyName="TotalIpv4FrameRate", \
    ColumnDescription="DescribeMe", \
    ColumnWidth="99", \
    ColumnUnits="17", \
    ColumnPrecision="2", \
    ColumnSortType="NONE", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="RealTimeResultColumnDefinition 88")

    RealTimeResultColumnDefinition_79 = stc.create("RealTimeResultColumnDefinition",under = ResultDataSet_1, \
    ColumnClassName="GeneratorPortResults", \
    ColumnPropertyName="TotalIpv6FrameRate", \
    ColumnDescription="", \
    ColumnWidth="101", \
    ColumnUnits="17", \
    ColumnPrecision="2", \
    ColumnSortType="NONE", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="RealTimeResultColumnDefinition 89")

    RealTimeResultColumnDefinition_80 = stc.create("RealTimeResultColumnDefinition",under = ResultDataSet_1, \
    ColumnClassName="GeneratorPortResults", \
    ColumnPropertyName="TotalMplsFrameRate", \
    ColumnDescription="DescribeMe", \
    ColumnWidth="90", \
    ColumnUnits="17", \
    ColumnPrecision="2", \
    ColumnSortType="NONE", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="RealTimeResultColumnDefinition 90")

    RealTimeResultColumnDefinition_81 = stc.create("RealTimeResultColumnDefinition",under = ResultDataSet_1, \
    ColumnClassName="GeneratorPortResults", \
    ColumnPropertyName="GeneratorIpv4FrameRate", \
    ColumnDescription="DescribeMe", \
    ColumnWidth="115", \
    ColumnUnits="17", \
    ColumnPrecision="2", \
    ColumnSortType="NONE", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="RealTimeResultColumnDefinition 91")

    RealTimeResultColumnDefinition_82 = stc.create("RealTimeResultColumnDefinition",under = ResultDataSet_1, \
    ColumnClassName="GeneratorPortResults", \
    ColumnPropertyName="GeneratorIpv6FrameRate", \
    ColumnDescription="DescribeMe", \
    ColumnWidth="117", \
    ColumnUnits="17", \
    ColumnPrecision="2", \
    ColumnSortType="NONE", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="RealTimeResultColumnDefinition 92")

    RealTimeResultColumnDefinition_83 = stc.create("RealTimeResultColumnDefinition",under = ResultDataSet_1, \
    ColumnClassName="GeneratorPortResults", \
    ColumnPropertyName="GeneratorVlanFrameRate", \
    ColumnDescription="DescribeMe", \
    ColumnWidth="127", \
    ColumnUnits="17", \
    ColumnPrecision="2", \
    ColumnSortType="NONE", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="RealTimeResultColumnDefinition 93")

    RealTimeResultColumnDefinition_84 = stc.create("RealTimeResultColumnDefinition",under = ResultDataSet_1, \
    ColumnClassName="GeneratorPortResults", \
    ColumnPropertyName="GeneratorMplsFrameRate", \
    ColumnDescription="DescribeMe", \
    ColumnWidth="125", \
    ColumnUnits="17", \
    ColumnPrecision="2", \
    ColumnSortType="NONE", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="RealTimeResultColumnDefinition 94")

    RealTimeResultColumnDefinition_85 = stc.create("RealTimeResultColumnDefinition",under = ResultDataSet_1, \
    ColumnClassName="AnalyzerPortResults", \
    ColumnPropertyName="Ipv4FrameRate", \
    ColumnDescription="", \
    ColumnWidth="114", \
    ColumnUnits="17", \
    ColumnPrecision="2", \
    ColumnSortType="NONE", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="RealTimeResultColumnDefinition 95")

    RealTimeResultColumnDefinition_86 = stc.create("RealTimeResultColumnDefinition",under = ResultDataSet_1, \
    ColumnClassName="AnalyzerPortResults", \
    ColumnPropertyName="Ipv6FrameRate", \
    ColumnDescription="", \
    ColumnWidth="109", \
    ColumnUnits="17", \
    ColumnPrecision="2", \
    ColumnSortType="NONE", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="RealTimeResultColumnDefinition 96")

    RealTimeResultColumnDefinition_87 = stc.create("RealTimeResultColumnDefinition",under = ResultDataSet_1, \
    ColumnClassName="AnalyzerPortResults", \
    ColumnPropertyName="TcpFrameRate", \
    ColumnDescription="", \
    ColumnWidth="77", \
    ColumnUnits="17", \
    ColumnPrecision="2", \
    ColumnSortType="NONE", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="RealTimeResultColumnDefinition 97")

    RealTimeResultColumnDefinition_88 = stc.create("RealTimeResultColumnDefinition",under = ResultDataSet_1, \
    ColumnClassName="AnalyzerPortResults", \
    ColumnPropertyName="UdpFrameRate", \
    ColumnDescription="", \
    ColumnWidth="84", \
    ColumnUnits="17", \
    ColumnPrecision="2", \
    ColumnSortType="NONE", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="RealTimeResultColumnDefinition 98")

    RealTimeResultColumnDefinition_89 = stc.create("RealTimeResultColumnDefinition",under = ResultDataSet_1, \
    ColumnClassName="AnalyzerPortResults", \
    ColumnPropertyName="MplsFrameRate", \
    ColumnDescription="", \
    ColumnWidth="86", \
    ColumnUnits="17", \
    ColumnPrecision="2", \
    ColumnSortType="NONE", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="RealTimeResultColumnDefinition 99")

    RealTimeResultGroupDefinition_6 = stc.create("RealTimeResultGroupDefinition",under = ResultDataSet_1, \
    GroupName="Undersize/Oversize/Jumbo", \
    GroupId="object://customgroup/06ce5837-a7ee-427b-96e8-10cca3ff961a/Undersize/Oversize/Jumbo", \
    ColumnClassName="GeneratorPortResults AnalyzerPortResults GeneratorPortResults AnalyzerPortResults GeneratorPortResults AnalyzerPortResults GeneratorPortResults AnalyzerPortResults AnalyzerPortResults GeneratorPortResults AnalyzerPortResults GeneratorPortResults AnalyzerPortResults GeneratorPortResults AnalyzerPortResults AnalyzerPortResults", \
    ColumnPropertyName="TotalFrameCount TotalFrameCount GeneratorUndersizeFrameCount UndersizeFrameCount GeneratorOversizeFrameCount OversizeFrameCount GeneratorJumboFrameCount JumboFrameCount PauseFrameCount GeneratorUndersizeFrameRate UndersizeFrameRate GeneratorOversizeFrameRate OversizeFrameRate GeneratorJumboFrameRate JumboFrameRate PauseFrameRate", \
    CountQuery="", \
    SqlString="SELECT Port.Name AS 'Port Name', GeneratorPortResults.TotalFrameCount AS 'Total Tx Count (Frames)', AnalyzerPortResults.TotalFrameCount AS 'Total Rx Count (Frames)', GeneratorPortResults.GeneratorUndersizeFrameCount AS 'Generator Undersize Count (Frames)', AnalyzerPortResults.UndersizeFrameCount AS 'Rx Undersize Frame Count (Frames)', GeneratorPortResults.GeneratorOversizeFrameCount AS 'Generator Oversize Count (Frames)', AnalyzerPortResults.OversizeFrameCount AS 'Rx Oversize Frame Count (Frames)', GeneratorPortResults.GeneratorJumboFrameCount AS 'Generator Jumbo Count (Frames)', AnalyzerPortResults.JumboFrameCount AS 'Rx Jumbo Frame Count (Frames)', AnalyzerPortResults.PauseFrameCount AS 'Rx Pause Frame Count (Frames)', GeneratorPortResults.GeneratorUndersizeFrameRate AS 'Generator Undersize Rate (fps)', AnalyzerPortResults.UndersizeFrameRate AS 'Rx Undersize Rate (fps)', GeneratorPortResults.GeneratorOversizeFrameRate AS 'Generator Oversize Rate (fps)', AnalyzerPortResults.OversizeFrameRate AS 'Rx Oversize Rate (fps)', GeneratorPortResults.GeneratorJumboFrameRate AS 'Generator Jumbo Frame Rate (fps)', AnalyzerPortResults.JumboFrameRate AS 'Rx Jumbo Rate (fps)', AnalyzerPortResults.PauseFrameRate AS 'Rx Pause Rate (fps)' FROM Port, GeneratorPortResults, AnalyzerPortResults, Generator, Analyzer WHERE ( Generator.ParentHnd = Port.Handle AND Analyzer.ParentHnd = Port.Handle AND GeneratorPortResults.ParentHnd = Generator.Handle AND AnalyzerPortResults.ParentHnd = Analyzer.Handle AND Port.DataSetId = @DataSetId AND GeneratorPortResults.DataSetId = @DataSetId AND AnalyzerPortResults.DataSetId = @DataSetId AND Generator.DataSetId = @DataSetId AND Analyzer.DataSetId = @DataSetId  ) UNION SELECT ExternalDevicePort.Name AS 'Port Name', GeneratorPortResults.TotalFrameCount AS 'Total Tx Count (Frames)', AnalyzerPortResults.TotalFrameCount AS 'Total Rx Count (Frames)', GeneratorPortResults.GeneratorUndersizeFrameCount AS 'Generator Undersize Count (Frames)', AnalyzerPortResults.UndersizeFrameCount AS 'Rx Undersize Frame Count (Frames)', GeneratorPortResults.GeneratorOversizeFrameCount AS 'Generator Oversize Count (Frames)', AnalyzerPortResults.OversizeFrameCount AS 'Rx Oversize Frame Count (Frames)', GeneratorPortResults.GeneratorJumboFrameCount AS 'Generator Jumbo Count (Frames)', AnalyzerPortResults.JumboFrameCount AS 'Rx Jumbo Frame Count (Frames)', AnalyzerPortResults.PauseFrameCount AS 'Rx Pause Frame Count (Frames)', GeneratorPortResults.GeneratorUndersizeFrameRate AS 'Generator Undersize Rate (fps)', AnalyzerPortResults.UndersizeFrameRate AS 'Rx Undersize Rate (fps)', GeneratorPortResults.GeneratorOversizeFrameRate AS 'Generator Oversize Rate (fps)', AnalyzerPortResults.OversizeFrameRate AS 'Rx Oversize Rate (fps)', GeneratorPortResults.GeneratorJumboFrameRate AS 'Generator Jumbo Frame Rate (fps)', AnalyzerPortResults.JumboFrameRate AS 'Rx Jumbo Rate (fps)', AnalyzerPortResults.PauseFrameRate AS 'Rx Pause Rate (fps)' FROM ExternalDevicePort, GeneratorPortResults, AnalyzerPortResults, Port, Generator, Analyzer WHERE ( Generator.ParentHnd = Port.Handle AND Analyzer.ParentHnd = Port.Handle AND GeneratorPortResults.ParentHnd = Generator.Handle AND AnalyzerPortResults.ParentHnd = Analyzer.Handle AND ExternalDevicePort.DataSetId = @DataSetId AND GeneratorPortResults.DataSetId = @DataSetId AND AnalyzerPortResults.DataSetId = @DataSetId AND Port.DataSetId = @DataSetId AND Generator.DataSetId = @DataSetId AND Analyzer.DataSetId = @DataSetId  ) ", \
    UseCustomSqlString="FALSE", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="RealTimeResultGroupDefinition 8")

    RealTimeResultColumnDefinition_90 = stc.create("RealTimeResultColumnDefinition",under = ResultDataSet_1, \
    ColumnClassName="AnalyzerPortResults", \
    ColumnPropertyName="IcmpFrameRate", \
    ColumnDescription="", \
    ColumnWidth="79", \
    ColumnUnits="17", \
    ColumnPrecision="2", \
    ColumnSortType="NONE", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="RealTimeResultColumnDefinition 100")

    RealTimeResultColumnDefinition_91 = stc.create("RealTimeResultColumnDefinition",under = ResultDataSet_1, \
    ColumnClassName="AnalyzerPortResults", \
    ColumnPropertyName="VlanFrameRate", \
    ColumnDescription="", \
    ColumnWidth="113", \
    ColumnUnits="17", \
    ColumnPrecision="2", \
    ColumnSortType="NONE", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="RealTimeResultColumnDefinition 101")

    RealTimeResultColumnDefinition_92 = stc.create("RealTimeResultColumnDefinition",under = ResultDataSet_1, \
    ColumnClassName="AnalyzerPortResults", \
    ColumnPropertyName="FcoeFrameRate", \
    ColumnDescription="", \
    ColumnWidth="93", \
    ColumnUnits="17", \
    ColumnPrecision="2", \
    ColumnSortType="NONE", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="RealTimeResultColumnDefinition 102")

    RealTimeResultColumnDefinition_93 = stc.create("RealTimeResultColumnDefinition",under = ResultDataSet_1, \
    ColumnClassName="GeneratorPortResults", \
    ColumnPropertyName="GeneratorUndersizeFrameCount", \
    ColumnDescription="", \
    ColumnWidth="200", \
    ColumnUnits="16", \
    ColumnPrecision="2", \
    ColumnSortType="NONE", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="RealTimeResultColumnDefinition 103")

    RealTimeResultColumnDefinition_94 = stc.create("RealTimeResultColumnDefinition",under = ResultDataSet_1, \
    ColumnClassName="AnalyzerPortResults", \
    ColumnPropertyName="UndersizeFrameCount", \
    ColumnDescription="", \
    ColumnWidth="198", \
    ColumnUnits="16", \
    ColumnPrecision="2", \
    ColumnSortType="NONE", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="RealTimeResultColumnDefinition 104")

    RealTimeResultColumnDefinition_95 = stc.create("RealTimeResultColumnDefinition",under = ResultDataSet_1, \
    ColumnClassName="GeneratorPortResults", \
    ColumnPropertyName="GeneratorOversizeFrameCount", \
    ColumnDescription="", \
    ColumnWidth="194", \
    ColumnUnits="16", \
    ColumnPrecision="2", \
    ColumnSortType="NONE", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="RealTimeResultColumnDefinition 613")

    RealTimeResultColumnDefinition_96 = stc.create("RealTimeResultColumnDefinition",under = ResultDataSet_1, \
    ColumnClassName="AnalyzerPortResults", \
    ColumnPropertyName="OversizeFrameCount", \
    ColumnDescription="", \
    ColumnWidth="192", \
    ColumnUnits="16", \
    ColumnPrecision="2", \
    ColumnSortType="NONE", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="RealTimeResultColumnDefinition 614")

    RealTimeResultColumnDefinition_97 = stc.create("RealTimeResultColumnDefinition",under = ResultDataSet_1, \
    ColumnClassName="GeneratorPortResults", \
    ColumnPropertyName="GeneratorJumboFrameCount", \
    ColumnDescription="", \
    ColumnWidth="185", \
    ColumnUnits="16", \
    ColumnPrecision="2", \
    ColumnSortType="NONE", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="RealTimeResultColumnDefinition 615")

    RealTimeResultColumnDefinition_98 = stc.create("RealTimeResultColumnDefinition",under = ResultDataSet_1, \
    ColumnClassName="AnalyzerPortResults", \
    ColumnPropertyName="JumboFrameCount", \
    ColumnDescription="", \
    ColumnWidth="182", \
    ColumnUnits="16", \
    ColumnPrecision="2", \
    ColumnSortType="NONE", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="RealTimeResultColumnDefinition 616")

    RealTimeResultColumnDefinition_99 = stc.create("RealTimeResultColumnDefinition",under = ResultDataSet_1, \
    ColumnClassName="AnalyzerPortResults", \
    ColumnPropertyName="PauseFrameCount", \
    ColumnDescription="", \
    ColumnWidth="179", \
    ColumnUnits="16", \
    ColumnPrecision="2", \
    ColumnSortType="NONE", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="RealTimeResultColumnDefinition 617")

    RealTimeResultColumnDefinition_100 = stc.create("RealTimeResultColumnDefinition",under = ResultDataSet_1, \
    ColumnClassName="GeneratorPortResults", \
    ColumnPropertyName="GeneratorUndersizeFrameRate", \
    ColumnDescription="", \
    ColumnWidth="172", \
    ColumnUnits="17", \
    ColumnPrecision="2", \
    ColumnSortType="NONE", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="RealTimeResultColumnDefinition 618")

    RealTimeResultColumnDefinition_101 = stc.create("RealTimeResultColumnDefinition",under = ResultDataSet_1, \
    ColumnClassName="AnalyzerPortResults", \
    ColumnPropertyName="UndersizeFrameRate", \
    ColumnDescription="", \
    ColumnWidth="135", \
    ColumnUnits="17", \
    ColumnPrecision="2", \
    ColumnSortType="NONE", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="RealTimeResultColumnDefinition 619")

    RealTimeResultColumnDefinition_102 = stc.create("RealTimeResultColumnDefinition",under = ResultDataSet_1, \
    ColumnClassName="GeneratorPortResults", \
    ColumnPropertyName="GeneratorOversizeFrameRate", \
    ColumnDescription="", \
    ColumnWidth="166", \
    ColumnUnits="17", \
    ColumnPrecision="2", \
    ColumnSortType="NONE", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="RealTimeResultColumnDefinition 127")

    RealTimeResultColumnDefinition_103 = stc.create("RealTimeResultColumnDefinition",under = ResultDataSet_1, \
    ColumnClassName="AnalyzerPortResults", \
    ColumnPropertyName="OversizeFrameRate", \
    ColumnDescription="", \
    ColumnWidth="129", \
    ColumnUnits="17", \
    ColumnPrecision="2", \
    ColumnSortType="NONE", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="RealTimeResultColumnDefinition 128")

    RealTimeResultColumnDefinition_104 = stc.create("RealTimeResultColumnDefinition",under = ResultDataSet_1, \
    ColumnClassName="GeneratorPortResults", \
    ColumnPropertyName="GeneratorJumboFrameRate", \
    ColumnDescription="", \
    ColumnWidth="191", \
    ColumnUnits="17", \
    ColumnPrecision="2", \
    ColumnSortType="NONE", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="RealTimeResultColumnDefinition 129")

    RealTimeResultColumnDefinition_105 = stc.create("RealTimeResultColumnDefinition",under = ResultDataSet_1, \
    ColumnClassName="AnalyzerPortResults", \
    ColumnPropertyName="JumboFrameRate", \
    ColumnDescription="", \
    ColumnWidth="119", \
    ColumnUnits="17", \
    ColumnPrecision="2", \
    ColumnSortType="NONE", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="RealTimeResultColumnDefinition 130")

    RealTimeResultColumnDefinition_106 = stc.create("RealTimeResultColumnDefinition",under = ResultDataSet_1, \
    ColumnClassName="AnalyzerPortResults", \
    ColumnPropertyName="PauseFrameRate", \
    ColumnDescription="", \
    ColumnWidth="89", \
    ColumnUnits="17", \
    ColumnPrecision="2", \
    ColumnSortType="NONE", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="RealTimeResultColumnDefinition 131")

    RealTimeResultColumnDefinition_107 = stc.create("RealTimeResultColumnDefinition",under = ResultDataSet_1, \
    ColumnClassName="GeneratorPortResults", \
    ColumnPropertyName="PfcFrameCount", \
    ColumnDescription="", \
    ColumnWidth="96", \
    ColumnUnits="16", \
    ColumnPrecision="2", \
    ColumnSortType="NONE", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="RealTimeResultColumnDefinition 132")

    RealTimeResultColumnDefinition_108 = stc.create("RealTimeResultColumnDefinition",under = ResultDataSet_1, \
    ColumnClassName="AnalyzerPortResults", \
    ColumnPropertyName="PfcFrameCount", \
    ColumnDescription="", \
    ColumnWidth="87", \
    ColumnUnits="16", \
    ColumnPrecision="2", \
    ColumnSortType="NONE", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="RealTimeResultColumnDefinition 133")

    RealTimeResultColumnDefinition_109 = stc.create("RealTimeResultColumnDefinition",under = ResultDataSet_1, \
    ColumnClassName="AnalyzerPortResults", \
    ColumnPropertyName="PfcFrameRate", \
    ColumnDescription="", \
    ColumnWidth="93", \
    ColumnUnits="17", \
    ColumnPrecision="2", \
    ColumnSortType="NONE", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="RealTimeResultColumnDefinition 134")

    RealTimeResultColumnDefinition_110 = stc.create("RealTimeResultColumnDefinition",under = ResultDataSet_1, \
    ColumnClassName="GeneratorPortResults", \
    ColumnPropertyName="PfcPri0FrameCount", \
    ColumnDescription="", \
    ColumnWidth="108", \
    ColumnUnits="16", \
    ColumnPrecision="2", \
    ColumnSortType="NONE", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="RealTimeResultColumnDefinition 135")

    RealTimeResultColumnDefinition_111 = stc.create("RealTimeResultColumnDefinition",under = ResultDataSet_1, \
    ColumnClassName="GeneratorPortResults", \
    ColumnPropertyName="PfcPri1FrameCount", \
    ColumnDescription="", \
    ColumnWidth="108", \
    ColumnUnits="16", \
    ColumnPrecision="2", \
    ColumnSortType="NONE", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="RealTimeResultColumnDefinition 136")

    RealTimeResultColumnDefinition_112 = stc.create("RealTimeResultColumnDefinition",under = ResultDataSet_1, \
    ColumnClassName="GeneratorPortResults", \
    ColumnPropertyName="PfcPri2FrameCount", \
    ColumnDescription="", \
    ColumnWidth="108", \
    ColumnUnits="16", \
    ColumnPrecision="2", \
    ColumnSortType="NONE", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="RealTimeResultColumnDefinition 137")

    RealTimeResultColumnDefinition_113 = stc.create("RealTimeResultColumnDefinition",under = ResultDataSet_1, \
    ColumnClassName="GeneratorPortResults", \
    ColumnPropertyName="PfcPri3FrameCount", \
    ColumnDescription="", \
    ColumnWidth="108", \
    ColumnUnits="16", \
    ColumnPrecision="2", \
    ColumnSortType="NONE", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="RealTimeResultColumnDefinition 138")

    RealTimeResultColumnDefinition_114 = stc.create("RealTimeResultColumnDefinition",under = ResultDataSet_1, \
    ColumnClassName="GeneratorPortResults", \
    ColumnPropertyName="PfcPri4FrameCount", \
    ColumnDescription="", \
    ColumnWidth="108", \
    ColumnUnits="16", \
    ColumnPrecision="2", \
    ColumnSortType="NONE", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="RealTimeResultColumnDefinition 139")

    RealTimeResultColumnDefinition_115 = stc.create("RealTimeResultColumnDefinition",under = ResultDataSet_1, \
    ColumnClassName="GeneratorPortResults", \
    ColumnPropertyName="PfcPri5FrameCount", \
    ColumnDescription="", \
    ColumnWidth="108", \
    ColumnUnits="16", \
    ColumnPrecision="2", \
    ColumnSortType="NONE", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="RealTimeResultColumnDefinition 140")

    RealTimeResultColumnDefinition_116 = stc.create("RealTimeResultColumnDefinition",under = ResultDataSet_1, \
    ColumnClassName="GeneratorPortResults", \
    ColumnPropertyName="PfcPri6FrameCount", \
    ColumnDescription="", \
    ColumnWidth="108", \
    ColumnUnits="16", \
    ColumnPrecision="2", \
    ColumnSortType="NONE", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="RealTimeResultColumnDefinition 141")

    RealTimeResultColumnDefinition_117 = stc.create("RealTimeResultColumnDefinition",under = ResultDataSet_1, \
    ColumnClassName="GeneratorPortResults", \
    ColumnPropertyName="PfcPri7FrameCount", \
    ColumnDescription="", \
    ColumnWidth="108", \
    ColumnUnits="16", \
    ColumnPrecision="2", \
    ColumnSortType="NONE", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="RealTimeResultColumnDefinition 142")

    RealTimeResultColumnDefinition_118 = stc.create("RealTimeResultColumnDefinition",under = ResultDataSet_1, \
    ColumnClassName="AnalyzerPortResults", \
    ColumnPropertyName="PfcPri0FrameCount", \
    ColumnDescription="", \
    ColumnWidth="109", \
    ColumnUnits="16", \
    ColumnPrecision="2", \
    ColumnSortType="NONE", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="RealTimeResultColumnDefinition 143")

    RealTimeResultColumnDefinition_119 = stc.create("RealTimeResultColumnDefinition",under = ResultDataSet_1, \
    ColumnClassName="AnalyzerPortResults", \
    ColumnPropertyName="PfcPri1FrameCount", \
    ColumnDescription="", \
    ColumnWidth="109", \
    ColumnUnits="16", \
    ColumnPrecision="2", \
    ColumnSortType="NONE", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="RealTimeResultColumnDefinition 144")

    RealTimeResultColumnDefinition_120 = stc.create("RealTimeResultColumnDefinition",under = ResultDataSet_1, \
    ColumnClassName="AnalyzerPortResults", \
    ColumnPropertyName="PfcPri2FrameCount", \
    ColumnDescription="", \
    ColumnWidth="109", \
    ColumnUnits="16", \
    ColumnPrecision="2", \
    ColumnSortType="NONE", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="RealTimeResultColumnDefinition 145")

    RealTimeResultColumnDefinition_121 = stc.create("RealTimeResultColumnDefinition",under = ResultDataSet_1, \
    ColumnClassName="AnalyzerPortResults", \
    ColumnPropertyName="PfcPri3FrameCount", \
    ColumnDescription="", \
    ColumnWidth="109", \
    ColumnUnits="16", \
    ColumnPrecision="2", \
    ColumnSortType="NONE", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="RealTimeResultColumnDefinition 146")

    RealTimeResultColumnDefinition_122 = stc.create("RealTimeResultColumnDefinition",under = ResultDataSet_1, \
    ColumnClassName="AnalyzerPortResults", \
    ColumnPropertyName="PfcPri4FrameCount", \
    ColumnDescription="", \
    ColumnWidth="109", \
    ColumnUnits="16", \
    ColumnPrecision="2", \
    ColumnSortType="NONE", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="RealTimeResultColumnDefinition 147")

    RealTimeResultGroupDefinition_7 = stc.create("RealTimeResultGroupDefinition",under = ResultDataSet_1, \
    GroupName="PFC Counters", \
    GroupId="object://customgroup/ce2848b9-5f04-419d-8809-030032c630e4/PFC Counters", \
    ColumnClassName="GeneratorPortResults AnalyzerPortResults AnalyzerPortResults GeneratorPortResults GeneratorPortResults GeneratorPortResults GeneratorPortResults GeneratorPortResults GeneratorPortResults GeneratorPortResults GeneratorPortResults AnalyzerPortResults AnalyzerPortResults AnalyzerPortResults AnalyzerPortResults AnalyzerPortResults AnalyzerPortResults AnalyzerPortResults AnalyzerPortResults", \
    ColumnPropertyName="PfcFrameCount PfcFrameCount PfcFrameRate PfcPri0FrameCount PfcPri1FrameCount PfcPri2FrameCount PfcPri3FrameCount PfcPri4FrameCount PfcPri5FrameCount PfcPri6FrameCount PfcPri7FrameCount PfcPri0FrameCount PfcPri1FrameCount PfcPri2FrameCount PfcPri3FrameCount PfcPri4FrameCount PfcPri5FrameCount PfcPri6FrameCount PfcPri7FrameCount", \
    CountQuery="", \
    SqlString="SELECT Port.Name AS 'Port Name', GeneratorPortResults.PfcFrameCount AS 'Tx PFC Count (Frames)', AnalyzerPortResults.PfcFrameCount AS 'Rx PFC Count (Frames)', GeneratorPortResults.PfcPri0FrameCount AS 'Tx PFC Priority0 Count (Frames)', GeneratorPortResults.PfcPri1FrameCount AS 'Tx PFC Priority1 Count (Frames)', GeneratorPortResults.PfcPri2FrameCount AS 'Tx PFC Priority2 Count (Frames)', GeneratorPortResults.PfcPri3FrameCount AS 'Tx PFC Priority3 Count (Frames)', GeneratorPortResults.PfcPri4FrameCount AS 'Tx PFC Priority4 Count (Frames)', GeneratorPortResults.PfcPri5FrameCount AS 'Tx PFC Priority5 Count (Frames)', GeneratorPortResults.PfcPri6FrameCount AS 'Tx PFC Priority6 Count (Frames)', GeneratorPortResults.PfcPri7FrameCount AS 'Tx PFC Priority7 Count (Frames)', AnalyzerPortResults.PfcPri0FrameCount AS 'Rx PFC Priority0 Count (Frames)', AnalyzerPortResults.PfcPri1FrameCount AS 'Rx PFC Priority1 Count (Frames)', AnalyzerPortResults.PfcPri2FrameCount AS 'Rx PFC Priority2 Count (Frames)', AnalyzerPortResults.PfcPri3FrameCount AS 'Rx PFC Priority3 Count (Frames)', AnalyzerPortResults.PfcPri4FrameCount AS 'Rx PFC Priority4 Count (Frames)', AnalyzerPortResults.PfcPri5FrameCount AS 'Rx PFC Priority5 Count (Frames)', AnalyzerPortResults.PfcPri6FrameCount AS 'Rx PFC Priority6 Count (Frames)', AnalyzerPortResults.PfcPri7FrameCount AS 'Rx PFC Priority7 Count (Frames)', AnalyzerPortResults.PfcPri0Quanta AS 'Rx PFC Priority0 Quanta', AnalyzerPortResults.PfcPri1Quanta AS 'Rx PFC Priority1 Quanta', AnalyzerPortResults.PfcPri2Quanta AS 'Rx PFC Priority2 Quanta', AnalyzerPortResults.PfcPri3Quanta AS 'Rx PFC Priority3 Quanta', AnalyzerPortResults.PfcPri4Quanta AS 'Rx PFC Priority4 Quanta', AnalyzerPortResults.PfcPri5Quanta AS 'Rx PFC Priority5 Quanta', AnalyzerPortResults.PfcPri6Quanta AS 'Rx PFC Priority6 Quanta', AnalyzerPortResults.PfcPri7Quanta AS 'Rx PFC Priority7 Quanta' FROM Port, GeneratorPortResults, AnalyzerPortResults, Generator, Analyzer WHERE ( Generator.ParentHnd = Port.Handle AND Analyzer.ParentHnd = Port.Handle AND GeneratorPortResults.ParentHnd = Generator.Handle AND AnalyzerPortResults.ParentHnd = Analyzer.Handle AND Port.DataSetId = @DataSetId AND GeneratorPortResults.DataSetId = @DataSetId AND AnalyzerPortResults.DataSetId = @DataSetId AND Generator.DataSetId = @DataSetId AND Analyzer.DataSetId = @DataSetId  )", \
    UseCustomSqlString="TRUE", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="RealTimeResultGroupDefinition 9")

    RealTimeResultColumnDefinition_123 = stc.create("RealTimeResultColumnDefinition",under = ResultDataSet_1, \
    ColumnClassName="AnalyzerPortResults", \
    ColumnPropertyName="PfcPri5FrameCount", \
    ColumnDescription="", \
    ColumnWidth="109", \
    ColumnUnits="16", \
    ColumnPrecision="2", \
    ColumnSortType="NONE", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="RealTimeResultColumnDefinition 147")

    RealTimeResultColumnDefinition_124 = stc.create("RealTimeResultColumnDefinition",under = ResultDataSet_1, \
    ColumnClassName="AnalyzerPortResults", \
    ColumnPropertyName="PfcPri6FrameCount", \
    ColumnDescription="", \
    ColumnWidth="109", \
    ColumnUnits="16", \
    ColumnPrecision="2", \
    ColumnSortType="NONE", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="RealTimeResultColumnDefinition 147")

    RealTimeResultColumnDefinition_125 = stc.create("RealTimeResultColumnDefinition",under = ResultDataSet_1, \
    ColumnClassName="AnalyzerPortResults", \
    ColumnPropertyName="PfcPri7FrameCount", \
    ColumnDescription="", \
    ColumnWidth="109", \
    ColumnUnits="16", \
    ColumnPrecision="2", \
    ColumnSortType="NONE", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="RealTimeResultColumnDefinition 147")

    RealTimeResultColumnDefinition_126 = stc.create("RealTimeResultColumnDefinition",under = ResultDataSet_1, \
    ColumnClassName="AnalyzerPortResults", \
    ColumnPropertyName="UserDefinedFrameCount1", \
    ColumnDescription="", \
    ColumnWidth="109", \
    ColumnUnits="16", \
    ColumnPrecision="2", \
    ColumnSortType="NONE", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="RealTimeResultColumnDefinition 147")

    RealTimeResultColumnDefinition_127 = stc.create("RealTimeResultColumnDefinition",under = ResultDataSet_1, \
    ColumnClassName="AnalyzerPortResults", \
    ColumnPropertyName="UserDefinedFrameRate1", \
    ColumnDescription="", \
    ColumnWidth="109", \
    ColumnUnits="17", \
    ColumnPrecision="2", \
    ColumnSortType="NONE", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="RealTimeResultColumnDefinition 147")

    RealTimeResultColumnDefinition_128 = stc.create("RealTimeResultColumnDefinition",under = ResultDataSet_1, \
    ColumnClassName="AnalyzerPortResults", \
    ColumnPropertyName="UserDefinedFrameCount2", \
    ColumnDescription="", \
    ColumnWidth="109", \
    ColumnUnits="16", \
    ColumnPrecision="2", \
    ColumnSortType="NONE", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="RealTimeResultColumnDefinition 147")

    RealTimeResultColumnDefinition_129 = stc.create("RealTimeResultColumnDefinition",under = ResultDataSet_1, \
    ColumnClassName="AnalyzerPortResults", \
    ColumnPropertyName="UserDefinedFrameRate2", \
    ColumnDescription="", \
    ColumnWidth="109", \
    ColumnUnits="17", \
    ColumnPrecision="2", \
    ColumnSortType="NONE", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="RealTimeResultColumnDefinition 147")

    RealTimeResultColumnDefinition_130 = stc.create("RealTimeResultColumnDefinition",under = ResultDataSet_1, \
    ColumnClassName="AnalyzerPortResults", \
    ColumnPropertyName="UserDefinedFrameCount3", \
    ColumnDescription="", \
    ColumnWidth="135", \
    ColumnUnits="16", \
    ColumnPrecision="2", \
    ColumnSortType="NONE", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="RealTimeResultColumnDefinition 147")

    RealTimeResultColumnDefinition_131 = stc.create("RealTimeResultColumnDefinition",under = ResultDataSet_1, \
    ColumnClassName="AnalyzerPortResults", \
    ColumnPropertyName="UserDefinedFrameRate3", \
    ColumnDescription="", \
    ColumnWidth="135", \
    ColumnUnits="17", \
    ColumnPrecision="2", \
    ColumnSortType="NONE", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="RealTimeResultColumnDefinition 147")

    RealTimeResultColumnDefinition_132 = stc.create("RealTimeResultColumnDefinition",under = ResultDataSet_1, \
    ColumnClassName="AnalyzerPortResults", \
    ColumnPropertyName="UserDefinedFrameCount4", \
    ColumnDescription="", \
    ColumnWidth="135", \
    ColumnUnits="16", \
    ColumnPrecision="2", \
    ColumnSortType="NONE", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="RealTimeResultColumnDefinition 147")

    RealTimeResultColumnDefinition_133 = stc.create("RealTimeResultColumnDefinition",under = ResultDataSet_1, \
    ColumnClassName="AnalyzerPortResults", \
    ColumnPropertyName="UserDefinedFrameRate4", \
    ColumnDescription="", \
    ColumnWidth="135", \
    ColumnUnits="17", \
    ColumnPrecision="2", \
    ColumnSortType="NONE", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="RealTimeResultColumnDefinition 147")

    RealTimeResultColumnDefinition_134 = stc.create("RealTimeResultColumnDefinition",under = ResultDataSet_1, \
    ColumnClassName="AnalyzerPortResults", \
    ColumnPropertyName="UserDefinedFrameCount5", \
    ColumnDescription="", \
    ColumnWidth="135", \
    ColumnUnits="16", \
    ColumnPrecision="2", \
    ColumnSortType="NONE", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="RealTimeResultColumnDefinition 147")

    RealTimeResultColumnDefinition_135 = stc.create("RealTimeResultColumnDefinition",under = ResultDataSet_1, \
    ColumnClassName="AnalyzerPortResults", \
    ColumnPropertyName="UserDefinedFrameRate5", \
    ColumnDescription="", \
    ColumnWidth="135", \
    ColumnUnits="17", \
    ColumnPrecision="2", \
    ColumnSortType="NONE", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="RealTimeResultColumnDefinition 147")

    RealTimeResultColumnDefinition_136 = stc.create("RealTimeResultColumnDefinition",under = ResultDataSet_1, \
    ColumnClassName="AnalyzerPortResults", \
    ColumnPropertyName="UserDefinedFrameCount6", \
    ColumnDescription="", \
    ColumnWidth="135", \
    ColumnUnits="16", \
    ColumnPrecision="2", \
    ColumnSortType="NONE", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="RealTimeResultColumnDefinition 147")

    RealTimeResultColumnDefinition_137 = stc.create("RealTimeResultColumnDefinition",under = ResultDataSet_1, \
    ColumnClassName="AnalyzerPortResults", \
    ColumnPropertyName="UserDefinedFrameRate6", \
    ColumnDescription="", \
    ColumnWidth="135", \
    ColumnUnits="17", \
    ColumnPrecision="2", \
    ColumnSortType="NONE", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="RealTimeResultColumnDefinition 147")

    RealTimeResultGroupDefinition_8 = stc.create("RealTimeResultGroupDefinition",under = ResultDataSet_1, \
    GroupName="User Defined", \
    GroupId="object://customgroup/45684926-5012-4d7b-a560-70e552840cbb/User Defined", \
    ColumnClassName="AnalyzerPortResults AnalyzerPortResults AnalyzerPortResults AnalyzerPortResults AnalyzerPortResults AnalyzerPortResults AnalyzerPortResults AnalyzerPortResults AnalyzerPortResults AnalyzerPortResults AnalyzerPortResults AnalyzerPortResults", \
    ColumnPropertyName="UserDefinedFrameCount1 UserDefinedFrameRate1 UserDefinedFrameCount2 UserDefinedFrameRate2 UserDefinedFrameCount3 UserDefinedFrameRate3 UserDefinedFrameCount4 UserDefinedFrameRate4 UserDefinedFrameCount5 UserDefinedFrameRate5 UserDefinedFrameCount6 UserDefinedFrameRate6", \
    CountQuery="", \
    SqlString="SELECT Port.Name AS 'Port Name', GeneratorPortResults.TotalFrameCount AS 'Total Tx Count (Frames)', AnalyzerPortResults.TotalFrameCount AS 'Total Rx Count (Frames)', AnalyzerPortResults.UserDefinedFrameCount1 AS 'User Defined Capture Frame Count 1 (Frames)', AnalyzerPortResults.UserDefinedFrameCount2 AS 'User Defined Capture Frame Count 2 (Frames)', AnalyzerPortResults.UserDefinedFrameCount3 AS 'User Defined Capture Frame Count 3 (Frames)', AnalyzerPortResults.UserDefinedFrameCount4 AS 'User Defined Capture Frame Count 4 (Frames)', AnalyzerPortResults.UserDefinedFrameCount5 AS 'User Defined Capture Frame Count 5 (Frames)', AnalyzerPortResults.UserDefinedFrameCount6 AS 'User Defined Capture Frame Count 6 (Frames)'  FROM Port, GeneratorPortResults, Generator, AnalyzerPortResults, Analyzer WHERE ( Generator.ParentHnd = Port.Handle AND Analyzer.ParentHnd = Port.Handle AND GeneratorPortResults.ParentHnd = Generator.Handle AND AnalyzerPortResults.ParentHnd = Analyzer.Handle AND Port.DataSetId = @DataSetId AND GeneratorPortResults.DataSetId = @DataSetId AND Generator.DataSetId = @DataSetId AND AnalyzerPortResults.DataSetId = @DataSetId AND Analyzer.DataSetId = @DataSetId  )", \
    UseCustomSqlString="TRUE", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="RealTimeResultGroupDefinition 14")

    RealTimeResultColumnDefinition_138 = stc.create("RealTimeResultColumnDefinition",under = ResultDataSet_1, \
    ColumnClassName="AnalyzerPortResults", \
    ColumnPropertyName="DroppedFrameCount", \
    ColumnDescription="", \
    ColumnWidth="0", \
    ColumnUnits="16", \
    ColumnPrecision="2", \
    ColumnSortType="NONE", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="RealTimeResultColumnDefinition 140")

    RealTimeResultColumnDefinition_139 = stc.create("RealTimeResultColumnDefinition",under = ResultDataSet_1, \
    ColumnClassName="AnalyzerPortResults", \
    ColumnPropertyName="InOrderFrameCount", \
    ColumnDescription="", \
    ColumnWidth="0", \
    ColumnUnits="16", \
    ColumnPrecision="2", \
    ColumnSortType="NONE", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="RealTimeResultColumnDefinition 141")

    RealTimeResultColumnDefinition_140 = stc.create("RealTimeResultColumnDefinition",under = ResultDataSet_1, \
    ColumnClassName="AnalyzerPortResults", \
    ColumnPropertyName="ReorderedFrameCount", \
    ColumnDescription="", \
    ColumnWidth="0", \
    ColumnUnits="16", \
    ColumnPrecision="2", \
    ColumnSortType="NONE", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="RealTimeResultColumnDefinition 139")

    RealTimeResultColumnDefinition_141 = stc.create("RealTimeResultColumnDefinition",under = ResultDataSet_1, \
    ColumnClassName="AnalyzerPortResults", \
    ColumnPropertyName="DuplicateFrameCount", \
    ColumnDescription="", \
    ColumnWidth="0", \
    ColumnUnits="16", \
    ColumnPrecision="2", \
    ColumnSortType="NONE", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="RealTimeResultColumnDefinition 142")

    RealTimeResultColumnDefinition_142 = stc.create("RealTimeResultColumnDefinition",under = ResultDataSet_1, \
    ColumnClassName="AnalyzerPortResults", \
    ColumnPropertyName="LateFrameCount", \
    ColumnDescription="", \
    ColumnWidth="0", \
    ColumnUnits="16", \
    ColumnPrecision="2", \
    ColumnSortType="NONE", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="RealTimeResultColumnDefinition 143")

    RealTimeResultGroupDefinition_9 = stc.create("RealTimeResultGroupDefinition",under = ResultDataSet_1, \
    GroupName="Advanced Sequencing", \
    GroupId="object://customgroup/d775c482-4220-4044-b3d8-d0980146f9dc/Advanced Sequencing", \
    ColumnClassName="AnalyzerPortResults AnalyzerPortResults AnalyzerPortResults AnalyzerPortResults AnalyzerPortResults", \
    ColumnPropertyName="DroppedFrameCount InOrderFrameCount ReorderedFrameCount DuplicateFrameCount LateFrameCount", \
    CountQuery="", \
    SqlString="SELECT Port.Name AS 'Port Name', AnalyzerPortResults.DroppedFrameCount AS 'Dropped Count (Frames)', AnalyzerPortResults.InOrderFrameCount AS 'In-order Count (Frames)', AnalyzerPortResults.ReorderedFrameCount AS 'Reordered Count (Frames)', AnalyzerPortResults.DuplicateFrameCount AS 'Duplicate Count (Frames)', AnalyzerPortResults.LateFrameCount AS 'Late Count (Frames)' FROM Port, AnalyzerPortResults, Analyzer WHERE ( Analyzer.ParentHnd = Port.Handle AND AnalyzerPortResults.ParentHnd = Analyzer.Handle AND Port.DataSetId = @DataSetId AND AnalyzerPortResults.DataSetId = @DataSetId AND Analyzer.DataSetId = @DataSetId  ) UNION SELECT ExternalDevicePort.Name AS 'Port Name', AnalyzerPortResults.DroppedFrameCount AS 'Dropped Count (Frames)', AnalyzerPortResults.InOrderFrameCount AS 'In-order Count (Frames)', AnalyzerPortResults.ReorderedFrameCount AS 'Reordered Count (Frames)', AnalyzerPortResults.DuplicateFrameCount AS 'Duplicate Count (Frames)', AnalyzerPortResults.LateFrameCount AS 'Late Count (Frames)' FROM ExternalDevicePort, AnalyzerPortResults, Port, Analyzer WHERE ( Analyzer.ParentHnd = Port.Handle AND AnalyzerPortResults.ParentHnd = Analyzer.Handle AND ExternalDevicePort.DataSetId = @DataSetId AND AnalyzerPortResults.DataSetId = @DataSetId AND Port.DataSetId = @DataSetId AND Analyzer.DataSetId = @DataSetId  ) ", \
    UseCustomSqlString="FALSE", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="RealTimeResultGroupDefinition 9")

    RealTimeResultColumnDefinition_143 = stc.create("RealTimeResultColumnDefinition",under = ResultDataSet_1, \
    ColumnClassName="AnalyzerPortResults", \
    ColumnPropertyName="CorrectedRsFecErrorCount", \
    ColumnDescription="", \
    ColumnWidth="0", \
    ColumnUnits="28", \
    ColumnPrecision="2", \
    ColumnSortType="NONE", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="RealTimeResultColumnDefinition 144")

    RealTimeResultColumnDefinition_144 = stc.create("RealTimeResultColumnDefinition",under = ResultDataSet_1, \
    ColumnClassName="AnalyzerPortResults", \
    ColumnPropertyName="UncorrectedRsFecErrorCount", \
    ColumnDescription="", \
    ColumnWidth="0", \
    ColumnUnits="28", \
    ColumnPrecision="2", \
    ColumnSortType="NONE", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="RealTimeResultColumnDefinition 145")

    RealTimeResultColumnDefinition_145 = stc.create("RealTimeResultColumnDefinition",under = ResultDataSet_1, \
    ColumnClassName="AnalyzerPortResults", \
    ColumnPropertyName="CorrectedRsFecSymbols", \
    ColumnDescription="", \
    ColumnWidth="0", \
    ColumnUnits="0", \
    ColumnPrecision="2", \
    ColumnSortType="NONE", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="RealTimeResultColumnDefinition 146")

    RealTimeResultColumnDefinition_146 = stc.create("RealTimeResultColumnDefinition",under = ResultDataSet_1, \
    ColumnClassName="AnalyzerPortResults", \
    ColumnPropertyName="CorrectedBaseRFecErrorCount", \
    ColumnDescription="", \
    ColumnWidth="0", \
    ColumnUnits="28", \
    ColumnPrecision="2", \
    ColumnSortType="NONE", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="RealTimeResultColumnDefinition 147")

    RealTimeResultColumnDefinition_147 = stc.create("RealTimeResultColumnDefinition",under = ResultDataSet_1, \
    ColumnClassName="AnalyzerPortResults", \
    ColumnPropertyName="UncorrectedBaseRFecErrorCount", \
    ColumnDescription="", \
    ColumnWidth="0", \
    ColumnUnits="28", \
    ColumnPrecision="2", \
    ColumnSortType="NONE", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="RealTimeResultColumnDefinition 148")

    RealTimeResultColumnDefinition_148 = stc.create("RealTimeResultColumnDefinition",under = ResultDataSet_1, \
    ColumnClassName="AnalyzerPortResults", \
    ColumnPropertyName="PreRsFecSerRate", \
    ColumnDescription="", \
    ColumnWidth="0", \
    ColumnUnits="29", \
    ColumnPrecision="2", \
    ColumnSortType="NONE", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="RealTimeResultColumnDefinition 149")

    RealTimeResultColumnDefinition_149 = stc.create("RealTimeResultColumnDefinition",under = ResultDataSet_1, \
    ColumnClassName="AnalyzerPortResults", \
    ColumnPropertyName="PostRsFecSerRate", \
    ColumnDescription="", \
    ColumnWidth="0", \
    ColumnUnits="29", \
    ColumnPrecision="2", \
    ColumnSortType="NONE", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="RealTimeResultColumnDefinition 150")

    RealTimeResultColumnDefinition_150 = stc.create("RealTimeResultColumnDefinition",under = ResultDataSet_1, \
    ColumnClassName="AnalyzerPortResults", \
    ColumnPropertyName="PreBaseRFecSerRate", \
    ColumnDescription="", \
    ColumnWidth="0", \
    ColumnUnits="29", \
    ColumnPrecision="2", \
    ColumnSortType="NONE", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="RealTimeResultColumnDefinition 151")

    RealTimeResultColumnDefinition_151 = stc.create("RealTimeResultColumnDefinition",under = ResultDataSet_1, \
    ColumnClassName="AnalyzerPortResults", \
    ColumnPropertyName="PostBaseRFecSerRate", \
    ColumnDescription="", \
    ColumnWidth="0", \
    ColumnUnits="29", \
    ColumnPrecision="2", \
    ColumnSortType="NONE", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="RealTimeResultColumnDefinition 152")

    RealTimeResultGroupDefinition_10 = stc.create("RealTimeResultGroupDefinition",under = ResultDataSet_1, \
    GroupName="FEC Counters", \
    GroupId="object://customgroup/bdefbcbd-7034-44a1-9d63-b5a6b6736efb/FEC Counters", \
    ColumnClassName="AnalyzerPortResults AnalyzerPortResults AnalyzerPortResults AnalyzerPortResults AnalyzerPortResults AnalyzerPortResults AnalyzerPortResults AnalyzerPortResults AnalyzerPortResults", \
    ColumnPropertyName="CorrectedRsFecErrorCount UncorrectedRsFecErrorCount CorrectedRsFecSymbols CorrectedBaseRFecErrorCount UncorrectedBaseRFecErrorCount PreRsFecSerRate PostRsFecSerRate PreBaseRFecSerRate PostBaseRFecSerRate", \
    CountQuery="", \
    SqlString="SELECT Port.Name AS 'Port Name', AnalyzerPortResults.CorrectedRsFecErrorCount AS 'Corrected RS FEC Errors Count (codewords)', AnalyzerPortResults.UncorrectedRsFecErrorCount AS 'Uncorrected RS FEC Errors Count (codewords)', AnalyzerPortResults.CorrectedRsFecSymbols AS 'Corrected RS FEC Symbols', AnalyzerPortResults.CorrectedBaseRFecErrorCount AS 'Corrected BaseR FEC Errors Count (codewords)', AnalyzerPortResults.UncorrectedBaseRFecErrorCount AS 'Uncorrected BaseR FEC Errors Count (codewords)', AnalyzerPortResults.PreRsFecSerRate AS 'Pre RS FEC Error Rate (cwps)', AnalyzerPortResults.PostRsFecSerRate AS 'Post RS FEC Error Rate (cwps)', AnalyzerPortResults.PreBaseRFecSerRate AS 'Pre Base-R FEC Error Rate (cwps)', AnalyzerPortResults.PostBaseRFecSerRate AS 'Post Base-R FEC Error Rate (cwps)' FROM Port, AnalyzerPortResults, Analyzer WHERE ( Analyzer.ParentHnd = Port.Handle AND AnalyzerPortResults.ParentHnd = Analyzer.Handle AND Port.DataSetId = @DataSetId AND AnalyzerPortResults.DataSetId = @DataSetId AND Analyzer.DataSetId = @DataSetId  ) UNION SELECT ExternalDevicePort.Name AS 'Port Name', AnalyzerPortResults.CorrectedRsFecErrorCount AS 'Corrected RS FEC Errors Count (codewords)', AnalyzerPortResults.UncorrectedRsFecErrorCount AS 'Uncorrected RS FEC Errors Count (codewords)', AnalyzerPortResults.CorrectedRsFecSymbols AS 'Corrected RS FEC Symbols', AnalyzerPortResults.CorrectedBaseRFecErrorCount AS 'Corrected BaseR FEC Errors Count (codewords)', AnalyzerPortResults.UncorrectedBaseRFecErrorCount AS 'Uncorrected BaseR FEC Errors Count (codewords)', AnalyzerPortResults.PreRsFecSerRate AS 'Pre RS FEC Error Rate (cwps)', AnalyzerPortResults.PostRsFecSerRate AS 'Post RS FEC Error Rate (cwps)', AnalyzerPortResults.PreBaseRFecSerRate AS 'Pre Base-R FEC Error Rate (cwps)', AnalyzerPortResults.PostBaseRFecSerRate AS 'Post Base-R FEC Error Rate (cwps)' FROM ExternalDevicePort, AnalyzerPortResults, Port, Analyzer WHERE ( Analyzer.ParentHnd = Port.Handle AND AnalyzerPortResults.ParentHnd = Analyzer.Handle AND ExternalDevicePort.DataSetId = @DataSetId AND AnalyzerPortResults.DataSetId = @DataSetId AND Port.DataSetId = @DataSetId AND Analyzer.DataSetId = @DataSetId  ) ", \
    UseCustomSqlString="FALSE", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="RealTimeResultGroupDefinition 10")

    Perspective_1 = stc.create("Perspective",under = Project_1, \
    PerspectiveViewOwner="SYSTEM", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="Perspective 1")

    PerspectiveNode_1 = stc.create("PerspectiveNode",under = Perspective_1, \
    Guid="8CF0ABC3-9F7C-46bd-A22E-00D88A8376D3", \
    Data="<NodeData Name=\"resultFrame.1\" FrameId=\"8CF0ABC3-9F7C-46bd-A22E-00D88A8376D3\" Active=\"true\" RowCount=\"1\" ColumnCount=\"2\" />", \
    ContentData="""<ContentData><NodeContentData FrameName=\"frame://core/Port/ResultQuery:(1, 0, 0)\" ResultDataSetId=\"Port Traffic\\Basic Traffic Results\" Column=\"0\" Row=\"0\" DockPanelNumber=\"1\" /><NodeContentData FrameName=\"frame://core/DynamicResultView/ResultQuery:(1, 0, 1)\" ResultDataSetId=\"Port Traffic and Counters\\Aggregate Port L1 Tx Rate\" Column=\"1\" Row=\"0\" DockPanelNumber=\"1\" /></ContentData> 
    """, \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="PerspectiveNode 1")

    PerspectiveNode_2 = stc.create("PerspectiveNode",under = Perspective_1, \
    Guid="1F412EE6-760C-4937-9644-ACFA463EA44E", \
    Data="<NodeData Name=\"resultFrame.2\" FrameId=\"1F412EE6-760C-4937-9644-ACFA463EA44E\" Active=\"false\" RowCount=\"1\" ColumnCount=\"2\" />", \
    ContentData="""<ContentData /> 
    """, \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="PerspectiveNode 2")

    DynamicResultView_1 = stc.create("DynamicResultView",under = Project_1, \
    ResultSourceClass="Port", \
    SaveToConfig="TRUE", \
    Identifier="Port Traffic and Counters\\Aggregate Port L1 Tx Rate", \
    Persistent="TRUE", \
    CreatorId="", \
    IsDeprecated="FALSE", \
    Path="Port Traffic", \
    ResultViewOwner="SYSTEM", \
    Description="object://core/DynamicResultView", \
    CustomDisplayName="", \
    CustomDisplayPath="Port Traffic and Counters", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="Aggregate Port L1 Tx Rate")

    PresentationResultQuery_1 = stc.create("PresentationResultQuery",under = DynamicResultView_1, \
    SelectProperties="Port.TxL1BitRate Port.TxMaxLineRate Project.Name", \
    WhereConditions="", \
    GroupByProperties="Project.Name", \
    LimitOffset="0", \
    LimitSize="2000", \
    SortBy="", \
    ArchivingOption="NONE", \
    ResultState="IDLE", \
    ArchivingInterval="10", \
    DatabaseFileName="", \
    DisableAutoGrouping="FALSE", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="PresentationResultQuery 1")

    ColumnDisplayProperties_1 = stc.create("ColumnDisplayProperties",under = DynamicResultView_1, \
    ColumnPropertyId="Port.TxL1BitRate", \
    ColumnCaption="Tx L1 Rate", \
    ColumnWidth="0", \
    ColumnUnits="5", \
    ColumnPrecision="255", \
    ColumnGroups="", \
    ColumnSortIndex="0", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="ColumnDisplayProperties 1")

    ColumnDisplayProperties_2 = stc.create("ColumnDisplayProperties",under = DynamicResultView_1, \
    ColumnPropertyId="Port.TxMaxLineRate", \
    ColumnCaption="Tx Max Line Rate", \
    ColumnWidth="0", \
    ColumnUnits="5", \
    ColumnPrecision="255", \
    ColumnGroups="", \
    ColumnSortIndex="0", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="ColumnDisplayProperties 2")

    ColumnDisplayProperties_3 = stc.create("ColumnDisplayProperties",under = DynamicResultView_1, \
    ColumnPropertyId="Project.Name", \
    ColumnCaption="Project Name", \
    ColumnWidth="0", \
    ColumnUnits="5", \
    ColumnPrecision="255", \
    ColumnGroups="", \
    ColumnSortIndex="0", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="ColumnDisplayProperties 3")

    Host_1 = (stc.get( Port_1, 'children-Host' )).split(' ')[0]
    stc.config(Host_1, \
    DeviceCount="1", \
    EnablePingResponse="FALSE", \
    RouterId="192.0.0.1", \
    RouterIdStep="0.0.0.1", \
    Ipv6RouterId="2000::1", \
    Ipv6RouterIdStep="::1", \
    ReadOnly="FALSE", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="Host")

    EthIIIf_1 = stc.create("EthIIIf",under = Host_1, \
    SourceMac="00:10:94:00:00:02", \
    SrcMacStep="00:00:00:00:00:01", \
    SrcMacList="", \
    SrcMacStepMask="00:00:ff:ff:ff:ff", \
    SrcMacRepeatCount="0", \
    Authenticator="default", \
    UseDefaultPhyMac="FALSE", \
    IfCountPerLowerIf="1", \
    IfRecycleCount="0", \
    IsDecorated="FALSE", \
    IsLoopbackIf="FALSE", \
    IsRange="TRUE", \
    IsDirectlyConnected="TRUE", \
    IsRealism="FALSE", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="EthernetII 1")

    HdlcIf_1 = stc.create("HdlcIf",under = Host_1, \
    ProtocolType="HDLC_PROTOCOL_TYPE_IPV4", \
    IfCountPerLowerIf="1", \
    IfRecycleCount="0", \
    IsDecorated="FALSE", \
    IsLoopbackIf="FALSE", \
    IsRange="TRUE", \
    IsDirectlyConnected="TRUE", \
    IsRealism="FALSE", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="HDLC 1")

    PppIf_1 = stc.create("PppIf",under = Host_1, \
    ProtocolId="PPP_PROTOCOL_ID_IPV4", \
    IfCountPerLowerIf="1", \
    IfRecycleCount="0", \
    IsDecorated="FALSE", \
    IsLoopbackIf="FALSE", \
    IsRange="TRUE", \
    IsDirectlyConnected="TRUE", \
    IsRealism="FALSE", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="PPP 1")

    PppIf_2 = stc.create("PppIf",under = Host_1, \
    ProtocolId="PPP_PROTOCOL_ID_IPV4", \
    IfCountPerLowerIf="1", \
    IfRecycleCount="0", \
    IsDecorated="FALSE", \
    IsLoopbackIf="FALSE", \
    IsRange="TRUE", \
    IsDirectlyConnected="TRUE", \
    IsRealism="FALSE", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="PPP 2")

    Ipv4If_1 = stc.create("Ipv4If",under = Host_1, \
    Address="192.85.1.3", \
    AddrStep="0.0.0.1", \
    AddrStepMask="255.255.255.255", \
    SkipReserved="TRUE", \
    AddrList="", \
    AddrRepeatCount="0", \
    AddrResolver="default", \
    PrefixLength="24", \
    UsePortDefaultIpv4Gateway="FALSE", \
    Gateway="192.85.1.1", \
    GatewayStep="0.0.0.0", \
    GatewayRepeatCount="0", \
    GatewayRecycleCount="0", \
    UseIpAddrRangeSettingsForGateway="FALSE", \
    GatewayList="", \
    ResolveGatewayMac="TRUE", \
    GatewayMac="00:00:01:00:00:01", \
    GatewayMacResolver="default", \
    Ttl="255", \
    TosType="TOS", \
    Tos="192", \
    NeedsAuthentication="FALSE", \
    IfCountPerLowerIf="1", \
    IfRecycleCount="0", \
    IsDecorated="FALSE", \
    IsLoopbackIf="FALSE", \
    IsRange="TRUE", \
    IsDirectlyConnected="TRUE", \
    IsRealism="FALSE", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="IPv4 1")

    Ipv6If_1 = stc.create("Ipv6If",under = Host_1, \
    Address="2000::2", \
    AddrStep="::1", \
    AddrStepMask="ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff", \
    SkipReserved="FALSE", \
    AddrList="", \
    AddrRepeatCount="0", \
    AddrResolver="default", \
    AllocateEui64LinkLocalAddress="FALSE", \
    PrefixLength="64", \
    UsePortDefaultIpv6Gateway="FALSE", \
    EnableGatewayLearning="FALSE", \
    Gateway="::", \
    GatewayStep="::", \
    GatewayRepeatCount="0", \
    UseIpAddrRangeSettingsForGateway="FALSE", \
    GatewayList="", \
    GatewayRecycleCount="0", \
    ResolveGatewayMac="TRUE", \
    GatewayMac="00:00:01:00:00:01", \
    GatewayMacResolver="default", \
    HopLimit="255", \
    TrafficClass="0", \
    FlowLabel="7", \
    NeedsAuthentication="FALSE", \
    IfCountPerLowerIf="1", \
    IfRecycleCount="0", \
    IsDecorated="FALSE", \
    IsLoopbackIf="FALSE", \
    IsRange="TRUE", \
    IsDirectlyConnected="TRUE", \
    IsRealism="FALSE", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="IPv6 1")

    Ipv6If_2 = stc.create("Ipv6If",under = Host_1, \
    Address="2000::2", \
    AddrStep="::1", \
    AddrStepMask="ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff", \
    SkipReserved="FALSE", \
    AddrList="", \
    AddrRepeatCount="0", \
    AddrResolver="default", \
    AllocateEui64LinkLocalAddress="FALSE", \
    PrefixLength="64", \
    UsePortDefaultIpv6Gateway="FALSE", \
    EnableGatewayLearning="FALSE", \
    Gateway="::", \
    GatewayStep="::", \
    GatewayRepeatCount="0", \
    UseIpAddrRangeSettingsForGateway="FALSE", \
    GatewayList="", \
    GatewayRecycleCount="0", \
    ResolveGatewayMac="TRUE", \
    GatewayMac="00:00:01:00:00:01", \
    GatewayMacResolver="default", \
    HopLimit="255", \
    TrafficClass="0", \
    FlowLabel="7", \
    NeedsAuthentication="FALSE", \
    IfCountPerLowerIf="1", \
    IfRecycleCount="0", \
    IsDecorated="FALSE", \
    IsLoopbackIf="FALSE", \
    IsRange="TRUE", \
    IsDirectlyConnected="TRUE", \
    IsRealism="FALSE", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="IPv6 2")

    SystemResourceManager_1 = (stc.get( Port_1, 'children-SystemResourceManager' )).split(' ')[0]
    stc.config(SystemResourceManager_1, \
    MemoryThreshold="80", \
    MemoryThresholdEnable="FALSE", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="Resource Manager 1")

    Generator_1 = (stc.get( Port_1, 'children-Generator' )).split(' ')[0]
    stc.config(Generator_1, \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="Traffic Generator 1")

    GeneratorConfig_1 = (stc.get( Generator_1, 'children-GeneratorConfig' )).split(' ')[0]
    stc.config(GeneratorConfig_1, \
    SchedulingMode="PORT_BASED", \
    AdvancedInterleaving="FALSE", \
    Duration="30", \
    DurationMode="CONTINUOUS", \
    StepSize="1", \
    TimestampLatchMode="START_OF_FRAME", \
    RandomLengthSeed="10900842", \
    JumboFrameThreshold="1518", \
    OversizeFrameThreshold="9018", \
    UndersizeFrameThreshold="64", \
    BurstSize="1", \
    LoadUnit="PERCENT_LINE_RATE", \
    LoadMode="FIXED", \
    FixedLoad="10", \
    RandomMaxLoad="100", \
    RandomMinLoad="10", \
    InterFrameGap="12", \
    InterFrameGapUnit="BYTES", \
    SmoothenRandomLength="FALSE", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="Generator Configuration 1")

    Analyzer_1 = (stc.get( Port_1, 'children-Analyzer' )).split(' ')[0]
    stc.config(Analyzer_1, \
    FilterOnStreamId="TRUE", \
    FilterOnInnerIP="FALSE", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="Traffic Analyzer 1")

    AnalyzerConfig_1 = (stc.get( Analyzer_1, 'children-AnalyzerConfig' )).split(' ')[0]
    stc.config(AnalyzerConfig_1, \
    TimestampLatchMode="START_OF_FRAME", \
    SigMode="ENHANCED_DETECTION", \
    HistogramMode="LATENCY", \
    JumboFrameThreshold="1518", \
    OversizeFrameThreshold="9018", \
    UndersizeFrameThreshold="64", \
    AdvSeqCheckerLateThreshold="1000", \
    VlanAlternateTpid="34984", \
    AlternateSigOffset="0", \
    LatencyMode="PER_STREAM_RX_LATENCY_ON", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="Advanced Analyzer Settings 1")

    InterarrivalTimeHistogram_1 = (stc.get( AnalyzerConfig_1, 'children-InterarrivalTimeHistogram' )).split(' ')[0]
    stc.config(InterarrivalTimeHistogram_1, \
    Description="(ns)", \
    BucketSizeList="2 4 8 16 32 64 128 256 512 1024 2048 4096 8192 16384 32768 65536", \
    LimitList="2 6 14 30 62 126 254 510 1022 2046 4094 8190 16382 32766 65534", \
    DistributionMode="CUSTOM_MODE", \
    ConfigMode="CONFIG_SIZE_MODE", \
    DistributionModeSize="1024", \
    UniformDistributionSize="8", \
    CenterPoint="568", \
    BucketSizeUnit="TEN_NANOSECONDS", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="Histograms 1")

    LatencyHistogram_1 = (stc.get( AnalyzerConfig_1, 'children-LatencyHistogram' )).split(' ')[0]
    stc.config(LatencyHistogram_1, \
    Description="(ns)", \
    BucketSizeList="2 4 8 16 32 64 128 256 512 1024 2048 4096 8192 16384 32768 65536", \
    LimitList="2 6 14 30 62 126 254 510 1022 2046 4094 8190 16382 32766 65534", \
    DistributionMode="CUSTOM_MODE", \
    ConfigMode="CONFIG_SIZE_MODE", \
    DistributionModeSize="1024", \
    UniformDistributionSize="8", \
    CenterPoint="568", \
    BucketSizeUnit="TEN_NANOSECONDS", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="Histograms 1")

    FrameLengthHistogram_1 = (stc.get( AnalyzerConfig_1, 'children-FrameLengthHistogram' )).split(' ')[0]
    stc.config(FrameLengthHistogram_1, \
    Description="(in bytes)", \
    BucketSizeList="2 4 8 16 32 64 128 256 512 1024 2048 4096 8192 16384 32768 65536", \
    LimitList="2 6 14 30 62 126 254 510 1022 2046 4094 8190 16382 32766 65534", \
    DistributionMode="CUSTOM_MODE", \
    ConfigMode="CONFIG_SIZE_MODE", \
    DistributionModeSize="1024", \
    UniformDistributionSize="8", \
    CenterPoint="568", \
    BucketSizeUnit="TEN_NANOSECONDS", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="Histograms 1")

    SeqRunLengthHistogram_1 = (stc.get( AnalyzerConfig_1, 'children-SeqRunLengthHistogram' )).split(' ')[0]
    stc.config(SeqRunLengthHistogram_1, \
    Description="(in frames)", \
    BucketSizeList="2 4 8 16 32 64 128 256 512 1024 2048 4096 8192 16384 32768 65536", \
    LimitList="2 6 14 30 62 126 254 510 1022 2046 4094 8190 16382 32766 65534", \
    DistributionMode="CUSTOM_MODE", \
    ConfigMode="CONFIG_SIZE_MODE", \
    DistributionModeSize="1024", \
    UniformDistributionSize="8", \
    CenterPoint="568", \
    BucketSizeUnit="TEN_NANOSECONDS", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="Histograms 1")

    SeqDiffCheckHistogram_1 = (stc.get( AnalyzerConfig_1, 'children-SeqDiffCheckHistogram' )).split(' ')[0]
    stc.config(SeqDiffCheckHistogram_1, \
    Description="(in deltas)", \
    BucketSizeList="2 4 8 16 32 64 128 256 512 1024 2048 4096 8192 16384 32768 65536", \
    LimitList="2 6 14 30 62 126 254 510 1022 2046 4094 8190 16382 32766 65534", \
    DistributionMode="CUSTOM_MODE", \
    ConfigMode="CONFIG_SIZE_MODE", \
    DistributionModeSize="1024", \
    UniformDistributionSize="8", \
    CenterPoint="568", \
    BucketSizeUnit="TEN_NANOSECONDS", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="Histograms 1")

    JitterHistogram_1 = (stc.get( AnalyzerConfig_1, 'children-JitterHistogram' )).split(' ')[0]
    stc.config(JitterHistogram_1, \
    Description="(ns)", \
    BucketSizeList="2 4 8 16 32 64 128 256 512 1024 2048 4096 8192 16384 32768 65536", \
    LimitList="2 6 14 30 62 126 254 510 1022 2046 4094 8190 16382 32766 65534", \
    DistributionMode="CUSTOM_MODE", \
    ConfigMode="CONFIG_SIZE_MODE", \
    DistributionModeSize="1024", \
    UniformDistributionSize="8", \
    CenterPoint="568", \
    BucketSizeUnit="TEN_NANOSECONDS", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="Histograms 1")

    DiffServConfig_1 = (stc.get( Analyzer_1, 'children-DiffServConfig' )).split(' ')[0]
    stc.config(DiffServConfig_1, \
    QualifyIpv6DstAddr="FALSE", \
    Ipv6DstAddr="ffff::ffff", \
    QualifyIpv4DstAddr="FALSE", \
    Ipv4DstAddr="0.0.0.0", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="QoS Settings 1")

    HighResolutionSamplingPortConfig_1 = (stc.get( Analyzer_1, 'children-HighResolutionSamplingPortConfig' )).split(' ')[0]
    stc.config(HighResolutionSamplingPortConfig_1, \
    BaselineSampleCount="3", \
    EnableTrigger="TRUE", \
    TriggerCondition="LESS_THAN", \
    TriggerValueUnitMode="PERCENT_BASELINE", \
    TriggerStat="TotalFrameRate", \
    TriggerValue="95", \
    TriggerLocation="20", \
    TimingMode="INTERVAL", \
    SamplingInterval="10", \
    SamplingDuration="10", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="High Resolution Port Sampling 1")

    Capture_1 = (stc.get( Port_1, 'children-Capture' )).split(' ')[0]
    stc.config(Capture_1, \
    ElapsedTime="0:00:00", \
    TabIndex="0", \
    Mode="REGULAR_MODE", \
    SrcMode="TX_RX_MODE", \
    RealTimeMode="REALTIME_DISABLE", \
    FlagMode="REGULAR_FLAG_MODE", \
    BufferMode="WRAP", \
    Start="16384", \
    Stop="0", \
    SliceMode="DISABLE", \
    SliceOffsetRef="PREAMBLE", \
    SliceOffset="0", \
    SliceCaptureSize="128", \
    RealTimeFramesBuffer="0", \
    RealTimeBufferStatus="FALSE", \
    CurrentTask="IDLE", \
    CurrentFiltersUsed="0", \
    CurrentFilterBytesUsed="0", \
    AbortSaveTask="FALSE", \
    PostStopTriggerBuffer="255", \
    CaptureFilterMode="FRAMECONTENT", \
    SaveBufferWithPreamble="FALSE", \
    IncreasedMemorySupport="FALSE", \
    Ieee80211FilterString="", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="Capture 1")

    CaptureFilter_1 = (stc.get( Capture_1, 'children-CaptureFilter' )).split(' ')[0]
    stc.config(CaptureFilter_1, \
    QualifyEvents="TRUE", \
    FilterName="", \
    SigPresent="IGNORE", \
    Oversized="IGNORE", \
    Jumbo="IGNORE", \
    Undersized="IGNORE", \
    FcsError="IGNORE", \
    Ipv4CheckSumError="IGNORE", \
    TcpUdpIgmpCheckSumError="IGNORE", \
    SigSeqNumError="IGNORE", \
    Tcp="IGNORE", \
    Udp="IGNORE", \
    Ipv4="IGNORE", \
    Ipv6="IGNORE", \
    Igmp="IGNORE", \
    FrameLenMatch="IGNORE", \
    StreamIdMatch="IGNORE", \
    PrbsError="IGNORE", \
    FilterExpression="{ None }", \
    GuiExpression="", \
    FrameLength="0", \
    StreamId="0", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="Qualify Events 1")

    CaptureFilterStartEvent_1 = (stc.get( Capture_1, 'children-CaptureFilterStartEvent' )).split(' ')[0]
    stc.config(CaptureFilterStartEvent_1, \
    StartEvents="FALSE", \
    FilterName="", \
    SigPresent="IGNORE", \
    Oversized="IGNORE", \
    Jumbo="IGNORE", \
    Undersized="IGNORE", \
    FcsError="IGNORE", \
    Ipv4CheckSumError="IGNORE", \
    TcpUdpIgmpCheckSumError="IGNORE", \
    SigSeqNumError="IGNORE", \
    Tcp="IGNORE", \
    Udp="IGNORE", \
    Ipv4="IGNORE", \
    Ipv6="IGNORE", \
    Igmp="IGNORE", \
    FrameLenMatch="IGNORE", \
    StreamIdMatch="IGNORE", \
    PrbsError="IGNORE", \
    FilterExpression="{ None }", \
    GuiExpression="", \
    FrameLength="0", \
    StreamId="0", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="Start Events 1")

    CaptureFilterStopEvent_1 = (stc.get( Capture_1, 'children-CaptureFilterStopEvent' )).split(' ')[0]
    stc.config(CaptureFilterStopEvent_1, \
    StopEvents="FALSE", \
    FilterName="", \
    SigPresent="IGNORE", \
    Oversized="IGNORE", \
    Jumbo="IGNORE", \
    Undersized="IGNORE", \
    FcsError="IGNORE", \
    Ipv4CheckSumError="IGNORE", \
    TcpUdpIgmpCheckSumError="IGNORE", \
    SigSeqNumError="IGNORE", \
    Tcp="IGNORE", \
    Udp="IGNORE", \
    Ipv4="IGNORE", \
    Ipv6="IGNORE", \
    Igmp="IGNORE", \
    FrameLenMatch="IGNORE", \
    StreamIdMatch="IGNORE", \
    PrbsError="IGNORE", \
    FilterExpression="{ None }", \
    GuiExpression="", \
    FrameLength="0", \
    StreamId="0", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="Stop Events 1")

    CaptureIeee80211_1 = (stc.get( Capture_1, 'children-CaptureIeee80211' )).split(' ')[0]
    stc.config(CaptureIeee80211_1, \
    ChannelWidth="CHANNEL_WIDTH_40M", \
    Channel="36", \
    SecondChannel="149", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="Capture IEEE 802.11 1")

    CaptureRawPacketTagsInfo_1 = (stc.get( Capture_1, 'children-CaptureRawPacketTagsInfo' )).split(' ')[0]
    stc.config(CaptureRawPacketTagsInfo_1, \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="CaptureRawPacketTagsInfo 1")

    ArpCache_1 = (stc.get( Port_1, 'children-ArpCache' )).split(' ')[0]
    stc.config(ArpCache_1, \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="ArpCache 1")

    ArpNdReport_1 = (stc.get( Port_1, 'children-ArpNdReport' )).split(' ')[0]
    stc.config(ArpNdReport_1, \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="ArpNdReport 1")

    PingReport_1 = (stc.get( Port_1, 'children-PingReport' )).split(' ')[0]
    stc.config(PingReport_1, \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="PingReport 1")

    IgmpPortConfig_1 = (stc.get( Port_1, 'children-IgmpPortConfig' )).split(' ')[0]
    stc.config(IgmpPortConfig_1, \
    RatePps="0", \
    MaxBurst="0", \
    CalculateLatencyDelay="10", \
    VlanSubFilter="OUTER", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="IgmpPortConfig 1")

    MldPortConfig_1 = (stc.get( Port_1, 'children-MldPortConfig' )).split(' ')[0]
    stc.config(MldPortConfig_1, \
    RatePps="0", \
    MaxBurst="0", \
    CalculateLatencyDelay="10", \
    VlanSubFilter="OUTER", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="MldPortConfig 1")

    OsePortConfig_1 = (stc.get( Port_1, 'children-OsePortConfig' )).split(' ')[0]
    stc.config(OsePortConfig_1, \
    VirtualSwitch="OVS_2_1", \
    ManufacturerDescription="Spirent Communications", \
    HardwareDescription="Open vSwitch", \
    SerialNumber="None", \
    DatapathDescription="None", \
    ExposeOvsdb="FALSE", \
    OvsdbPortNumber="6640", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="OsePortConfig 1")

    OvsdbPortConfig_1 = (stc.get( Port_1, 'children-OvsdbPortConfig' )).split(' ')[0]
    stc.config(OvsdbPortConfig_1, \
    ConnectionType="TCP", \
    PrivateKey="", \
    Certificate="", \
    CaCertificates="", \
    TlsConnectionOpen="FALSE", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="OVSDB Port Configuration 1")

    OpflexPortConfig_1 = (stc.get( Port_1, 'children-OpflexPortConfig' )).split(' ')[0]
    stc.config(OpflexPortConfig_1, \
    DomainName="Openstack", \
    AgentName="Agent1", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="Opflex Port Configuration 1")

    VxlanPortConfig_1 = (stc.get( Port_1, 'children-VxlanPortConfig' )).split(' ')[0]
    stc.config(VxlanPortConfig_1, \
    UdpDstPort="4789", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="VXLAN Port Configuration 1")

    QbvStreamConfig_1 = (stc.get( Port_1, 'children-QbvStreamConfig' )).split(' ')[0]
    stc.config(QbvStreamConfig_1, \
    ConfigQbvParams="FALSE", \
    GptpBaseTime="0.0", \
    GateCycleTime="1000", \
    StartTimeWithinCycle="0", \
    TickGranularityOfDut="2.5", \
    StreamStartWaitTime="0", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="QbvStreamConfig 1")

    StpPortConfig_1 = (stc.get( Port_1, 'children-StpPortConfig' )).split(' ')[0]
    stc.config(StpPortConfig_1, \
    StpType="STP", \
    PortType="TRUNK", \
    EthernetType="8100", \
    NativeVlan="1", \
    EnablePt2PtLink="FALSE", \
    EnableMacAddrReduction="FALSE", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="StpPortConfig 1")

    Dhcpv4PortConfig_1 = (stc.get( Port_1, 'children-Dhcpv4PortConfig' )).split(' ')[0]
    stc.config(Dhcpv4PortConfig_1, \
    MaxMsgSize="576", \
    LeaseTime="60", \
    MsgTimeout="60", \
    RetryCount="4", \
    RequestRate="100", \
    ReleaseRate="100", \
    StartingXid="0", \
    OutstandingSessionCount="1000", \
    SeqType="SEQUENTIAL", \
    MaxDnav4RetryCount="0", \
    Dnav4Timeout="1000", \
    EnableAssignCustomOptionsForHosts="FALSE", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="Dhcpv4PortConfig 1")

    Dhcpv6PortConfig_1 = (stc.get( Port_1, 'children-Dhcpv6PortConfig' )).split(' ')[0]
    stc.config(Dhcpv6PortConfig_1, \
    RequestRate="100", \
    ReleaseRate="100", \
    RenewRate="100", \
    SessionAutoRetry="FALSE", \
    RetryAttempts="0", \
    NoWaitMultiAdv="FALSE", \
    EnableBlockRate="FALSE", \
    SolicitTimeout="1", \
    MaxSolicitRetryTimeout="120", \
    SolicitRetryCount="10", \
    IndefSolicitRetry="FALSE", \
    DisableSolicitRetry="FALSE", \
    RequestTimeout="1", \
    MaxRequestRetryTimeout="30", \
    RequestRetryCount="10", \
    IndefRequestRetry="FALSE", \
    DisableRequestRetry="FALSE", \
    ConfirmTimeout="1", \
    MaxConfirmTimeout="4", \
    MaxConfirmDuration="10", \
    RenewTimeout="10", \
    MaxRenewRetryTimeout="600", \
    RenewRetryCount="0", \
    IndefRenewRetry="TRUE", \
    DisableRenewRetry="FALSE", \
    RebindTimeout="10", \
    MaxRebindRetryTimeout="600", \
    RebindRetryCount="0", \
    IndefRebindRetry="TRUE", \
    DisableRebindRetry="FALSE", \
    ReleaseTimeout="1", \
    ReleaseRetryCount="5", \
    IndefReleaseRetry="FALSE", \
    DisableReleaseRetry="FALSE", \
    DeclineTimeout="1", \
    DeclineRetryCount="5", \
    IndefDeclineRetry="FALSE", \
    DisableDeclineRetry="FALSE", \
    OutstandingSessionCount="1000", \
    InfoRequestTimeout="1", \
    MaxInfoRequestTimeout="120", \
    InfoRequestRetryCount="0", \
    IndefInfoRequestRetry="TRUE", \
    DisableInfoRequestRetry="FALSE", \
    LeaseTime="86400", \
    SeqType="SEQUENTIAL", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="Dhcpv6PortConfig 1")

    SaaPortConfig_1 = (stc.get( Port_1, 'children-SaaPortConfig' )).split(' ')[0]
    stc.config(SaaPortConfig_1, \
    RequestRate="300", \
    OutstandingSessionCount="1000", \
    SeqType="PARALLEL", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="SaaPortConfig 1")

    RoEPortConfig_1 = (stc.get( Port_1, 'children-RoEPortConfig' )).split(' ')[0]
    stc.config(RoEPortConfig_1, \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="RoEPortConfig 1")

    L2tpPortConfig_1 = (stc.get( Port_1, 'children-L2tpPortConfig' )).split(' ')[0]
    stc.config(L2tpPortConfig_1, \
    L2tpVersion="L2TPV2", \
    L2tpNodeType="LAC", \
    TunnelConnectRate="100", \
    SeqType="SEQUENTIAL", \
    ConnectRateV3="100", \
    DisconnectRateV3="1000", \
    SessionOutstandingV3="100", \
    CsurqRate="100", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="L2tpPortConfig 1")

    PppoxPortConfig_1 = (stc.get( Port_1, 'children-PppoxPortConfig' )).split(' ')[0]
    stc.config(PppoxPortConfig_1, \
    EmulationType="CLIENT", \
    EnableBlockRate="FALSE", \
    ConnectRate="100", \
    DisconnectRate="1000", \
    SessionOutstanding="100", \
    SeqType="SEQUENTIAL", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="PppoxPortConfig 1")

    PppProtocolConfig_1 = (stc.get( Port_1, 'children-PppProtocolConfig' )).split(' ')[0]
    stc.config(PppProtocolConfig_1, \
    PapRequestTimeout="3", \
    MaxPapRequestAttempts="10", \
    ChapChalRequestTimeout="3", \
    ChapAckTimeout="3", \
    MaxChapRequestReplyAttempts="10", \
    AutoRetryCount="65535", \
    EnableAutoRetry="FALSE", \
    EnableSessionAutoRetry="FALSE", \
    Ipv4PeerAddr="0.0.0.0", \
    Ipv6PeerAddr="::", \
    IpcpEncap="IPV4", \
    Protocol="PPPOPOS", \
    EnableMruNegotiation="TRUE", \
    EnableMagicNum="TRUE", \
    EnableNcpTermination="FALSE", \
    Authentication="NONE", \
    IncludeTxChapId="TRUE", \
    EnableOsi="FALSE", \
    EnableMpls="FALSE", \
    MruSize="1492", \
    EnableEchoRequest="FALSE", \
    EchoRequestGenFreq="10", \
    MaxEchoRequestAttempts="1", \
    LcpConfigRequestTimeout="3", \
    LcpConfigRequestMaxAttempts="10", \
    LcpTermRequestTimeout="3", \
    LcpTermRequestMaxAttempts="10", \
    NcpConfigRequestTimeout="3", \
    NcpConfigRequestMaxAttempts="10", \
    MaxNaks="5", \
    Username="spirent", \
    Password="spirent", \
    UseAuthenticationList="FALSE", \
    AuthenticationFilePath="", \
    EnablePrimaryDns="TRUE", \
    PrimaryDns="null", \
    EnableSecondaryDns="TRUE", \
    SecondaryDns="null", \
    RAMOFlag="NODHCP", \
    ConnectRate="100", \
    DisconnectRate="100", \
    UsePartialBlockState="FALSE", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="PPP 1")

    AncpPortConfig_1 = (stc.get( Port_1, 'children-AncpPortConfig' )).split(' ')[0]
    stc.config(AncpPortConfig_1, \
    EstablishRate="100", \
    TerminateRate="100", \
    SeqType="SEQUENTIAL", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="AncpPortConfig 1")

    EoamPortConfig_1 = (stc.get( Port_1, 'children-EoamPortConfig' )).split(' ')[0]
    stc.config(EoamPortConfig_1, \
    EtherType="8902", \
    MulticastMacType1="01:80:c2:00:00:30", \
    MulticastMacType2="01:80:c2:00:00:38", \
    EncodeMeLevel="TRUE", \
    DisableContChkRx="FALSE", \
    LinkTraceResponseRelayAction="DEFAULT", \
    ImmediateLinkTraceResponse="FALSE", \
    ImmediateLoopbackResponse="FALSE", \
    EchoTlvsInDelayMeasurementResponse="TRUE", \
    EchoTlvsInLossMeasurementResponse="TRUE", \
    EchoTlvsInSlr="TRUE", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="EoamPortConfig 1")

    AppPerfPortConfig_1 = (stc.get( Port_1, 'children-AppPerfPortConfig' )).split(' ')[0]
    stc.config(AppPerfPortConfig_1, \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="AppPerfPortConfig 1")

    VqAnalyzer_1 = (stc.get( Port_1, 'children-VqAnalyzer' )).split(' ')[0]
    stc.config(VqAnalyzer_1, \
    FrameLossConcealmentRobustness="4", \
    SlicesPerIframe="0", \
    NominalDelay="3", \
    MaxPktCount="65535", \
    MosVThreshold="1", \
    MosVNormalizedThreshold="1", \
    MosAvThreshold="1", \
    MosAThreshold="1", \
    PidInterval="1", \
    PatRepetition="0.5", \
    PmtRepetition="0.5", \
    PcrContinuity="0.1", \
    PcrRepetition="0.04", \
    PtsRepetition="0.7", \
    RtpTimestampThreshold="3", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="VqAnalyzer 1")

    EthernetCopper_1 = stc.create("EthernetCopper",under = Port_1, \
    AutoMdix="FALSE", \
    TestMode="NORMAL_OPERATION", \
    PerformanceMode="STC_DEFAULT", \
    LineSpeed="SPEED_1G", \
    AlternateSpeeds="", \
    AdvertiseIEEE="TRUE", \
    AdvertiseNBASET="TRUE", \
    Enable8023brPerPort="FALSE", \
    AutoNegotiation="TRUE", \
    AutoNegotiationMasterSlave="MASTER", \
    AutoNegotiationMasterSlaveEnable="TRUE", \
    DownshiftEnable="FALSE", \
    FlowControl="FALSE", \
    OptimizedXon="DISABLE", \
    PfcCableDelayType="FIBER", \
    PfcCableDelay="0", \
    Duplex="FULL", \
    CollisionExponent="10", \
    InternalPpmAdjust="0", \
    TransmitClockSource="INTERNAL", \
    ManagementRegistersTemplate="Templates/Mii/default_mii.xml", \
    IgnoreLinkStatus="FALSE", \
    DataPathMode="NORMAL", \
    Mtu="1500", \
    EnforceMtuOnRx="FALSE", \
    PortSetupMode="PORTCONFIG_ONLY", \
    ForwardErrorCorrection="TRUE", \
    CustomFecChange="0", \
    CustomFecMode="KR_FEC", \
    IgnoreFirmwareDefault="FALSE", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="Ethernet Copper Phy 1")

    Mii_1 = (stc.get( EthernetCopper_1, 'children-Mii' )).split(' ')[0]
    stc.config(Mii_1, \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="Mii 1")

    MiiRegister_1 = (stc.get( Mii_1, 'children-MiiRegister' )).split(' ')[0]
    stc.config(MiiRegister_1, \
    Address="0", \
    RegValue="4416", \
    WritableMask="65535", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="Control")

    MiiRegister_2 = (stc.get( Mii_1, 'children-MiiRegister' )).split(' ')[1]
    stc.config(MiiRegister_2, \
    Address="1", \
    RegValue="31085", \
    WritableMask="0", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="Status")

    MiiRegister_3 = (stc.get( Mii_1, 'children-MiiRegister' )).split(' ')[2]
    stc.config(MiiRegister_3, \
    Address="2", \
    RegValue="32", \
    WritableMask="0", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="PHY Identifier")

    MiiRegister_4 = (stc.get( Mii_1, 'children-MiiRegister' )).split(' ')[3]
    stc.config(MiiRegister_4, \
    Address="3", \
    RegValue="24753", \
    WritableMask="0", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="PHY Identifier")

    MiiRegister_5 = (stc.get( Mii_1, 'children-MiiRegister' )).split(' ')[4]
    stc.config(MiiRegister_5, \
    Address="4", \
    RegValue="481", \
    WritableMask="65535", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="Auto-Negotiation Advertisement")

    MiiRegister_6 = (stc.get( Mii_1, 'children-MiiRegister' )).split(' ')[5]
    stc.config(MiiRegister_6, \
    Address="5", \
    RegValue="19937", \
    WritableMask="0", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="Auto-Negotiation Link Partner Base Page Ability")

    MiiRegister_7 = (stc.get( Mii_1, 'children-MiiRegister' )).split(' ')[6]
    stc.config(MiiRegister_7, \
    Address="6", \
    RegValue="5", \
    WritableMask="0", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="Auto-Negotiation Expansion")

    MiiRegister_8 = (stc.get( Mii_1, 'children-MiiRegister' )).split(' ')[7]
    stc.config(MiiRegister_8, \
    Address="7", \
    RegValue="8193", \
    WritableMask="47103", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="Auto-Negotiation Next Page Transmit")

    MiiRegister_9 = (stc.get( Mii_1, 'children-MiiRegister' )).split(' ')[8]
    stc.config(MiiRegister_9, \
    Address="8", \
    RegValue="0", \
    WritableMask="0", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="Auto-Negotiation Link Partner Received Next Page")

    MiiRegister_10 = (stc.get( Mii_1, 'children-MiiRegister' )).split(' ')[9]
    stc.config(MiiRegister_10, \
    Address="9", \
    RegValue="512", \
    WritableMask="65535", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="MASTER-SLAVE Control Register")

    MiiRegister_11 = (stc.get( Mii_1, 'children-MiiRegister' )).split(' ')[10]
    stc.config(MiiRegister_11, \
    Address="10", \
    RegValue="0", \
    WritableMask="0", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="MASTER-SLAVE Status Register")

    MiiRegister_12 = (stc.get( Mii_1, 'children-MiiRegister' )).split(' ')[11]
    stc.config(MiiRegister_12, \
    Address="11", \
    RegValue="0", \
    WritableMask="0", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="Reserved")

    MiiRegister_13 = (stc.get( Mii_1, 'children-MiiRegister' )).split(' ')[12]
    stc.config(MiiRegister_13, \
    Address="12", \
    RegValue="0", \
    WritableMask="0", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="Reserved")

    MiiRegister_14 = (stc.get( Mii_1, 'children-MiiRegister' )).split(' ')[13]
    stc.config(MiiRegister_14, \
    Address="13", \
    RegValue="0", \
    WritableMask="0", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="Reserved")

    MiiRegister_15 = (stc.get( Mii_1, 'children-MiiRegister' )).split(' ')[14]
    stc.config(MiiRegister_15, \
    Address="14", \
    RegValue="0", \
    WritableMask="0", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="Reserved")

    MiiRegister_16 = (stc.get( Mii_1, 'children-MiiRegister' )).split(' ')[15]
    stc.config(MiiRegister_16, \
    Address="15", \
    RegValue="12288", \
    WritableMask="0", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="Extended Status")

    MiiRegister_17 = (stc.get( Mii_1, 'children-MiiRegister' )).split(' ')[16]
    stc.config(MiiRegister_17, \
    Address="16", \
    RegValue="16385", \
    WritableMask="65535", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="Vendor Specific")

    MiiRegister_18 = (stc.get( Mii_1, 'children-MiiRegister' )).split(' ')[17]
    stc.config(MiiRegister_18, \
    Address="17", \
    RegValue="768", \
    WritableMask="0", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="Vendor Specific")

    MiiRegister_19 = (stc.get( Mii_1, 'children-MiiRegister' )).split(' ')[18]
    stc.config(MiiRegister_19, \
    Address="18", \
    RegValue="0", \
    WritableMask="65535", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="Vendor Specific")

    MiiRegister_20 = (stc.get( Mii_1, 'children-MiiRegister' )).split(' ')[19]
    stc.config(MiiRegister_20, \
    Address="19", \
    RegValue="0", \
    WritableMask="65535", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="Vendor Specific")

    MiiRegister_21 = (stc.get( Mii_1, 'children-MiiRegister' )).split(' ')[20]
    stc.config(MiiRegister_21, \
    Address="20", \
    RegValue="0", \
    WritableMask="65535", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="Vendor Specific")

    MiiRegister_22 = (stc.get( Mii_1, 'children-MiiRegister' )).split(' ')[21]
    stc.config(MiiRegister_22, \
    Address="21", \
    RegValue="0", \
    WritableMask="0", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="Vendor Specific")

    MiiRegister_23 = (stc.get( Mii_1, 'children-MiiRegister' )).split(' ')[22]
    stc.config(MiiRegister_23, \
    Address="22", \
    RegValue="0", \
    WritableMask="0", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="Vendor Specific")

    MiiRegister_24 = (stc.get( Mii_1, 'children-MiiRegister' )).split(' ')[23]
    stc.config(MiiRegister_24, \
    Address="23", \
    RegValue="0", \
    WritableMask="65535", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="Vendor Specific")

    MiiRegister_25 = (stc.get( Mii_1, 'children-MiiRegister' )).split(' ')[24]
    stc.config(MiiRegister_25, \
    Address="24", \
    RegValue="25600", \
    WritableMask="65535", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="Vendor Specific")

    MiiRegister_26 = (stc.get( Mii_1, 'children-MiiRegister' )).split(' ')[25]
    stc.config(MiiRegister_26, \
    Address="25", \
    RegValue="0", \
    WritableMask="0", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="Vendor Specific")

    MiiRegister_27 = (stc.get( Mii_1, 'children-MiiRegister' )).split(' ')[26]
    stc.config(MiiRegister_27, \
    Address="26", \
    RegValue="0", \
    WritableMask="65535", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="Vendor Specific")

    MiiRegister_28 = (stc.get( Mii_1, 'children-MiiRegister' )).split(' ')[27]
    stc.config(MiiRegister_28, \
    Address="27", \
    RegValue="65535", \
    WritableMask="65535", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="Vendor Specific")

    MiiRegister_29 = (stc.get( Mii_1, 'children-MiiRegister' )).split(' ')[28]
    stc.config(MiiRegister_29, \
    Address="28", \
    RegValue="0", \
    WritableMask="0", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="Vendor Specific")

    MiiRegister_30 = (stc.get( Mii_1, 'children-MiiRegister' )).split(' ')[29]
    stc.config(MiiRegister_30, \
    Address="29", \
    RegValue="0", \
    WritableMask="0", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="Vendor Specific")

    MiiRegister_31 = (stc.get( Mii_1, 'children-MiiRegister' )).split(' ')[30]
    stc.config(MiiRegister_31, \
    Address="30", \
    RegValue="0", \
    WritableMask="0", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="Vendor Specific")

    MiiRegister_32 = (stc.get( Mii_1, 'children-MiiRegister' )).split(' ')[31]
    stc.config(MiiRegister_32, \
    Address="31", \
    RegValue="0", \
    WritableMask="0", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="Vendor Specific")

    EthernetCopper_2 = stc.create("EthernetCopper",under = Port_1, \
    AutoMdix="FALSE", \
    TestMode="NORMAL_OPERATION", \
    PerformanceMode="STC_DEFAULT", \
    LineSpeed="SPEED_1G", \
    AlternateSpeeds="", \
    AdvertiseIEEE="TRUE", \
    AdvertiseNBASET="TRUE", \
    Enable8023brPerPort="FALSE", \
    AutoNegotiation="TRUE", \
    AutoNegotiationMasterSlave="MASTER", \
    AutoNegotiationMasterSlaveEnable="TRUE", \
    DownshiftEnable="FALSE", \
    FlowControl="FALSE", \
    OptimizedXon="DISABLE", \
    PfcCableDelayType="FIBER", \
    PfcCableDelay="0", \
    Duplex="FULL", \
    CollisionExponent="10", \
    InternalPpmAdjust="0", \
    TransmitClockSource="INTERNAL", \
    ManagementRegistersTemplate="Templates/Mii/default_mii.xml", \
    IgnoreLinkStatus="FALSE", \
    DataPathMode="NORMAL", \
    Mtu="1500", \
    EnforceMtuOnRx="FALSE", \
    PortSetupMode="PORTCONFIG_ONLY", \
    ForwardErrorCorrection="TRUE", \
    CustomFecChange="0", \
    CustomFecMode="KR_FEC", \
    IgnoreFirmwareDefault="FALSE", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="Ethernet Copper Phy 3")

    Mii_2 = (stc.get( EthernetCopper_2, 'children-Mii' )).split(' ')[0]
    stc.config(Mii_2, \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="Mii 1")

    MiiRegister_33 = (stc.get( Mii_2, 'children-MiiRegister' )).split(' ')[0]
    stc.config(MiiRegister_33, \
    Address="0", \
    RegValue="4416", \
    WritableMask="65535", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="Control")

    MiiRegister_34 = (stc.get( Mii_2, 'children-MiiRegister' )).split(' ')[1]
    stc.config(MiiRegister_34, \
    Address="1", \
    RegValue="31085", \
    WritableMask="0", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="Status")

    MiiRegister_35 = (stc.get( Mii_2, 'children-MiiRegister' )).split(' ')[2]
    stc.config(MiiRegister_35, \
    Address="2", \
    RegValue="32", \
    WritableMask="0", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="PHY Identifier")

    MiiRegister_36 = (stc.get( Mii_2, 'children-MiiRegister' )).split(' ')[3]
    stc.config(MiiRegister_36, \
    Address="3", \
    RegValue="24753", \
    WritableMask="0", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="PHY Identifier")

    MiiRegister_37 = (stc.get( Mii_2, 'children-MiiRegister' )).split(' ')[4]
    stc.config(MiiRegister_37, \
    Address="4", \
    RegValue="481", \
    WritableMask="65535", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="Auto-Negotiation Advertisement")

    MiiRegister_38 = (stc.get( Mii_2, 'children-MiiRegister' )).split(' ')[5]
    stc.config(MiiRegister_38, \
    Address="5", \
    RegValue="19937", \
    WritableMask="0", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="Auto-Negotiation Link Partner Base Page Ability")

    MiiRegister_39 = (stc.get( Mii_2, 'children-MiiRegister' )).split(' ')[6]
    stc.config(MiiRegister_39, \
    Address="6", \
    RegValue="5", \
    WritableMask="0", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="Auto-Negotiation Expansion")

    MiiRegister_40 = (stc.get( Mii_2, 'children-MiiRegister' )).split(' ')[7]
    stc.config(MiiRegister_40, \
    Address="7", \
    RegValue="8193", \
    WritableMask="47103", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="Auto-Negotiation Next Page Transmit")

    MiiRegister_41 = (stc.get( Mii_2, 'children-MiiRegister' )).split(' ')[8]
    stc.config(MiiRegister_41, \
    Address="8", \
    RegValue="0", \
    WritableMask="0", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="Auto-Negotiation Link Partner Received Next Page")

    MiiRegister_42 = (stc.get( Mii_2, 'children-MiiRegister' )).split(' ')[9]
    stc.config(MiiRegister_42, \
    Address="9", \
    RegValue="512", \
    WritableMask="65535", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="MASTER-SLAVE Control Register")

    MiiRegister_43 = (stc.get( Mii_2, 'children-MiiRegister' )).split(' ')[10]
    stc.config(MiiRegister_43, \
    Address="10", \
    RegValue="0", \
    WritableMask="0", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="MASTER-SLAVE Status Register")

    MiiRegister_44 = (stc.get( Mii_2, 'children-MiiRegister' )).split(' ')[11]
    stc.config(MiiRegister_44, \
    Address="11", \
    RegValue="0", \
    WritableMask="0", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="Reserved")

    MiiRegister_45 = (stc.get( Mii_2, 'children-MiiRegister' )).split(' ')[12]
    stc.config(MiiRegister_45, \
    Address="12", \
    RegValue="0", \
    WritableMask="0", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="Reserved")

    MiiRegister_46 = (stc.get( Mii_2, 'children-MiiRegister' )).split(' ')[13]
    stc.config(MiiRegister_46, \
    Address="13", \
    RegValue="0", \
    WritableMask="0", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="Reserved")

    MiiRegister_47 = (stc.get( Mii_2, 'children-MiiRegister' )).split(' ')[14]
    stc.config(MiiRegister_47, \
    Address="14", \
    RegValue="0", \
    WritableMask="0", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="Reserved")

    MiiRegister_48 = (stc.get( Mii_2, 'children-MiiRegister' )).split(' ')[15]
    stc.config(MiiRegister_48, \
    Address="15", \
    RegValue="12288", \
    WritableMask="0", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="Extended Status")

    MiiRegister_49 = (stc.get( Mii_2, 'children-MiiRegister' )).split(' ')[16]
    stc.config(MiiRegister_49, \
    Address="16", \
    RegValue="16385", \
    WritableMask="65535", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="Vendor Specific")

    MiiRegister_50 = (stc.get( Mii_2, 'children-MiiRegister' )).split(' ')[17]
    stc.config(MiiRegister_50, \
    Address="17", \
    RegValue="768", \
    WritableMask="0", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="Vendor Specific")

    MiiRegister_51 = (stc.get( Mii_2, 'children-MiiRegister' )).split(' ')[18]
    stc.config(MiiRegister_51, \
    Address="18", \
    RegValue="0", \
    WritableMask="65535", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="Vendor Specific")

    MiiRegister_52 = (stc.get( Mii_2, 'children-MiiRegister' )).split(' ')[19]
    stc.config(MiiRegister_52, \
    Address="19", \
    RegValue="0", \
    WritableMask="65535", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="Vendor Specific")

    MiiRegister_53 = (stc.get( Mii_2, 'children-MiiRegister' )).split(' ')[20]
    stc.config(MiiRegister_53, \
    Address="20", \
    RegValue="0", \
    WritableMask="65535", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="Vendor Specific")

    MiiRegister_54 = (stc.get( Mii_2, 'children-MiiRegister' )).split(' ')[21]
    stc.config(MiiRegister_54, \
    Address="21", \
    RegValue="0", \
    WritableMask="0", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="Vendor Specific")

    MiiRegister_55 = (stc.get( Mii_2, 'children-MiiRegister' )).split(' ')[22]
    stc.config(MiiRegister_55, \
    Address="22", \
    RegValue="0", \
    WritableMask="0", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="Vendor Specific")

    MiiRegister_56 = (stc.get( Mii_2, 'children-MiiRegister' )).split(' ')[23]
    stc.config(MiiRegister_56, \
    Address="23", \
    RegValue="0", \
    WritableMask="65535", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="Vendor Specific")

    MiiRegister_57 = (stc.get( Mii_2, 'children-MiiRegister' )).split(' ')[24]
    stc.config(MiiRegister_57, \
    Address="24", \
    RegValue="25600", \
    WritableMask="65535", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="Vendor Specific")

    MiiRegister_58 = (stc.get( Mii_2, 'children-MiiRegister' )).split(' ')[25]
    stc.config(MiiRegister_58, \
    Address="25", \
    RegValue="0", \
    WritableMask="0", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="Vendor Specific")

    MiiRegister_59 = (stc.get( Mii_2, 'children-MiiRegister' )).split(' ')[26]
    stc.config(MiiRegister_59, \
    Address="26", \
    RegValue="0", \
    WritableMask="65535", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="Vendor Specific")

    MiiRegister_60 = (stc.get( Mii_2, 'children-MiiRegister' )).split(' ')[27]
    stc.config(MiiRegister_60, \
    Address="27", \
    RegValue="65535", \
    WritableMask="65535", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="Vendor Specific")

    MiiRegister_61 = (stc.get( Mii_2, 'children-MiiRegister' )).split(' ')[28]
    stc.config(MiiRegister_61, \
    Address="28", \
    RegValue="0", \
    WritableMask="0", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="Vendor Specific")

    MiiRegister_62 = (stc.get( Mii_2, 'children-MiiRegister' )).split(' ')[29]
    stc.config(MiiRegister_62, \
    Address="29", \
    RegValue="0", \
    WritableMask="0", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="Vendor Specific")

    MiiRegister_63 = (stc.get( Mii_2, 'children-MiiRegister' )).split(' ')[30]
    stc.config(MiiRegister_63, \
    Address="30", \
    RegValue="0", \
    WritableMask="0", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="Vendor Specific")

    MiiRegister_64 = (stc.get( Mii_2, 'children-MiiRegister' )).split(' ')[31]
    stc.config(MiiRegister_64, \
    Address="31", \
    RegValue="0", \
    WritableMask="0", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="Vendor Specific")

    StreamBlock_1 = stc.create("StreamBlock",under = Port_1, \
    IsControlledByGenerator="TRUE", \
    ControlledBy="generator", \
    TrafficPattern="PAIR", \
    EndpointMapping="ONE_TO_ONE", \
    EnableStreamOnlyGeneration="TRUE", \
    EnableBidirectionalTraffic="FALSE", \
    EqualRxPortDistribution="FALSE", \
    EnableTxPortSendingTrafficToSelf="FALSE", \
    EnableControlPlane="FALSE", \
    InsertSig="TRUE", \
    FrameLengthMode="FIXED", \
    FixedFrameLength="128", \
    MinFrameLength="128", \
    MaxFrameLength="256", \
    StepFrameLength="1", \
    FillType="CONSTANT", \
    ConstantFillPattern="0", \
    EnableFcsErrorInsertion="FALSE", \
    Filter="Device,MPLS-TP,Bfd,Rip,Lldp,Ieee1588v2,Ieee8021as,Bgp,Isis,Ldp,Stp,Ospfv3,Lacp,Pim,Rsvp,Ospfv2,FCoE,FCPlugin,FCoEVFPort,FCFPort,TwampClient,TwampServer,LspPing,Lisp,Srp,Trill Protocol,Otv,Openflow Protocol,Ancp,PppProtocol,PppoeProtocol,Vxlan,OSE,802.1x,OVSDB Protocol,Vepa,Opflex Protocol,Responder,IEEE 802.11 Protocol,Avbgen,RadarEmulation,TtwbProxy,ECPRI Protocol,Packet Channel,SyncE,Dhcpv4,IgmpMld,Dhcpv6,AppPerf,Cifs,Dpg,CSMP,Iperf,XMPPvJ,Ntp,Ftp,Http,RawTcp,Sip,Video,IPv4", \
    ShowAllHeaders="FALSE", \
    AllowInvalidHeaders="FALSE", \
    AutoSelectTunnel="FALSE", \
    ByPassSimpleIpSubnetChecking="FALSE", \
    EnableHighSpeedResultAnalysis="TRUE", \
    EnableBackBoneTrafficSendToSelf="TRUE", \
    EnableResolveDestMacAddress="TRUE", \
    AdvancedInterleavingGroup="0", \
    DisableTunnelBinding="FALSE", \
    Enable8023brMFrame="FALSE", \
    EnableCustomPfc="FALSE", \
    CustomPfcPriority="0", \
    TimeStampType="MIN", \
    TimeStampOffset="0", \
    FrameConfig="<frame><config><pdus><pdu name=\"ipv4_8200\" pdu=\"ipv4:IPv4\"><totalLength>20</totalLength><ttl>255</ttl><checksum>32267</checksum><sourceAddr>10.10.10.2</sourceAddr><destAddr>20.20.20.2</destAddr><prefixLength>24</prefixLength><destPrefixLength>24</destPrefixLength><gateway>10.10.10.1</gateway><tosDiffserv name=\"anon_8295\"><tos name=\"anon_8296\"><precedence>6</precedence><dBit>0</dBit><tBit>0</tBit><rBit>0</rBit><mBit>0</mBit><reserved>0</reserved></tos></tosDiffserv></pdu></pdus></config></frame>", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="StreamBlock 12-3")

    Host_2 = (stc.get( Port_2, 'children-Host' )).split(' ')[0]
    stc.config(Host_2, \
    DeviceCount="1", \
    EnablePingResponse="FALSE", \
    RouterId="192.0.0.1", \
    RouterIdStep="0.0.0.1", \
    Ipv6RouterId="2000::1", \
    Ipv6RouterIdStep="::1", \
    ReadOnly="FALSE", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="Host")

    EthIIIf_2 = stc.create("EthIIIf",under = Host_2, \
    SourceMac="00:10:94:00:00:02", \
    SrcMacStep="00:00:00:00:00:01", \
    SrcMacList="", \
    SrcMacStepMask="00:00:ff:ff:ff:ff", \
    SrcMacRepeatCount="0", \
    Authenticator="default", \
    UseDefaultPhyMac="FALSE", \
    IfCountPerLowerIf="1", \
    IfRecycleCount="0", \
    IsDecorated="FALSE", \
    IsLoopbackIf="FALSE", \
    IsRange="TRUE", \
    IsDirectlyConnected="TRUE", \
    IsRealism="FALSE", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="EthernetII 2")

    HdlcIf_2 = stc.create("HdlcIf",under = Host_2, \
    ProtocolType="HDLC_PROTOCOL_TYPE_IPV4", \
    IfCountPerLowerIf="1", \
    IfRecycleCount="0", \
    IsDecorated="FALSE", \
    IsLoopbackIf="FALSE", \
    IsRange="TRUE", \
    IsDirectlyConnected="TRUE", \
    IsRealism="FALSE", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="HDLC 2")

    PppIf_3 = stc.create("PppIf",under = Host_2, \
    ProtocolId="PPP_PROTOCOL_ID_IPV4", \
    IfCountPerLowerIf="1", \
    IfRecycleCount="0", \
    IsDecorated="FALSE", \
    IsLoopbackIf="FALSE", \
    IsRange="TRUE", \
    IsDirectlyConnected="TRUE", \
    IsRealism="FALSE", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="PPP 3")

    PppIf_4 = stc.create("PppIf",under = Host_2, \
    ProtocolId="PPP_PROTOCOL_ID_IPV4", \
    IfCountPerLowerIf="1", \
    IfRecycleCount="0", \
    IsDecorated="FALSE", \
    IsLoopbackIf="FALSE", \
    IsRange="TRUE", \
    IsDirectlyConnected="TRUE", \
    IsRealism="FALSE", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="PPP 4")

    Ipv4If_2 = stc.create("Ipv4If",under = Host_2, \
    Address="192.85.1.3", \
    AddrStep="0.0.0.1", \
    AddrStepMask="255.255.255.255", \
    SkipReserved="TRUE", \
    AddrList="", \
    AddrRepeatCount="0", \
    AddrResolver="default", \
    PrefixLength="24", \
    UsePortDefaultIpv4Gateway="FALSE", \
    Gateway="192.85.1.1", \
    GatewayStep="0.0.0.0", \
    GatewayRepeatCount="0", \
    GatewayRecycleCount="0", \
    UseIpAddrRangeSettingsForGateway="FALSE", \
    GatewayList="", \
    ResolveGatewayMac="TRUE", \
    GatewayMac="00:00:01:00:00:01", \
    GatewayMacResolver="default", \
    Ttl="255", \
    TosType="TOS", \
    Tos="192", \
    NeedsAuthentication="FALSE", \
    IfCountPerLowerIf="1", \
    IfRecycleCount="0", \
    IsDecorated="FALSE", \
    IsLoopbackIf="FALSE", \
    IsRange="TRUE", \
    IsDirectlyConnected="TRUE", \
    IsRealism="FALSE", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="IPv4 2")

    Ipv6If_3 = stc.create("Ipv6If",under = Host_2, \
    Address="2000::2", \
    AddrStep="::1", \
    AddrStepMask="ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff", \
    SkipReserved="FALSE", \
    AddrList="", \
    AddrRepeatCount="0", \
    AddrResolver="default", \
    AllocateEui64LinkLocalAddress="FALSE", \
    PrefixLength="64", \
    UsePortDefaultIpv6Gateway="FALSE", \
    EnableGatewayLearning="FALSE", \
    Gateway="::", \
    GatewayStep="::", \
    GatewayRepeatCount="0", \
    UseIpAddrRangeSettingsForGateway="FALSE", \
    GatewayList="", \
    GatewayRecycleCount="0", \
    ResolveGatewayMac="TRUE", \
    GatewayMac="00:00:01:00:00:01", \
    GatewayMacResolver="default", \
    HopLimit="255", \
    TrafficClass="0", \
    FlowLabel="7", \
    NeedsAuthentication="FALSE", \
    IfCountPerLowerIf="1", \
    IfRecycleCount="0", \
    IsDecorated="FALSE", \
    IsLoopbackIf="FALSE", \
    IsRange="TRUE", \
    IsDirectlyConnected="TRUE", \
    IsRealism="FALSE", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="IPv6 3")

    Ipv6If_4 = stc.create("Ipv6If",under = Host_2, \
    Address="2000::2", \
    AddrStep="::1", \
    AddrStepMask="ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff", \
    SkipReserved="FALSE", \
    AddrList="", \
    AddrRepeatCount="0", \
    AddrResolver="default", \
    AllocateEui64LinkLocalAddress="FALSE", \
    PrefixLength="64", \
    UsePortDefaultIpv6Gateway="FALSE", \
    EnableGatewayLearning="FALSE", \
    Gateway="::", \
    GatewayStep="::", \
    GatewayRepeatCount="0", \
    UseIpAddrRangeSettingsForGateway="FALSE", \
    GatewayList="", \
    GatewayRecycleCount="0", \
    ResolveGatewayMac="TRUE", \
    GatewayMac="00:00:01:00:00:01", \
    GatewayMacResolver="default", \
    HopLimit="255", \
    TrafficClass="0", \
    FlowLabel="7", \
    NeedsAuthentication="FALSE", \
    IfCountPerLowerIf="1", \
    IfRecycleCount="0", \
    IsDecorated="FALSE", \
    IsLoopbackIf="FALSE", \
    IsRange="TRUE", \
    IsDirectlyConnected="TRUE", \
    IsRealism="FALSE", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="IPv6 4")

    SystemResourceManager_2 = (stc.get( Port_2, 'children-SystemResourceManager' )).split(' ')[0]
    stc.config(SystemResourceManager_2, \
    MemoryThreshold="80", \
    MemoryThresholdEnable="FALSE", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="Resource Manager 2")

    Generator_2 = (stc.get( Port_2, 'children-Generator' )).split(' ')[0]
    stc.config(Generator_2, \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="Traffic Generator 2")

    GeneratorConfig_2 = (stc.get( Generator_2, 'children-GeneratorConfig' )).split(' ')[0]
    stc.config(GeneratorConfig_2, \
    SchedulingMode="PORT_BASED", \
    AdvancedInterleaving="FALSE", \
    Duration="30", \
    DurationMode="CONTINUOUS", \
    StepSize="1", \
    TimestampLatchMode="START_OF_FRAME", \
    RandomLengthSeed="10900842", \
    JumboFrameThreshold="1518", \
    OversizeFrameThreshold="9018", \
    UndersizeFrameThreshold="64", \
    BurstSize="1", \
    LoadUnit="PERCENT_LINE_RATE", \
    LoadMode="FIXED", \
    FixedLoad="10", \
    RandomMaxLoad="100", \
    RandomMinLoad="10", \
    InterFrameGap="12", \
    InterFrameGapUnit="BYTES", \
    SmoothenRandomLength="FALSE", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="Generator Configuration 2")

    Analyzer_2 = (stc.get( Port_2, 'children-Analyzer' )).split(' ')[0]
    stc.config(Analyzer_2, \
    FilterOnStreamId="TRUE", \
    FilterOnInnerIP="FALSE", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="Traffic Analyzer 2")

    AnalyzerConfig_2 = (stc.get( Analyzer_2, 'children-AnalyzerConfig' )).split(' ')[0]
    stc.config(AnalyzerConfig_2, \
    TimestampLatchMode="START_OF_FRAME", \
    SigMode="ENHANCED_DETECTION", \
    HistogramMode="LATENCY", \
    JumboFrameThreshold="1518", \
    OversizeFrameThreshold="9018", \
    UndersizeFrameThreshold="64", \
    AdvSeqCheckerLateThreshold="1000", \
    VlanAlternateTpid="34984", \
    AlternateSigOffset="0", \
    LatencyMode="PER_STREAM_RX_LATENCY_ON", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="Advanced Analyzer Settings 2")

    InterarrivalTimeHistogram_2 = (stc.get( AnalyzerConfig_2, 'children-InterarrivalTimeHistogram' )).split(' ')[0]
    stc.config(InterarrivalTimeHistogram_2, \
    Description="(ns)", \
    BucketSizeList="2 4 8 16 32 64 128 256 512 1024 2048 4096 8192 16384 32768 65536", \
    LimitList="2 6 14 30 62 126 254 510 1022 2046 4094 8190 16382 32766 65534", \
    DistributionMode="CUSTOM_MODE", \
    ConfigMode="CONFIG_SIZE_MODE", \
    DistributionModeSize="1024", \
    UniformDistributionSize="8", \
    CenterPoint="568", \
    BucketSizeUnit="TEN_NANOSECONDS", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="Histograms 2")

    LatencyHistogram_2 = (stc.get( AnalyzerConfig_2, 'children-LatencyHistogram' )).split(' ')[0]
    stc.config(LatencyHistogram_2, \
    Description="(ns)", \
    BucketSizeList="2 4 8 16 32 64 128 256 512 1024 2048 4096 8192 16384 32768 65536", \
    LimitList="2 6 14 30 62 126 254 510 1022 2046 4094 8190 16382 32766 65534", \
    DistributionMode="CUSTOM_MODE", \
    ConfigMode="CONFIG_SIZE_MODE", \
    DistributionModeSize="1024", \
    UniformDistributionSize="8", \
    CenterPoint="568", \
    BucketSizeUnit="TEN_NANOSECONDS", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="Histograms 2")

    FrameLengthHistogram_2 = (stc.get( AnalyzerConfig_2, 'children-FrameLengthHistogram' )).split(' ')[0]
    stc.config(FrameLengthHistogram_2, \
    Description="(in bytes)", \
    BucketSizeList="2 4 8 16 32 64 128 256 512 1024 2048 4096 8192 16384 32768 65536", \
    LimitList="2 6 14 30 62 126 254 510 1022 2046 4094 8190 16382 32766 65534", \
    DistributionMode="CUSTOM_MODE", \
    ConfigMode="CONFIG_SIZE_MODE", \
    DistributionModeSize="1024", \
    UniformDistributionSize="8", \
    CenterPoint="568", \
    BucketSizeUnit="TEN_NANOSECONDS", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="Histograms 2")

    SeqRunLengthHistogram_2 = (stc.get( AnalyzerConfig_2, 'children-SeqRunLengthHistogram' )).split(' ')[0]
    stc.config(SeqRunLengthHistogram_2, \
    Description="(in frames)", \
    BucketSizeList="2 4 8 16 32 64 128 256 512 1024 2048 4096 8192 16384 32768 65536", \
    LimitList="2 6 14 30 62 126 254 510 1022 2046 4094 8190 16382 32766 65534", \
    DistributionMode="CUSTOM_MODE", \
    ConfigMode="CONFIG_SIZE_MODE", \
    DistributionModeSize="1024", \
    UniformDistributionSize="8", \
    CenterPoint="568", \
    BucketSizeUnit="TEN_NANOSECONDS", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="Histograms 2")

    SeqDiffCheckHistogram_2 = (stc.get( AnalyzerConfig_2, 'children-SeqDiffCheckHistogram' )).split(' ')[0]
    stc.config(SeqDiffCheckHistogram_2, \
    Description="(in deltas)", \
    BucketSizeList="2 4 8 16 32 64 128 256 512 1024 2048 4096 8192 16384 32768 65536", \
    LimitList="2 6 14 30 62 126 254 510 1022 2046 4094 8190 16382 32766 65534", \
    DistributionMode="CUSTOM_MODE", \
    ConfigMode="CONFIG_SIZE_MODE", \
    DistributionModeSize="1024", \
    UniformDistributionSize="8", \
    CenterPoint="568", \
    BucketSizeUnit="TEN_NANOSECONDS", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="Histograms 2")

    JitterHistogram_2 = (stc.get( AnalyzerConfig_2, 'children-JitterHistogram' )).split(' ')[0]
    stc.config(JitterHistogram_2, \
    Description="(ns)", \
    BucketSizeList="2 4 8 16 32 64 128 256 512 1024 2048 4096 8192 16384 32768 65536", \
    LimitList="2 6 14 30 62 126 254 510 1022 2046 4094 8190 16382 32766 65534", \
    DistributionMode="CUSTOM_MODE", \
    ConfigMode="CONFIG_SIZE_MODE", \
    DistributionModeSize="1024", \
    UniformDistributionSize="8", \
    CenterPoint="568", \
    BucketSizeUnit="TEN_NANOSECONDS", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="Histograms 2")

    DiffServConfig_2 = (stc.get( Analyzer_2, 'children-DiffServConfig' )).split(' ')[0]
    stc.config(DiffServConfig_2, \
    QualifyIpv6DstAddr="FALSE", \
    Ipv6DstAddr="ffff::ffff", \
    QualifyIpv4DstAddr="FALSE", \
    Ipv4DstAddr="0.0.0.0", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="QoS Settings 2")

    HighResolutionSamplingPortConfig_2 = (stc.get( Analyzer_2, 'children-HighResolutionSamplingPortConfig' )).split(' ')[0]
    stc.config(HighResolutionSamplingPortConfig_2, \
    BaselineSampleCount="3", \
    EnableTrigger="TRUE", \
    TriggerCondition="LESS_THAN", \
    TriggerValueUnitMode="PERCENT_BASELINE", \
    TriggerStat="TotalFrameRate", \
    TriggerValue="95", \
    TriggerLocation="20", \
    TimingMode="INTERVAL", \
    SamplingInterval="10", \
    SamplingDuration="10", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="High Resolution Port Sampling 2")

    Capture_2 = (stc.get( Port_2, 'children-Capture' )).split(' ')[0]
    stc.config(Capture_2, \
    ElapsedTime="0:00:00", \
    TabIndex="0", \
    Mode="REGULAR_MODE", \
    SrcMode="TX_RX_MODE", \
    RealTimeMode="REALTIME_DISABLE", \
    FlagMode="REGULAR_FLAG_MODE", \
    BufferMode="WRAP", \
    Start="16384", \
    Stop="0", \
    SliceMode="DISABLE", \
    SliceOffsetRef="PREAMBLE", \
    SliceOffset="0", \
    SliceCaptureSize="128", \
    RealTimeFramesBuffer="0", \
    RealTimeBufferStatus="FALSE", \
    CurrentTask="IDLE", \
    CurrentFiltersUsed="0", \
    CurrentFilterBytesUsed="0", \
    AbortSaveTask="FALSE", \
    PostStopTriggerBuffer="255", \
    CaptureFilterMode="FRAMECONTENT", \
    SaveBufferWithPreamble="FALSE", \
    IncreasedMemorySupport="FALSE", \
    Ieee80211FilterString="", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="Capture 2")

    CaptureFilter_2 = (stc.get( Capture_2, 'children-CaptureFilter' )).split(' ')[0]
    stc.config(CaptureFilter_2, \
    QualifyEvents="TRUE", \
    FilterName="", \
    SigPresent="IGNORE", \
    Oversized="IGNORE", \
    Jumbo="IGNORE", \
    Undersized="IGNORE", \
    FcsError="IGNORE", \
    Ipv4CheckSumError="IGNORE", \
    TcpUdpIgmpCheckSumError="IGNORE", \
    SigSeqNumError="IGNORE", \
    Tcp="IGNORE", \
    Udp="IGNORE", \
    Ipv4="IGNORE", \
    Ipv6="IGNORE", \
    Igmp="IGNORE", \
    FrameLenMatch="IGNORE", \
    StreamIdMatch="IGNORE", \
    PrbsError="IGNORE", \
    FilterExpression="{ None }", \
    GuiExpression="", \
    FrameLength="0", \
    StreamId="0", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="Qualify Events 2")

    CaptureFilterStartEvent_2 = (stc.get( Capture_2, 'children-CaptureFilterStartEvent' )).split(' ')[0]
    stc.config(CaptureFilterStartEvent_2, \
    StartEvents="FALSE", \
    FilterName="", \
    SigPresent="IGNORE", \
    Oversized="IGNORE", \
    Jumbo="IGNORE", \
    Undersized="IGNORE", \
    FcsError="IGNORE", \
    Ipv4CheckSumError="IGNORE", \
    TcpUdpIgmpCheckSumError="IGNORE", \
    SigSeqNumError="IGNORE", \
    Tcp="IGNORE", \
    Udp="IGNORE", \
    Ipv4="IGNORE", \
    Ipv6="IGNORE", \
    Igmp="IGNORE", \
    FrameLenMatch="IGNORE", \
    StreamIdMatch="IGNORE", \
    PrbsError="IGNORE", \
    FilterExpression="{ None }", \
    GuiExpression="", \
    FrameLength="0", \
    StreamId="0", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="Start Events 2")

    CaptureFilterStopEvent_2 = (stc.get( Capture_2, 'children-CaptureFilterStopEvent' )).split(' ')[0]
    stc.config(CaptureFilterStopEvent_2, \
    StopEvents="FALSE", \
    FilterName="", \
    SigPresent="IGNORE", \
    Oversized="IGNORE", \
    Jumbo="IGNORE", \
    Undersized="IGNORE", \
    FcsError="IGNORE", \
    Ipv4CheckSumError="IGNORE", \
    TcpUdpIgmpCheckSumError="IGNORE", \
    SigSeqNumError="IGNORE", \
    Tcp="IGNORE", \
    Udp="IGNORE", \
    Ipv4="IGNORE", \
    Ipv6="IGNORE", \
    Igmp="IGNORE", \
    FrameLenMatch="IGNORE", \
    StreamIdMatch="IGNORE", \
    PrbsError="IGNORE", \
    FilterExpression="{ None }", \
    GuiExpression="", \
    FrameLength="0", \
    StreamId="0", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="Stop Events 2")

    CaptureIeee80211_2 = (stc.get( Capture_2, 'children-CaptureIeee80211' )).split(' ')[0]
    stc.config(CaptureIeee80211_2, \
    ChannelWidth="CHANNEL_WIDTH_40M", \
    Channel="36", \
    SecondChannel="149", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="Capture IEEE 802.11 2")

    CaptureRawPacketTagsInfo_2 = (stc.get( Capture_2, 'children-CaptureRawPacketTagsInfo' )).split(' ')[0]
    stc.config(CaptureRawPacketTagsInfo_2, \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="CaptureRawPacketTagsInfo 2")

    ArpCache_2 = (stc.get( Port_2, 'children-ArpCache' )).split(' ')[0]
    stc.config(ArpCache_2, \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="ArpCache 2")

    ArpNdReport_2 = (stc.get( Port_2, 'children-ArpNdReport' )).split(' ')[0]
    stc.config(ArpNdReport_2, \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="ArpNdReport 2")

    PingReport_2 = (stc.get( Port_2, 'children-PingReport' )).split(' ')[0]
    stc.config(PingReport_2, \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="PingReport 2")

    IgmpPortConfig_2 = (stc.get( Port_2, 'children-IgmpPortConfig' )).split(' ')[0]
    stc.config(IgmpPortConfig_2, \
    RatePps="0", \
    MaxBurst="0", \
    CalculateLatencyDelay="10", \
    VlanSubFilter="OUTER", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="IgmpPortConfig 2")

    MldPortConfig_2 = (stc.get( Port_2, 'children-MldPortConfig' )).split(' ')[0]
    stc.config(MldPortConfig_2, \
    RatePps="0", \
    MaxBurst="0", \
    CalculateLatencyDelay="10", \
    VlanSubFilter="OUTER", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="MldPortConfig 2")

    OsePortConfig_2 = (stc.get( Port_2, 'children-OsePortConfig' )).split(' ')[0]
    stc.config(OsePortConfig_2, \
    VirtualSwitch="OVS_2_1", \
    ManufacturerDescription="Spirent Communications", \
    HardwareDescription="Open vSwitch", \
    SerialNumber="None", \
    DatapathDescription="None", \
    ExposeOvsdb="FALSE", \
    OvsdbPortNumber="6640", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="OsePortConfig 2")

    OvsdbPortConfig_2 = (stc.get( Port_2, 'children-OvsdbPortConfig' )).split(' ')[0]
    stc.config(OvsdbPortConfig_2, \
    ConnectionType="TCP", \
    PrivateKey="", \
    Certificate="", \
    CaCertificates="", \
    TlsConnectionOpen="FALSE", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="OVSDB Port Configuration 2")

    OpflexPortConfig_2 = (stc.get( Port_2, 'children-OpflexPortConfig' )).split(' ')[0]
    stc.config(OpflexPortConfig_2, \
    DomainName="Openstack", \
    AgentName="Agent1", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="Opflex Port Configuration 2")

    VxlanPortConfig_2 = (stc.get( Port_2, 'children-VxlanPortConfig' )).split(' ')[0]
    stc.config(VxlanPortConfig_2, \
    UdpDstPort="4789", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="VXLAN Port Configuration 2")

    QbvStreamConfig_2 = (stc.get( Port_2, 'children-QbvStreamConfig' )).split(' ')[0]
    stc.config(QbvStreamConfig_2, \
    ConfigQbvParams="FALSE", \
    GptpBaseTime="0.0", \
    GateCycleTime="1000", \
    StartTimeWithinCycle="0", \
    TickGranularityOfDut="2.5", \
    StreamStartWaitTime="0", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="QbvStreamConfig 2")

    StpPortConfig_2 = (stc.get( Port_2, 'children-StpPortConfig' )).split(' ')[0]
    stc.config(StpPortConfig_2, \
    StpType="STP", \
    PortType="TRUNK", \
    EthernetType="8100", \
    NativeVlan="1", \
    EnablePt2PtLink="FALSE", \
    EnableMacAddrReduction="FALSE", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="StpPortConfig 2")

    Dhcpv4PortConfig_2 = (stc.get( Port_2, 'children-Dhcpv4PortConfig' )).split(' ')[0]
    stc.config(Dhcpv4PortConfig_2, \
    MaxMsgSize="576", \
    LeaseTime="60", \
    MsgTimeout="60", \
    RetryCount="4", \
    RequestRate="100", \
    ReleaseRate="100", \
    StartingXid="0", \
    OutstandingSessionCount="1000", \
    SeqType="SEQUENTIAL", \
    MaxDnav4RetryCount="0", \
    Dnav4Timeout="1000", \
    EnableAssignCustomOptionsForHosts="FALSE", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="Dhcpv4PortConfig 2")

    Dhcpv6PortConfig_2 = (stc.get( Port_2, 'children-Dhcpv6PortConfig' )).split(' ')[0]
    stc.config(Dhcpv6PortConfig_2, \
    RequestRate="100", \
    ReleaseRate="100", \
    RenewRate="100", \
    SessionAutoRetry="FALSE", \
    RetryAttempts="0", \
    NoWaitMultiAdv="FALSE", \
    EnableBlockRate="FALSE", \
    SolicitTimeout="1", \
    MaxSolicitRetryTimeout="120", \
    SolicitRetryCount="10", \
    IndefSolicitRetry="FALSE", \
    DisableSolicitRetry="FALSE", \
    RequestTimeout="1", \
    MaxRequestRetryTimeout="30", \
    RequestRetryCount="10", \
    IndefRequestRetry="FALSE", \
    DisableRequestRetry="FALSE", \
    ConfirmTimeout="1", \
    MaxConfirmTimeout="4", \
    MaxConfirmDuration="10", \
    RenewTimeout="10", \
    MaxRenewRetryTimeout="600", \
    RenewRetryCount="0", \
    IndefRenewRetry="TRUE", \
    DisableRenewRetry="FALSE", \
    RebindTimeout="10", \
    MaxRebindRetryTimeout="600", \
    RebindRetryCount="0", \
    IndefRebindRetry="TRUE", \
    DisableRebindRetry="FALSE", \
    ReleaseTimeout="1", \
    ReleaseRetryCount="5", \
    IndefReleaseRetry="FALSE", \
    DisableReleaseRetry="FALSE", \
    DeclineTimeout="1", \
    DeclineRetryCount="5", \
    IndefDeclineRetry="FALSE", \
    DisableDeclineRetry="FALSE", \
    OutstandingSessionCount="1000", \
    InfoRequestTimeout="1", \
    MaxInfoRequestTimeout="120", \
    InfoRequestRetryCount="0", \
    IndefInfoRequestRetry="TRUE", \
    DisableInfoRequestRetry="FALSE", \
    LeaseTime="86400", \
    SeqType="SEQUENTIAL", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="Dhcpv6PortConfig 2")

    SaaPortConfig_2 = (stc.get( Port_2, 'children-SaaPortConfig' )).split(' ')[0]
    stc.config(SaaPortConfig_2, \
    RequestRate="300", \
    OutstandingSessionCount="1000", \
    SeqType="PARALLEL", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="SaaPortConfig 2")

    RoEPortConfig_2 = (stc.get( Port_2, 'children-RoEPortConfig' )).split(' ')[0]
    stc.config(RoEPortConfig_2, \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="RoEPortConfig 2")

    L2tpPortConfig_2 = (stc.get( Port_2, 'children-L2tpPortConfig' )).split(' ')[0]
    stc.config(L2tpPortConfig_2, \
    L2tpVersion="L2TPV2", \
    L2tpNodeType="LAC", \
    TunnelConnectRate="100", \
    SeqType="SEQUENTIAL", \
    ConnectRateV3="100", \
    DisconnectRateV3="1000", \
    SessionOutstandingV3="100", \
    CsurqRate="100", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="L2tpPortConfig 2")

    PppoxPortConfig_2 = (stc.get( Port_2, 'children-PppoxPortConfig' )).split(' ')[0]
    stc.config(PppoxPortConfig_2, \
    EmulationType="CLIENT", \
    EnableBlockRate="FALSE", \
    ConnectRate="100", \
    DisconnectRate="1000", \
    SessionOutstanding="100", \
    SeqType="SEQUENTIAL", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="PppoxPortConfig 2")

    PppProtocolConfig_2 = (stc.get( Port_2, 'children-PppProtocolConfig' )).split(' ')[0]
    stc.config(PppProtocolConfig_2, \
    PapRequestTimeout="3", \
    MaxPapRequestAttempts="10", \
    ChapChalRequestTimeout="3", \
    ChapAckTimeout="3", \
    MaxChapRequestReplyAttempts="10", \
    AutoRetryCount="65535", \
    EnableAutoRetry="FALSE", \
    EnableSessionAutoRetry="FALSE", \
    Ipv4PeerAddr="0.0.0.0", \
    Ipv6PeerAddr="::", \
    IpcpEncap="IPV4", \
    Protocol="PPPOPOS", \
    EnableMruNegotiation="TRUE", \
    EnableMagicNum="TRUE", \
    EnableNcpTermination="FALSE", \
    Authentication="NONE", \
    IncludeTxChapId="TRUE", \
    EnableOsi="FALSE", \
    EnableMpls="FALSE", \
    MruSize="1492", \
    EnableEchoRequest="FALSE", \
    EchoRequestGenFreq="10", \
    MaxEchoRequestAttempts="1", \
    LcpConfigRequestTimeout="3", \
    LcpConfigRequestMaxAttempts="10", \
    LcpTermRequestTimeout="3", \
    LcpTermRequestMaxAttempts="10", \
    NcpConfigRequestTimeout="3", \
    NcpConfigRequestMaxAttempts="10", \
    MaxNaks="5", \
    Username="spirent", \
    Password="spirent", \
    UseAuthenticationList="FALSE", \
    AuthenticationFilePath="", \
    EnablePrimaryDns="TRUE", \
    PrimaryDns="null", \
    EnableSecondaryDns="TRUE", \
    SecondaryDns="null", \
    RAMOFlag="NODHCP", \
    ConnectRate="100", \
    DisconnectRate="100", \
    UsePartialBlockState="FALSE", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="PPP 2")

    AncpPortConfig_2 = (stc.get( Port_2, 'children-AncpPortConfig' )).split(' ')[0]
    stc.config(AncpPortConfig_2, \
    EstablishRate="100", \
    TerminateRate="100", \
    SeqType="SEQUENTIAL", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="AncpPortConfig 2")

    EoamPortConfig_2 = (stc.get( Port_2, 'children-EoamPortConfig' )).split(' ')[0]
    stc.config(EoamPortConfig_2, \
    EtherType="8902", \
    MulticastMacType1="01:80:c2:00:00:30", \
    MulticastMacType2="01:80:c2:00:00:38", \
    EncodeMeLevel="TRUE", \
    DisableContChkRx="FALSE", \
    LinkTraceResponseRelayAction="DEFAULT", \
    ImmediateLinkTraceResponse="FALSE", \
    ImmediateLoopbackResponse="FALSE", \
    EchoTlvsInDelayMeasurementResponse="TRUE", \
    EchoTlvsInLossMeasurementResponse="TRUE", \
    EchoTlvsInSlr="TRUE", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="EoamPortConfig 2")

    AppPerfPortConfig_2 = (stc.get( Port_2, 'children-AppPerfPortConfig' )).split(' ')[0]
    stc.config(AppPerfPortConfig_2, \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="AppPerfPortConfig 2")

    VqAnalyzer_2 = (stc.get( Port_2, 'children-VqAnalyzer' )).split(' ')[0]
    stc.config(VqAnalyzer_2, \
    FrameLossConcealmentRobustness="4", \
    SlicesPerIframe="0", \
    NominalDelay="3", \
    MaxPktCount="65535", \
    MosVThreshold="1", \
    MosVNormalizedThreshold="1", \
    MosAvThreshold="1", \
    MosAThreshold="1", \
    PidInterval="1", \
    PatRepetition="0.5", \
    PmtRepetition="0.5", \
    PcrContinuity="0.1", \
    PcrRepetition="0.04", \
    PtsRepetition="0.7", \
    RtpTimestampThreshold="3", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="VqAnalyzer 2")

    EthernetCopper_3 = stc.create("EthernetCopper",under = Port_2, \
    AutoMdix="FALSE", \
    TestMode="NORMAL_OPERATION", \
    PerformanceMode="STC_DEFAULT", \
    LineSpeed="SPEED_1G", \
    AlternateSpeeds="", \
    AdvertiseIEEE="TRUE", \
    AdvertiseNBASET="TRUE", \
    Enable8023brPerPort="FALSE", \
    AutoNegotiation="TRUE", \
    AutoNegotiationMasterSlave="MASTER", \
    AutoNegotiationMasterSlaveEnable="TRUE", \
    DownshiftEnable="FALSE", \
    FlowControl="FALSE", \
    OptimizedXon="DISABLE", \
    PfcCableDelayType="FIBER", \
    PfcCableDelay="0", \
    Duplex="FULL", \
    CollisionExponent="10", \
    InternalPpmAdjust="0", \
    TransmitClockSource="INTERNAL", \
    ManagementRegistersTemplate="Templates/Mii/default_mii.xml", \
    IgnoreLinkStatus="FALSE", \
    DataPathMode="NORMAL", \
    Mtu="1500", \
    EnforceMtuOnRx="FALSE", \
    PortSetupMode="PORTCONFIG_ONLY", \
    ForwardErrorCorrection="TRUE", \
    CustomFecChange="0", \
    CustomFecMode="KR_FEC", \
    IgnoreFirmwareDefault="FALSE", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="Ethernet Copper Phy 2")

    Mii_3 = (stc.get( EthernetCopper_3, 'children-Mii' )).split(' ')[0]
    stc.config(Mii_3, \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="Mii 1")

    MiiRegister_65 = (stc.get( Mii_3, 'children-MiiRegister' )).split(' ')[0]
    stc.config(MiiRegister_65, \
    Address="0", \
    RegValue="4416", \
    WritableMask="65535", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="Control")

    MiiRegister_66 = (stc.get( Mii_3, 'children-MiiRegister' )).split(' ')[1]
    stc.config(MiiRegister_66, \
    Address="1", \
    RegValue="31085", \
    WritableMask="0", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="Status")

    MiiRegister_67 = (stc.get( Mii_3, 'children-MiiRegister' )).split(' ')[2]
    stc.config(MiiRegister_67, \
    Address="2", \
    RegValue="32", \
    WritableMask="0", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="PHY Identifier")

    MiiRegister_68 = (stc.get( Mii_3, 'children-MiiRegister' )).split(' ')[3]
    stc.config(MiiRegister_68, \
    Address="3", \
    RegValue="24753", \
    WritableMask="0", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="PHY Identifier")

    MiiRegister_69 = (stc.get( Mii_3, 'children-MiiRegister' )).split(' ')[4]
    stc.config(MiiRegister_69, \
    Address="4", \
    RegValue="481", \
    WritableMask="65535", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="Auto-Negotiation Advertisement")

    MiiRegister_70 = (stc.get( Mii_3, 'children-MiiRegister' )).split(' ')[5]
    stc.config(MiiRegister_70, \
    Address="5", \
    RegValue="19937", \
    WritableMask="0", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="Auto-Negotiation Link Partner Base Page Ability")

    MiiRegister_71 = (stc.get( Mii_3, 'children-MiiRegister' )).split(' ')[6]
    stc.config(MiiRegister_71, \
    Address="6", \
    RegValue="5", \
    WritableMask="0", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="Auto-Negotiation Expansion")

    MiiRegister_72 = (stc.get( Mii_3, 'children-MiiRegister' )).split(' ')[7]
    stc.config(MiiRegister_72, \
    Address="7", \
    RegValue="8193", \
    WritableMask="47103", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="Auto-Negotiation Next Page Transmit")

    MiiRegister_73 = (stc.get( Mii_3, 'children-MiiRegister' )).split(' ')[8]
    stc.config(MiiRegister_73, \
    Address="8", \
    RegValue="0", \
    WritableMask="0", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="Auto-Negotiation Link Partner Received Next Page")

    MiiRegister_74 = (stc.get( Mii_3, 'children-MiiRegister' )).split(' ')[9]
    stc.config(MiiRegister_74, \
    Address="9", \
    RegValue="512", \
    WritableMask="65535", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="MASTER-SLAVE Control Register")

    MiiRegister_75 = (stc.get( Mii_3, 'children-MiiRegister' )).split(' ')[10]
    stc.config(MiiRegister_75, \
    Address="10", \
    RegValue="0", \
    WritableMask="0", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="MASTER-SLAVE Status Register")

    MiiRegister_76 = (stc.get( Mii_3, 'children-MiiRegister' )).split(' ')[11]
    stc.config(MiiRegister_76, \
    Address="11", \
    RegValue="0", \
    WritableMask="0", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="Reserved")

    MiiRegister_77 = (stc.get( Mii_3, 'children-MiiRegister' )).split(' ')[12]
    stc.config(MiiRegister_77, \
    Address="12", \
    RegValue="0", \
    WritableMask="0", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="Reserved")

    MiiRegister_78 = (stc.get( Mii_3, 'children-MiiRegister' )).split(' ')[13]
    stc.config(MiiRegister_78, \
    Address="13", \
    RegValue="0", \
    WritableMask="0", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="Reserved")

    MiiRegister_79 = (stc.get( Mii_3, 'children-MiiRegister' )).split(' ')[14]
    stc.config(MiiRegister_79, \
    Address="14", \
    RegValue="0", \
    WritableMask="0", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="Reserved")

    MiiRegister_80 = (stc.get( Mii_3, 'children-MiiRegister' )).split(' ')[15]
    stc.config(MiiRegister_80, \
    Address="15", \
    RegValue="12288", \
    WritableMask="0", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="Extended Status")

    MiiRegister_81 = (stc.get( Mii_3, 'children-MiiRegister' )).split(' ')[16]
    stc.config(MiiRegister_81, \
    Address="16", \
    RegValue="16385", \
    WritableMask="65535", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="Vendor Specific")

    MiiRegister_82 = (stc.get( Mii_3, 'children-MiiRegister' )).split(' ')[17]
    stc.config(MiiRegister_82, \
    Address="17", \
    RegValue="768", \
    WritableMask="0", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="Vendor Specific")

    MiiRegister_83 = (stc.get( Mii_3, 'children-MiiRegister' )).split(' ')[18]
    stc.config(MiiRegister_83, \
    Address="18", \
    RegValue="0", \
    WritableMask="65535", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="Vendor Specific")

    MiiRegister_84 = (stc.get( Mii_3, 'children-MiiRegister' )).split(' ')[19]
    stc.config(MiiRegister_84, \
    Address="19", \
    RegValue="0", \
    WritableMask="65535", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="Vendor Specific")

    MiiRegister_85 = (stc.get( Mii_3, 'children-MiiRegister' )).split(' ')[20]
    stc.config(MiiRegister_85, \
    Address="20", \
    RegValue="0", \
    WritableMask="65535", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="Vendor Specific")

    MiiRegister_86 = (stc.get( Mii_3, 'children-MiiRegister' )).split(' ')[21]
    stc.config(MiiRegister_86, \
    Address="21", \
    RegValue="0", \
    WritableMask="0", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="Vendor Specific")

    MiiRegister_87 = (stc.get( Mii_3, 'children-MiiRegister' )).split(' ')[22]
    stc.config(MiiRegister_87, \
    Address="22", \
    RegValue="0", \
    WritableMask="0", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="Vendor Specific")

    MiiRegister_88 = (stc.get( Mii_3, 'children-MiiRegister' )).split(' ')[23]
    stc.config(MiiRegister_88, \
    Address="23", \
    RegValue="0", \
    WritableMask="65535", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="Vendor Specific")

    MiiRegister_89 = (stc.get( Mii_3, 'children-MiiRegister' )).split(' ')[24]
    stc.config(MiiRegister_89, \
    Address="24", \
    RegValue="25600", \
    WritableMask="65535", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="Vendor Specific")

    MiiRegister_90 = (stc.get( Mii_3, 'children-MiiRegister' )).split(' ')[25]
    stc.config(MiiRegister_90, \
    Address="25", \
    RegValue="0", \
    WritableMask="0", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="Vendor Specific")

    MiiRegister_91 = (stc.get( Mii_3, 'children-MiiRegister' )).split(' ')[26]
    stc.config(MiiRegister_91, \
    Address="26", \
    RegValue="0", \
    WritableMask="65535", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="Vendor Specific")

    MiiRegister_92 = (stc.get( Mii_3, 'children-MiiRegister' )).split(' ')[27]
    stc.config(MiiRegister_92, \
    Address="27", \
    RegValue="65535", \
    WritableMask="65535", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="Vendor Specific")

    MiiRegister_93 = (stc.get( Mii_3, 'children-MiiRegister' )).split(' ')[28]
    stc.config(MiiRegister_93, \
    Address="28", \
    RegValue="0", \
    WritableMask="0", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="Vendor Specific")

    MiiRegister_94 = (stc.get( Mii_3, 'children-MiiRegister' )).split(' ')[29]
    stc.config(MiiRegister_94, \
    Address="29", \
    RegValue="0", \
    WritableMask="0", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="Vendor Specific")

    MiiRegister_95 = (stc.get( Mii_3, 'children-MiiRegister' )).split(' ')[30]
    stc.config(MiiRegister_95, \
    Address="30", \
    RegValue="0", \
    WritableMask="0", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="Vendor Specific")

    MiiRegister_96 = (stc.get( Mii_3, 'children-MiiRegister' )).split(' ')[31]
    stc.config(MiiRegister_96, \
    Address="31", \
    RegValue="0", \
    WritableMask="0", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="Vendor Specific")

    EthernetCopper_4 = stc.create("EthernetCopper",under = Port_2, \
    AutoMdix="FALSE", \
    TestMode="NORMAL_OPERATION", \
    PerformanceMode="STC_DEFAULT", \
    LineSpeed="SPEED_1G", \
    AlternateSpeeds="", \
    AdvertiseIEEE="TRUE", \
    AdvertiseNBASET="TRUE", \
    Enable8023brPerPort="FALSE", \
    AutoNegotiation="TRUE", \
    AutoNegotiationMasterSlave="MASTER", \
    AutoNegotiationMasterSlaveEnable="TRUE", \
    DownshiftEnable="FALSE", \
    FlowControl="FALSE", \
    OptimizedXon="DISABLE", \
    PfcCableDelayType="FIBER", \
    PfcCableDelay="0", \
    Duplex="FULL", \
    CollisionExponent="10", \
    InternalPpmAdjust="0", \
    TransmitClockSource="INTERNAL", \
    ManagementRegistersTemplate="Templates/Mii/default_mii.xml", \
    IgnoreLinkStatus="FALSE", \
    DataPathMode="NORMAL", \
    Mtu="1500", \
    EnforceMtuOnRx="FALSE", \
    PortSetupMode="PORTCONFIG_ONLY", \
    ForwardErrorCorrection="TRUE", \
    CustomFecChange="0", \
    CustomFecMode="KR_FEC", \
    IgnoreFirmwareDefault="FALSE", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="Ethernet Copper Phy 4")

    Mii_4 = (stc.get( EthernetCopper_4, 'children-Mii' )).split(' ')[0]
    stc.config(Mii_4, \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="Mii 1")

    MiiRegister_97 = (stc.get( Mii_4, 'children-MiiRegister' )).split(' ')[0]
    stc.config(MiiRegister_97, \
    Address="0", \
    RegValue="4416", \
    WritableMask="65535", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="Control")

    MiiRegister_98 = (stc.get( Mii_4, 'children-MiiRegister' )).split(' ')[1]
    stc.config(MiiRegister_98, \
    Address="1", \
    RegValue="31085", \
    WritableMask="0", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="Status")

    MiiRegister_99 = (stc.get( Mii_4, 'children-MiiRegister' )).split(' ')[2]
    stc.config(MiiRegister_99, \
    Address="2", \
    RegValue="32", \
    WritableMask="0", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="PHY Identifier")

    MiiRegister_100 = (stc.get( Mii_4, 'children-MiiRegister' )).split(' ')[3]
    stc.config(MiiRegister_100, \
    Address="3", \
    RegValue="24753", \
    WritableMask="0", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="PHY Identifier")

    MiiRegister_101 = (stc.get( Mii_4, 'children-MiiRegister' )).split(' ')[4]
    stc.config(MiiRegister_101, \
    Address="4", \
    RegValue="481", \
    WritableMask="65535", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="Auto-Negotiation Advertisement")

    MiiRegister_102 = (stc.get( Mii_4, 'children-MiiRegister' )).split(' ')[5]
    stc.config(MiiRegister_102, \
    Address="5", \
    RegValue="19937", \
    WritableMask="0", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="Auto-Negotiation Link Partner Base Page Ability")

    MiiRegister_103 = (stc.get( Mii_4, 'children-MiiRegister' )).split(' ')[6]
    stc.config(MiiRegister_103, \
    Address="6", \
    RegValue="5", \
    WritableMask="0", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="Auto-Negotiation Expansion")

    MiiRegister_104 = (stc.get( Mii_4, 'children-MiiRegister' )).split(' ')[7]
    stc.config(MiiRegister_104, \
    Address="7", \
    RegValue="8193", \
    WritableMask="47103", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="Auto-Negotiation Next Page Transmit")

    MiiRegister_105 = (stc.get( Mii_4, 'children-MiiRegister' )).split(' ')[8]
    stc.config(MiiRegister_105, \
    Address="8", \
    RegValue="0", \
    WritableMask="0", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="Auto-Negotiation Link Partner Received Next Page")

    MiiRegister_106 = (stc.get( Mii_4, 'children-MiiRegister' )).split(' ')[9]
    stc.config(MiiRegister_106, \
    Address="9", \
    RegValue="512", \
    WritableMask="65535", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="MASTER-SLAVE Control Register")

    MiiRegister_107 = (stc.get( Mii_4, 'children-MiiRegister' )).split(' ')[10]
    stc.config(MiiRegister_107, \
    Address="10", \
    RegValue="0", \
    WritableMask="0", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="MASTER-SLAVE Status Register")

    MiiRegister_108 = (stc.get( Mii_4, 'children-MiiRegister' )).split(' ')[11]
    stc.config(MiiRegister_108, \
    Address="11", \
    RegValue="0", \
    WritableMask="0", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="Reserved")

    MiiRegister_109 = (stc.get( Mii_4, 'children-MiiRegister' )).split(' ')[12]
    stc.config(MiiRegister_109, \
    Address="12", \
    RegValue="0", \
    WritableMask="0", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="Reserved")

    MiiRegister_110 = (stc.get( Mii_4, 'children-MiiRegister' )).split(' ')[13]
    stc.config(MiiRegister_110, \
    Address="13", \
    RegValue="0", \
    WritableMask="0", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="Reserved")

    MiiRegister_111 = (stc.get( Mii_4, 'children-MiiRegister' )).split(' ')[14]
    stc.config(MiiRegister_111, \
    Address="14", \
    RegValue="0", \
    WritableMask="0", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="Reserved")

    MiiRegister_112 = (stc.get( Mii_4, 'children-MiiRegister' )).split(' ')[15]
    stc.config(MiiRegister_112, \
    Address="15", \
    RegValue="12288", \
    WritableMask="0", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="Extended Status")

    MiiRegister_113 = (stc.get( Mii_4, 'children-MiiRegister' )).split(' ')[16]
    stc.config(MiiRegister_113, \
    Address="16", \
    RegValue="16385", \
    WritableMask="65535", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="Vendor Specific")

    MiiRegister_114 = (stc.get( Mii_4, 'children-MiiRegister' )).split(' ')[17]
    stc.config(MiiRegister_114, \
    Address="17", \
    RegValue="768", \
    WritableMask="0", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="Vendor Specific")

    MiiRegister_115 = (stc.get( Mii_4, 'children-MiiRegister' )).split(' ')[18]
    stc.config(MiiRegister_115, \
    Address="18", \
    RegValue="0", \
    WritableMask="65535", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="Vendor Specific")

    MiiRegister_116 = (stc.get( Mii_4, 'children-MiiRegister' )).split(' ')[19]
    stc.config(MiiRegister_116, \
    Address="19", \
    RegValue="0", \
    WritableMask="65535", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="Vendor Specific")

    MiiRegister_117 = (stc.get( Mii_4, 'children-MiiRegister' )).split(' ')[20]
    stc.config(MiiRegister_117, \
    Address="20", \
    RegValue="0", \
    WritableMask="65535", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="Vendor Specific")

    MiiRegister_118 = (stc.get( Mii_4, 'children-MiiRegister' )).split(' ')[21]
    stc.config(MiiRegister_118, \
    Address="21", \
    RegValue="0", \
    WritableMask="0", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="Vendor Specific")

    MiiRegister_119 = (stc.get( Mii_4, 'children-MiiRegister' )).split(' ')[22]
    stc.config(MiiRegister_119, \
    Address="22", \
    RegValue="0", \
    WritableMask="0", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="Vendor Specific")

    MiiRegister_120 = (stc.get( Mii_4, 'children-MiiRegister' )).split(' ')[23]
    stc.config(MiiRegister_120, \
    Address="23", \
    RegValue="0", \
    WritableMask="65535", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="Vendor Specific")

    MiiRegister_121 = (stc.get( Mii_4, 'children-MiiRegister' )).split(' ')[24]
    stc.config(MiiRegister_121, \
    Address="24", \
    RegValue="25600", \
    WritableMask="65535", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="Vendor Specific")

    MiiRegister_122 = (stc.get( Mii_4, 'children-MiiRegister' )).split(' ')[25]
    stc.config(MiiRegister_122, \
    Address="25", \
    RegValue="0", \
    WritableMask="0", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="Vendor Specific")

    MiiRegister_123 = (stc.get( Mii_4, 'children-MiiRegister' )).split(' ')[26]
    stc.config(MiiRegister_123, \
    Address="26", \
    RegValue="0", \
    WritableMask="65535", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="Vendor Specific")

    MiiRegister_124 = (stc.get( Mii_4, 'children-MiiRegister' )).split(' ')[27]
    stc.config(MiiRegister_124, \
    Address="27", \
    RegValue="65535", \
    WritableMask="65535", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="Vendor Specific")

    MiiRegister_125 = (stc.get( Mii_4, 'children-MiiRegister' )).split(' ')[28]
    stc.config(MiiRegister_125, \
    Address="28", \
    RegValue="0", \
    WritableMask="0", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="Vendor Specific")

    MiiRegister_126 = (stc.get( Mii_4, 'children-MiiRegister' )).split(' ')[29]
    stc.config(MiiRegister_126, \
    Address="29", \
    RegValue="0", \
    WritableMask="0", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="Vendor Specific")

    MiiRegister_127 = (stc.get( Mii_4, 'children-MiiRegister' )).split(' ')[30]
    stc.config(MiiRegister_127, \
    Address="30", \
    RegValue="0", \
    WritableMask="0", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="Vendor Specific")

    MiiRegister_128 = (stc.get( Mii_4, 'children-MiiRegister' )).split(' ')[31]
    stc.config(MiiRegister_128, \
    Address="31", \
    RegValue="0", \
    WritableMask="0", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="Vendor Specific")

    StreamBlock_2 = stc.create("StreamBlock",under = Port_2, \
    IsControlledByGenerator="TRUE", \
    ControlledBy="generator", \
    TrafficPattern="PAIR", \
    EndpointMapping="ONE_TO_ONE", \
    EnableStreamOnlyGeneration="TRUE", \
    EnableBidirectionalTraffic="FALSE", \
    EqualRxPortDistribution="FALSE", \
    EnableTxPortSendingTrafficToSelf="FALSE", \
    EnableControlPlane="FALSE", \
    InsertSig="TRUE", \
    FrameLengthMode="FIXED", \
    FixedFrameLength="128", \
    MinFrameLength="128", \
    MaxFrameLength="256", \
    StepFrameLength="1", \
    FillType="CONSTANT", \
    ConstantFillPattern="0", \
    EnableFcsErrorInsertion="FALSE", \
    Filter="Device,MPLS-TP,Bfd,Rip,Lldp,Ieee1588v2,Ieee8021as,Bgp,Isis,Ldp,Stp,Ospfv3,Lacp,Pim,Rsvp,Ospfv2,FCoE,FCPlugin,FCoEVFPort,FCFPort,TwampClient,TwampServer,LspPing,Lisp,Srp,Trill Protocol,Otv,Openflow Protocol,Ancp,PppProtocol,PppoeProtocol,Vxlan,OSE,802.1x,OVSDB Protocol,Vepa,Opflex Protocol,Responder,IEEE 802.11 Protocol,Avbgen,RadarEmulation,TtwbProxy,ECPRI Protocol,Packet Channel,SyncE,Dhcpv4,IgmpMld,Dhcpv6,AppPerf,Cifs,Dpg,CSMP,Iperf,XMPPvJ,Ntp,Ftp,Http,RawTcp,Sip,Video,IPv4", \
    ShowAllHeaders="FALSE", \
    AllowInvalidHeaders="FALSE", \
    AutoSelectTunnel="FALSE", \
    ByPassSimpleIpSubnetChecking="FALSE", \
    EnableHighSpeedResultAnalysis="TRUE", \
    EnableBackBoneTrafficSendToSelf="TRUE", \
    EnableResolveDestMacAddress="TRUE", \
    AdvancedInterleavingGroup="0", \
    DisableTunnelBinding="FALSE", \
    Enable8023brMFrame="FALSE", \
    EnableCustomPfc="FALSE", \
    CustomPfcPriority="0", \
    TimeStampType="MIN", \
    TimeStampOffset="0", \
    FrameConfig="<frame><config><pdus><pdu name=\"ipv4_8200\" pdu=\"ipv4:IPv4\"><totalLength>20</totalLength><ttl>255</ttl><checksum>32267</checksum><sourceAddr>20.20.20.2</sourceAddr><destAddr>10.10.10.2</destAddr><prefixLength>24</prefixLength><destPrefixLength>24</destPrefixLength><gateway>20.20.20.1</gateway><tosDiffserv name=\"anon_8305\"><tos name=\"anon_8306\"><precedence>6</precedence><dBit>0</dBit><tBit>0</tBit><rBit>0</rBit><mBit>0</mBit><reserved>0</reserved></tos></tosDiffserv></pdu></pdus></config></frame>", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="StreamBlock 12-4")

    EmulatedDevice_1 = stc.create("EmulatedDevice",under = Project_1, \
    DeviceCount="1", \
    EnablePingResponse="TRUE", \
    RouterId="192.0.0.5", \
    RouterIdStep="0.0.0.1", \
    Ipv6RouterId="2000::5", \
    Ipv6RouterIdStep="::1", \
    ReadOnly="FALSE", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="Device 1")

    Ipv4If_3 = stc.create("Ipv4If",under = EmulatedDevice_1, \
    Address="10.10.10.2", \
    AddrStep="0.0.0.1", \
    AddrStepMask="255.255.255.255", \
    SkipReserved="TRUE", \
    AddrList="", \
    AddrRepeatCount="0", \
    AddrResolver="default", \
    PrefixLength="24", \
    UsePortDefaultIpv4Gateway="FALSE", \
    Gateway="10.10.10.1", \
    GatewayStep="0.0.0.0", \
    GatewayRepeatCount="0", \
    GatewayRecycleCount="0", \
    UseIpAddrRangeSettingsForGateway="FALSE", \
    GatewayList="", \
    ResolveGatewayMac="TRUE", \
    GatewayMac="00:00:00:00:00:00", \
    GatewayMacResolver="default", \
    Ttl="255", \
    TosType="TOS", \
    Tos="192", \
    NeedsAuthentication="FALSE", \
    IfCountPerLowerIf="1", \
    IfRecycleCount="0", \
    IsDecorated="FALSE", \
    IsLoopbackIf="FALSE", \
    IsRange="TRUE", \
    IsDirectlyConnected="TRUE", \
    IsRealism="FALSE", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="IPv4 7")

    EthIIIf_3 = stc.create("EthIIIf",under = EmulatedDevice_1, \
    SourceMac="00:10:94:00:00:05", \
    SrcMacStep="00:00:00:00:00:01", \
    SrcMacList="", \
    SrcMacStepMask="00:00:ff:ff:ff:ff", \
    SrcMacRepeatCount="0", \
    Authenticator="default", \
    UseDefaultPhyMac="FALSE", \
    IfCountPerLowerIf="1", \
    IfRecycleCount="0", \
    IsDecorated="FALSE", \
    IsLoopbackIf="FALSE", \
    IsRange="TRUE", \
    IsDirectlyConnected="TRUE", \
    IsRealism="FALSE", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="EthernetII 7")

    VlanIf_1 = stc.create("VlanIf",under = EmulatedDevice_1, \
    VlanId="10", \
    IdStep="1", \
    IdList="", \
    IdRepeatCount="0", \
    IdResolver="default", \
    Priority="7", \
    Cfi="0", \
    Tpid="33024", \
    IfCountPerLowerIf="1", \
    IfRecycleCount="0", \
    IsDecorated="FALSE", \
    IsLoopbackIf="FALSE", \
    IsRange="TRUE", \
    IsDirectlyConnected="TRUE", \
    IsRealism="FALSE", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="VLAN 1")

    EmulatedDeviceGenParams_1 = stc.create("EmulatedDeviceGenParams",under = Project_1, \
    BlockMode="ONE_NETWORK_PER_BLOCK", \
    RouterId="192.0.0.7", \
    RouterIdStep="0.0.0.1", \
    RouterIdSrc="MANUAL", \
    Ipv6RouterId="2000::7", \
    Ipv6RouterIdStep="::1", \
    Ipv6RouterIdSrc="MANUAL", \
    Role="", \
    DeviceTags="", \
    DuplicateNameResolution="SKIP_BLOCK_INDEX", \
    DeviceName="Device $(BlockIndex)", \
    BlockIndex="1", \
    PortType="ETHERNET", \
    Count="1", \
    CountBlockPerPort="1", \
    CountPerBlock="1", \
    GroupAssignmentMode="GROUPS_PER_PORT", \
    StepOrder="", \
    PreviewMaxCount="1000", \
    PreviewMode="FULL", \
    PreviewMaxCountPerIncrementLevel="3", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="EmulatedDeviceGenParams 1")

    DeviceGenIpv4IfParams_1 = stc.create("DeviceGenIpv4IfParams",under = EmulatedDeviceGenParams_1, \
    PrefixLength="24", \
    Addr="192.85.1.9", \
    AddrStep="0.0.0.1", \
    Gateway="192.85.1.1", \
    GatewayStep="0.0.0.0", \
    TosType="TOS", \
    Tos="192", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="DeviceGenIpv4IfParams 1")

    DeviceGenLinkedStep_1 = stc.create("DeviceGenLinkedStep",under = DeviceGenIpv4IfParams_1, \
    PropertyId="Addr", \
    LinkToId="port", \
    Step="1.0.0.0", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="DeviceGenLinkedStep 1")

    DeviceGenEthIIIfParams_1 = stc.create("DeviceGenEthIIIfParams",under = EmulatedDeviceGenParams_1, \
    SrcMac="00:10:94:00:00:07", \
    SrcMacStep="00:00:00:00:00:01", \
    UseDefaultPhyMac="FALSE", \
    EnableRfc4814Addresses="FALSE", \
    RandomSeedValue="4814", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="DeviceGenEthIIIfParams 1")

    EmulatedDevice_2 = stc.create("EmulatedDevice",under = Project_1, \
    DeviceCount="1", \
    EnablePingResponse="TRUE", \
    RouterId="192.0.0.6", \
    RouterIdStep="0.0.0.1", \
    Ipv6RouterId="2000::6", \
    Ipv6RouterIdStep="::1", \
    ReadOnly="FALSE", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="Device 2")

    Ipv4If_4 = stc.create("Ipv4If",under = EmulatedDevice_2, \
    Address="20.20.20.2", \
    AddrStep="0.0.0.1", \
    AddrStepMask="255.255.255.255", \
    SkipReserved="TRUE", \
    AddrList="", \
    AddrRepeatCount="0", \
    AddrResolver="default", \
    PrefixLength="24", \
    UsePortDefaultIpv4Gateway="FALSE", \
    Gateway="20.20.20.1", \
    GatewayStep="0.0.0.0", \
    GatewayRepeatCount="0", \
    GatewayRecycleCount="0", \
    UseIpAddrRangeSettingsForGateway="FALSE", \
    GatewayList="", \
    ResolveGatewayMac="TRUE", \
    GatewayMac="00:00:00:00:00:00", \
    GatewayMacResolver="default", \
    Ttl="255", \
    TosType="TOS", \
    Tos="192", \
    NeedsAuthentication="FALSE", \
    IfCountPerLowerIf="1", \
    IfRecycleCount="0", \
    IsDecorated="FALSE", \
    IsLoopbackIf="FALSE", \
    IsRange="TRUE", \
    IsDirectlyConnected="TRUE", \
    IsRealism="FALSE", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="IPv4 8")

    EthIIIf_4 = stc.create("EthIIIf",under = EmulatedDevice_2, \
    SourceMac="00:10:94:00:00:06", \
    SrcMacStep="00:00:00:00:00:01", \
    SrcMacList="", \
    SrcMacStepMask="00:00:ff:ff:ff:ff", \
    SrcMacRepeatCount="0", \
    Authenticator="default", \
    UseDefaultPhyMac="FALSE", \
    IfCountPerLowerIf="1", \
    IfRecycleCount="0", \
    IsDecorated="FALSE", \
    IsLoopbackIf="FALSE", \
    IsRange="TRUE", \
    IsDirectlyConnected="TRUE", \
    IsRealism="FALSE", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="EthernetII 8")

    VlanIf_2 = stc.create("VlanIf",under = EmulatedDevice_2, \
    VlanId="20", \
    IdStep="1", \
    IdList="", \
    IdRepeatCount="0", \
    IdResolver="default", \
    Priority="7", \
    Cfi="0", \
    Tpid="33024", \
    IfCountPerLowerIf="1", \
    IfRecycleCount="0", \
    IsDecorated="FALSE", \
    IsLoopbackIf="FALSE", \
    IsRange="TRUE", \
    IsDirectlyConnected="TRUE", \
    IsRealism="FALSE", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="VLAN 2")

    DynamicResultView_2 = stc.create("DynamicResultView",under = Project_1, \
    ResultSourceClass="Port", \
    SaveToConfig="TRUE", \
    Identifier="Port Traffic and Counters\\Aggregate Port L1 Rx Rate", \
    Persistent="TRUE", \
    CreatorId="", \
    IsDeprecated="FALSE", \
    Path="Port Traffic", \
    ResultViewOwner="SYSTEM", \
    Description="object://core/DynamicResultView", \
    CustomDisplayName="", \
    CustomDisplayPath="Port Traffic and Counters", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="Aggregate Port L1 Rx Rate")

    PresentationResultQuery_2 = stc.create("PresentationResultQuery",under = DynamicResultView_2, \
    SelectProperties="Port.RxL1BitRate Port.RxMaxLineRate Project.Name", \
    WhereConditions="", \
    GroupByProperties="Project.Name", \
    LimitOffset="0", \
    LimitSize="2000", \
    SortBy="", \
    ArchivingOption="NONE", \
    ResultState="IDLE", \
    ArchivingInterval="10", \
    DatabaseFileName="", \
    DisableAutoGrouping="FALSE", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="PresentationResultQuery 2")

    ColumnDisplayProperties_4 = stc.create("ColumnDisplayProperties",under = DynamicResultView_2, \
    ColumnPropertyId="Port.RxL1BitRate", \
    ColumnCaption="Rx L1 Rate", \
    ColumnWidth="0", \
    ColumnUnits="5", \
    ColumnPrecision="255", \
    ColumnGroups="", \
    ColumnSortIndex="0", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="ColumnDisplayProperties 3")

    ColumnDisplayProperties_5 = stc.create("ColumnDisplayProperties",under = DynamicResultView_2, \
    ColumnPropertyId="Port.RxMaxLineRate", \
    ColumnCaption="Rx Max Line Rate", \
    ColumnWidth="0", \
    ColumnUnits="5", \
    ColumnPrecision="255", \
    ColumnGroups="", \
    ColumnSortIndex="0", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="ColumnDisplayProperties 4")

    ColumnDisplayProperties_6 = stc.create("ColumnDisplayProperties",under = DynamicResultView_2, \
    ColumnPropertyId="Project.Name", \
    ColumnCaption="Project Name", \
    ColumnWidth="0", \
    ColumnUnits="5", \
    ColumnPrecision="255", \
    ColumnGroups="", \
    ColumnSortIndex="0", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="ColumnDisplayProperties 5")

    StreamBlockLoadProfile_1 = stc.create("StreamBlockLoadProfile",under = Project_1, \
    Load="10", \
    LoadUnit="PERCENT_LINE_RATE", \
    BurstSize="1", \
    InterFrameGap="12", \
    InterFrameGapUnit="BYTES", \
    StartDelay="0", \
    Priority="0", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="StreamBlockLoadProfile 15")

    StreamBlockLoadProfile_2 = stc.create("StreamBlockLoadProfile",under = Project_1, \
    Load="10", \
    LoadUnit="PERCENT_LINE_RATE", \
    BurstSize="1", \
    InterFrameGap="12", \
    InterFrameGapUnit="BYTES", \
    StartDelay="0", \
    Priority="0", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="StreamBlockLoadProfile 16")

    ResultDataSet_2 = stc.create("ResultDataSet",under = Project_1, \
    PrimaryClass="TxStreamResults", \
    InternalXmlFormatString="", \
    ResultFilterMode="1", \
    ResultViewDataOutput="FALSE", \
    PageNumber="1", \
    RecordsPerPage="25", \
    NotifyInterval="1000", \
    Identifier="Stream Results\\Detailed Stream Results", \
    Persistent="TRUE", \
    CreatorId="", \
    IsDeprecated="FALSE", \
    Path="Stream Results", \
    ResultViewOwner="SYSTEM", \
    Description="object://l2l3/TxStreamResults", \
    CustomDisplayName="", \
    CustomDisplayPath="Streams", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="Detailed Stream Results")

    RealTimeResultGroupDefinition_11 = stc.create("RealTimeResultGroupDefinition",under = ResultDataSet_2, \
    GroupName="All Groups", \
    GroupId="core://allgroups/", \
    ColumnClassName="TxStreamResults", \
    ColumnPropertyName="StreamInfo", \
    CountQuery="", \
    SqlString="", \
    UseCustomSqlString="FALSE", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="RealTimeResultGroupDefinition 11")

    RealTimeResultGroupDefinition_12 = stc.create("RealTimeResultGroupDefinition",under = ResultDataSet_2, \
    GroupName="Basic Counters", \
    GroupId="object://customgroup/a7d38eca-b341-4d2f-9c5b-400e46180add/Basic Counters", \
    ColumnClassName="Port RxStreamSummaryResults RxStreamSummaryResults RxStreamSummaryResults TxStreamResults RxStreamSummaryResults TxStreamResults RxStreamSummaryResults TxStreamResults RxStreamSummaryResults TxStreamResults RxStreamSummaryResults TxStreamResults RxStreamSummaryResults TxStreamResults RxStreamSummaryResults RxStreamSummaryResults RxStreamSummaryResults RxStreamSummaryResults RxStreamSummaryResults RxStreamSummaryResults RxStreamSummaryResults RxStreamSummaryResults RxStreamSummaryResults RxStreamSummaryResults RxStreamSummaryResults RxStreamSummaryResults RxStreamSummaryResults RxStreamSummaryResults RxStreamSummaryResults TxStreamResults", \
    ColumnPropertyName="Name PortUiName AggregatedRxPortCount PortStrayFrames FrameCount FrameCount BitRate BitRate BitCount BitCount L1BitCount L1BitCount L1BitRate L1BitRate FrameRate FrameRate SigFrameCount SigFrameRate ShortTermAvgLatency AvgLatency MinLatency MaxLatency ShortTermAvgJitter AvgJitter MinJitter MaxJitter ShortTermAvgInterarrivalTime AvgInterarrivalTime MinInterarrivalTime MaxInterarrivalTime ExpectedRxFrameCount", \
    CountQuery="select count(*) from (select TxStreamId from TxRxEotStreamResults group by DataSetId, TxStreamId)", \
    SqlString="select TxPortName as 'Tx Port', group_concat(distinct ActualRxPortName) as 'Rx Port', TxStreamBlockName as 'Stream Block', TxStreamId as 'Stream Id', TxStreamIndex as 'Stream Index', (case when MIN(coalesce(IsExpectedPort,1)) = 0 then 'YES' else 'NO' end) as 'Port Stray Frames', TxFrameCount as 'Tx Count (Frames)', coalesce(sum(FrameCount), 0) as 'Rx Count (Frames)', coalesce(sum(SigFrameCount), 0) as 'Sig Count (Frames)', (TxOctetCount * 8) as 'Tx Count (bits)', coalesce(sum(OctetCount * 8), 0) as 'Rx Count (bits)', TxL1BitCount as 'Tx L1 Count (bits)', coalesce(sum(L1BitCount), 0) as 'Rx L1 Count (bits)', coalesce(round(sum(TotalLatency) / 100.0 / sum(SigFrameCount), 3), '') as 'Avg Latency (us)', coalesce(min(MinLatency), 0.0) as 'Min Latency (us)', coalesce(max(MaxLatency), 0.0) as 'Max Latency (us)', (case when (sum(TotalJitter) < 0.001 and coalesce(avg(AvgJitter), 0) > 0) then round(avg(AvgJitter), 3) when ((InJitterModeRfc3393 and ModInSeqFrameCount < 1) or (not InJitterModeRfc3393 and ModSigFrameCount < 1)) then '' when (InJitterModeRfc3393) then coalesce(round(sum(TotalJitter) / 100.0 / sum(ModInSeqFrameCount), 3), '') else coalesce(round(sum(TotalJitter) / 100.0 / sum(ModSigFrameCount), 3), '') end) as 'Avg Jitter (us)', coalesce(min(MinJitter), 0.0) as 'Min Jitter (us)', coalesce(max(MaxJitter), 0.0) as 'Max Jitter (us)', coalesce(round(sum(TotalInterarrivalTime) / 100.0 / sum(ModFrameCount), 3), '') as 'Avg Inter-arrival Time (us)', coalesce(min(MinInterarrivalTime), 0.0) as 'Min Inter-arrival Time (us)', coalesce(max(MaxInterarrivalTime), 0.0) as 'Max Inter-arrival Time (us)', TxCellCount as 'Tx Count (Cells)', coalesce(sum(CellCount), 0) as 'Rx Count (Cells)' from TxRxEotStreamResults where isExpectedPort=1 group by DataSetId, TxStreamId", \
    UseCustomSqlString="TRUE", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="RealTimeResultGroupDefinition 12")

    ResultQuery_3 = stc.create("ResultQuery",under = ResultDataSet_2, \
    ConfigClassId="streamblock", \
    ResultClassId="rxstreamsummaryresults", \
    PropertyIdArray="rxbasicresults.framecount rxbasicresults.sigframecount rxbasicresults.fcserrorframecount rxbasicresults.minlatency rxbasicresults.maxlatency rxbasicresults.droppedframecount rxbasicresults.droppedframepercent rxbasicresults.inorderframecount rxbasicresults.reorderedframecount rxbasicresults.duplicateframecount rxbasicresults.lateframecount rxbasicresults.prbsbiterrorcount rxbasicresults.prbsfilloctetcount rxbasicresults.ipv4checksumerrorcount rxbasicresults.tcpudpchecksumerrorcount rxbasicresults.framerate rxbasicresults.sigframerate rxbasicresults.fcserrorframerate rxbasicresults.droppedframerate rxbasicresults.droppedframepercentrate rxbasicresults.inorderframerate rxbasicresults.reorderedframerate rxbasicresults.duplicateframerate rxbasicresults.lateframerate rxbasicresults.prbsbiterrorrate rxbasicresults.prbsfilloctetrate rxbasicresults.ipv4checksumerrorrate rxbasicresults.tcpudpchecksumerrorrate rxbasicresults.bitrate rxbasicresults.shorttermavglatency rxbasicresults.avglatency rxbasicresults.prbsbiterrorratio rxbasicresults.l1bitcount rxbasicresults.l1bitrate rxbasicresults.prbserrorframecount rxbasicresults.prbserrorframerate rxstreamsummaryresults.aggregatedrxportcount rxbasicresults.portstrayframes rxbasicresults.bitcount rxbasicresults.shorttermavgjitter rxbasicresults.avgjitter rxbasicresults.minjitter rxbasicresults.maxjitter rxbasicresults.shorttermavginterarrivaltime rxbasicresults.avginterarrivaltime rxbasicresults.mininterarrivaltime rxbasicresults.maxinterarrivaltime rxbasicresults.inseqframecount rxbasicresults.outseqframecount rxbasicresults.inseqframerate rxbasicresults.outseqframerate rxbasicresults.histbin1count rxbasicresults.histbin2count rxbasicresults.histbin3count rxbasicresults.histbin4count rxbasicresults.histbin5count rxbasicresults.histbin6count rxbasicresults.histbin7count rxbasicresults.histbin8count rxbasicresults.histbin9count rxbasicresults.histbin10count rxbasicresults.histbin11count rxbasicresults.histbin12count rxbasicresults.histbin13count rxbasicresults.histbin14count rxbasicresults.histbin15count rxbasicresults.histbin16count", \
    ResultOptions="Basic", \
    ArchivingOption="NONE", \
    InternalCookie="", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="ResultQuery 6")

    ResultQuery_4 = stc.create("ResultQuery",under = ResultDataSet_2, \
    ConfigClassId="streamblock", \
    ResultClassId="txstreamresults", \
    PropertyIdArray="txbasicresults.framecount txbasicresults.framerate txbasicresults.bitrate txstreamresults.expectedrxframecount txbasicresults.l1bitcount txbasicresults.l1bitrate txstreamresults.streaminfo txbasicresults.bitcount", \
    ResultOptions="Basic", \
    ArchivingOption="NONE", \
    InternalCookie="", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="ResultQuery 7")

    RealTimeResultColumnDefinition_152 = stc.create("RealTimeResultColumnDefinition",under = ResultDataSet_2, \
    ColumnClassName="TxStreamResults", \
    ColumnPropertyName="StreamInfo", \
    ColumnDescription="", \
    ColumnWidth="74", \
    ColumnUnits="0", \
    ColumnPrecision="2", \
    ColumnSortType="NONE", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="RealTimeResultColumnDefinition 119")

    RealTimeResultColumnDefinition_153 = stc.create("RealTimeResultColumnDefinition",under = ResultDataSet_2, \
    ColumnClassName="Port", \
    ColumnPropertyName="Name", \
    ColumnDescription="", \
    ColumnWidth="85", \
    ColumnUnits="0", \
    ColumnPrecision="2", \
    ColumnSortType="NONE", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="RealTimeResultColumnDefinition 120")

    RealTimeResultColumnDefinition_154 = stc.create("RealTimeResultColumnDefinition",under = ResultDataSet_2, \
    ColumnClassName="RxStreamSummaryResults", \
    ColumnPropertyName="PortUiName", \
    ColumnDescription="", \
    ColumnWidth="65", \
    ColumnUnits="0", \
    ColumnPrecision="2", \
    ColumnSortType="NONE", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="RealTimeResultColumnDefinition 121")

    RealTimeResultColumnDefinition_155 = stc.create("RealTimeResultColumnDefinition",under = ResultDataSet_2, \
    ColumnClassName="RxStreamSummaryResults", \
    ColumnPropertyName="AggregatedRxPortCount", \
    ColumnDescription="", \
    ColumnWidth="85", \
    ColumnUnits="0", \
    ColumnPrecision="2", \
    ColumnSortType="NONE", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="RealTimeResultColumnDefinition 122")

    RealTimeResultColumnDefinition_156 = stc.create("RealTimeResultColumnDefinition",under = ResultDataSet_2, \
    ColumnClassName="RxStreamSummaryResults", \
    ColumnPropertyName="PortStrayFrames", \
    ColumnDescription="", \
    ColumnWidth="75", \
    ColumnUnits="0", \
    ColumnPrecision="2", \
    ColumnSortType="NONE", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="RealTimeResultColumnDefinition 123")

    RealTimeResultColumnDefinition_157 = stc.create("RealTimeResultColumnDefinition",under = ResultDataSet_2, \
    ColumnClassName="TxStreamResults", \
    ColumnPropertyName="FrameCount", \
    ColumnDescription="", \
    ColumnWidth="97", \
    ColumnUnits="16", \
    ColumnPrecision="2", \
    ColumnSortType="NONE", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="RealTimeResultColumnDefinition 124")

    RealTimeResultColumnDefinition_158 = stc.create("RealTimeResultColumnDefinition",under = ResultDataSet_2, \
    ColumnClassName="RxStreamSummaryResults", \
    ColumnPropertyName="FrameCount", \
    ColumnDescription="", \
    ColumnWidth="97", \
    ColumnUnits="16", \
    ColumnPrecision="2", \
    ColumnSortType="NONE", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="RealTimeResultColumnDefinition 125")

    RealTimeResultColumnDefinition_159 = stc.create("RealTimeResultColumnDefinition",under = ResultDataSet_2, \
    ColumnClassName="TxStreamResults", \
    ColumnPropertyName="BitRate", \
    ColumnDescription="", \
    ColumnWidth="100", \
    ColumnUnits="7", \
    ColumnPrecision="2", \
    ColumnSortType="NONE", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="RealTimeResultColumnDefinition 126")

    RealTimeResultColumnDefinition_160 = stc.create("RealTimeResultColumnDefinition",under = ResultDataSet_2, \
    ColumnClassName="RxStreamSummaryResults", \
    ColumnPropertyName="BitRate", \
    ColumnDescription="", \
    ColumnWidth="100", \
    ColumnUnits="7", \
    ColumnPrecision="2", \
    ColumnSortType="NONE", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="RealTimeResultColumnDefinition 127")

    RealTimeResultColumnDefinition_161 = stc.create("RealTimeResultColumnDefinition",under = ResultDataSet_2, \
    ColumnClassName="TxStreamResults", \
    ColumnPropertyName="BitCount", \
    ColumnDescription="", \
    ColumnWidth="100", \
    ColumnUnits="1", \
    ColumnPrecision="2", \
    ColumnSortType="NONE", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="RealTimeResultColumnDefinition 128")

    RealTimeResultColumnDefinition_162 = stc.create("RealTimeResultColumnDefinition",under = ResultDataSet_2, \
    ColumnClassName="RxStreamSummaryResults", \
    ColumnPropertyName="BitCount", \
    ColumnDescription="", \
    ColumnWidth="100", \
    ColumnUnits="1", \
    ColumnPrecision="2", \
    ColumnSortType="NONE", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="RealTimeResultColumnDefinition 129")

    RealTimeResultColumnDefinition_163 = stc.create("RealTimeResultColumnDefinition",under = ResultDataSet_2, \
    ColumnClassName="TxStreamResults", \
    ColumnPropertyName="L1BitCount", \
    ColumnDescription="", \
    ColumnWidth="100", \
    ColumnUnits="1", \
    ColumnPrecision="2", \
    ColumnSortType="NONE", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="RealTimeResultColumnDefinition 130")

    RealTimeResultColumnDefinition_164 = stc.create("RealTimeResultColumnDefinition",under = ResultDataSet_2, \
    ColumnClassName="RxStreamSummaryResults", \
    ColumnPropertyName="L1BitCount", \
    ColumnDescription="", \
    ColumnWidth="100", \
    ColumnUnits="1", \
    ColumnPrecision="2", \
    ColumnSortType="NONE", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="RealTimeResultColumnDefinition 131")

    RealTimeResultColumnDefinition_165 = stc.create("RealTimeResultColumnDefinition",under = ResultDataSet_2, \
    ColumnClassName="TxStreamResults", \
    ColumnPropertyName="L1BitRate", \
    ColumnDescription="", \
    ColumnWidth="100", \
    ColumnUnits="7", \
    ColumnPrecision="2", \
    ColumnSortType="NONE", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="RealTimeResultColumnDefinition 132")

    RealTimeResultColumnDefinition_166 = stc.create("RealTimeResultColumnDefinition",under = ResultDataSet_2, \
    ColumnClassName="RxStreamSummaryResults", \
    ColumnPropertyName="L1BitRate", \
    ColumnDescription="", \
    ColumnWidth="100", \
    ColumnUnits="7", \
    ColumnPrecision="2", \
    ColumnSortType="NONE", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="RealTimeResultColumnDefinition 133")

    RealTimeResultColumnDefinition_167 = stc.create("RealTimeResultColumnDefinition",under = ResultDataSet_2, \
    ColumnClassName="TxStreamResults", \
    ColumnPropertyName="FrameRate", \
    ColumnDescription="", \
    ColumnWidth="90", \
    ColumnUnits="17", \
    ColumnPrecision="2", \
    ColumnSortType="NONE", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="RealTimeResultColumnDefinition 134")

    RealTimeResultColumnDefinition_168 = stc.create("RealTimeResultColumnDefinition",under = ResultDataSet_2, \
    ColumnClassName="RxStreamSummaryResults", \
    ColumnPropertyName="FrameRate", \
    ColumnDescription="", \
    ColumnWidth="91", \
    ColumnUnits="17", \
    ColumnPrecision="2", \
    ColumnSortType="NONE", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="RealTimeResultColumnDefinition 247")

    RealTimeResultColumnDefinition_169 = stc.create("RealTimeResultColumnDefinition",under = ResultDataSet_2, \
    ColumnClassName="RxStreamSummaryResults", \
    ColumnPropertyName="SigFrameCount", \
    ColumnDescription="", \
    ColumnWidth="116", \
    ColumnUnits="16", \
    ColumnPrecision="2", \
    ColumnSortType="NONE", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="RealTimeResultColumnDefinition 248")

    RealTimeResultColumnDefinition_170 = stc.create("RealTimeResultColumnDefinition",under = ResultDataSet_2, \
    ColumnClassName="RxStreamSummaryResults", \
    ColumnPropertyName="SigFrameRate", \
    ColumnDescription="", \
    ColumnWidth="109", \
    ColumnUnits="17", \
    ColumnPrecision="2", \
    ColumnSortType="NONE", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="RealTimeResultColumnDefinition 249")

    RealTimeResultColumnDefinition_171 = stc.create("RealTimeResultColumnDefinition",under = ResultDataSet_2, \
    ColumnClassName="RxStreamSummaryResults", \
    ColumnPropertyName="ShortTermAvgLatency", \
    ColumnDescription="", \
    ColumnWidth="123", \
    ColumnUnits="9", \
    ColumnPrecision="2", \
    ColumnSortType="NONE", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="RealTimeResultColumnDefinition 250")

    RealTimeResultColumnDefinition_172 = stc.create("RealTimeResultColumnDefinition",under = ResultDataSet_2, \
    ColumnClassName="RxStreamSummaryResults", \
    ColumnPropertyName="AvgLatency", \
    ColumnDescription="", \
    ColumnWidth="123", \
    ColumnUnits="9", \
    ColumnPrecision="2", \
    ColumnSortType="NONE", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="RealTimeResultColumnDefinition 247")

    RealTimeResultColumnDefinition_173 = stc.create("RealTimeResultColumnDefinition",under = ResultDataSet_2, \
    ColumnClassName="RxStreamSummaryResults", \
    ColumnPropertyName="MinLatency", \
    ColumnDescription="", \
    ColumnWidth="100", \
    ColumnUnits="9", \
    ColumnPrecision="2", \
    ColumnSortType="NONE", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="RealTimeResultColumnDefinition 248")

    RealTimeResultColumnDefinition_174 = stc.create("RealTimeResultColumnDefinition",under = ResultDataSet_2, \
    ColumnClassName="RxStreamSummaryResults", \
    ColumnPropertyName="MaxLatency", \
    ColumnDescription="", \
    ColumnWidth="103", \
    ColumnUnits="9", \
    ColumnPrecision="2", \
    ColumnSortType="NONE", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="RealTimeResultColumnDefinition 249")

    RealTimeResultColumnDefinition_175 = stc.create("RealTimeResultColumnDefinition",under = ResultDataSet_2, \
    ColumnClassName="RxStreamSummaryResults", \
    ColumnPropertyName="ShortTermAvgJitter", \
    ColumnDescription="", \
    ColumnWidth="123", \
    ColumnUnits="22", \
    ColumnPrecision="2", \
    ColumnSortType="NONE", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="RealTimeResultColumnDefinition 250")

    RealTimeResultColumnDefinition_176 = stc.create("RealTimeResultColumnDefinition",under = ResultDataSet_2, \
    ColumnClassName="RxStreamSummaryResults", \
    ColumnPropertyName="AvgJitter", \
    ColumnDescription="", \
    ColumnWidth="123", \
    ColumnUnits="22", \
    ColumnPrecision="2", \
    ColumnSortType="NONE", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="RealTimeResultColumnDefinition 135")

    RealTimeResultColumnDefinition_177 = stc.create("RealTimeResultColumnDefinition",under = ResultDataSet_2, \
    ColumnClassName="RxStreamSummaryResults", \
    ColumnPropertyName="MinJitter", \
    ColumnDescription="", \
    ColumnWidth="100", \
    ColumnUnits="22", \
    ColumnPrecision="2", \
    ColumnSortType="NONE", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="RealTimeResultColumnDefinition 136")

    RealTimeResultColumnDefinition_178 = stc.create("RealTimeResultColumnDefinition",under = ResultDataSet_2, \
    ColumnClassName="RxStreamSummaryResults", \
    ColumnPropertyName="MaxJitter", \
    ColumnDescription="", \
    ColumnWidth="103", \
    ColumnUnits="22", \
    ColumnPrecision="2", \
    ColumnSortType="NONE", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="RealTimeResultColumnDefinition 137")

    RealTimeResultColumnDefinition_179 = stc.create("RealTimeResultColumnDefinition",under = ResultDataSet_2, \
    ColumnClassName="RxStreamSummaryResults", \
    ColumnPropertyName="ShortTermAvgInterarrivalTime", \
    ColumnDescription="", \
    ColumnWidth="123", \
    ColumnUnits="22", \
    ColumnPrecision="2", \
    ColumnSortType="NONE", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="RealTimeResultColumnDefinition 138")

    RealTimeResultColumnDefinition_180 = stc.create("RealTimeResultColumnDefinition",under = ResultDataSet_2, \
    ColumnClassName="RxStreamSummaryResults", \
    ColumnPropertyName="AvgInterarrivalTime", \
    ColumnDescription="", \
    ColumnWidth="123", \
    ColumnUnits="22", \
    ColumnPrecision="2", \
    ColumnSortType="NONE", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="RealTimeResultColumnDefinition 139")

    RealTimeResultColumnDefinition_181 = stc.create("RealTimeResultColumnDefinition",under = ResultDataSet_2, \
    ColumnClassName="RxStreamSummaryResults", \
    ColumnPropertyName="MinInterarrivalTime", \
    ColumnDescription="", \
    ColumnWidth="100", \
    ColumnUnits="22", \
    ColumnPrecision="2", \
    ColumnSortType="NONE", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="RealTimeResultColumnDefinition 140")

    RealTimeResultColumnDefinition_182 = stc.create("RealTimeResultColumnDefinition",under = ResultDataSet_2, \
    ColumnClassName="RxStreamSummaryResults", \
    ColumnPropertyName="MaxInterarrivalTime", \
    ColumnDescription="", \
    ColumnWidth="103", \
    ColumnUnits="22", \
    ColumnPrecision="2", \
    ColumnSortType="NONE", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="RealTimeResultColumnDefinition 141")

    RealTimeResultColumnDefinition_183 = stc.create("RealTimeResultColumnDefinition",under = ResultDataSet_2, \
    ColumnClassName="TxStreamResults", \
    ColumnPropertyName="ExpectedRxFrameCount", \
    ColumnDescription="", \
    ColumnWidth="85", \
    ColumnUnits="16", \
    ColumnPrecision="2", \
    ColumnSortType="NONE", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="RealTimeResultColumnDefinition 143")

    RealTimeResultColumnDefinition_184 = stc.create("RealTimeResultColumnDefinition",under = ResultDataSet_2, \
    ColumnClassName="RxStreamSummaryResults", \
    ColumnPropertyName="Ipv4ChecksumErrorCount", \
    ColumnDescription="", \
    ColumnWidth="171", \
    ColumnUnits="0", \
    ColumnPrecision="2", \
    ColumnSortType="NONE", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="RealTimeResultColumnDefinition 144")

    RealTimeResultColumnDefinition_185 = stc.create("RealTimeResultColumnDefinition",under = ResultDataSet_2, \
    ColumnClassName="RxStreamSummaryResults", \
    ColumnPropertyName="TcpUdpChecksumErrorCount", \
    ColumnDescription="", \
    ColumnWidth="194", \
    ColumnUnits="0", \
    ColumnPrecision="2", \
    ColumnSortType="NONE", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="RealTimeResultColumnDefinition 145")

    RealTimeResultColumnDefinition_186 = stc.create("RealTimeResultColumnDefinition",under = ResultDataSet_2, \
    ColumnClassName="RxStreamSummaryResults", \
    ColumnPropertyName="PrbsBitErrorCount", \
    ColumnDescription="", \
    ColumnWidth="121", \
    ColumnUnits="1", \
    ColumnPrecision="2", \
    ColumnSortType="NONE", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="RealTimeResultColumnDefinition 146")

    RealTimeResultColumnDefinition_187 = stc.create("RealTimeResultColumnDefinition",under = ResultDataSet_2, \
    ColumnClassName="RxStreamSummaryResults", \
    ColumnPropertyName="PrbsFillOctetCount", \
    ColumnDescription="", \
    ColumnWidth="123", \
    ColumnUnits="12", \
    ColumnPrecision="2", \
    ColumnSortType="NONE", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="RealTimeResultColumnDefinition 148")

    RealTimeResultColumnDefinition_188 = stc.create("RealTimeResultColumnDefinition",under = ResultDataSet_2, \
    ColumnClassName="RxStreamSummaryResults", \
    ColumnPropertyName="PrbsBitErrorRatio", \
    ColumnDescription="", \
    ColumnWidth="100", \
    ColumnUnits="0", \
    ColumnPrecision="2", \
    ColumnSortType="NONE", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="RealTimeResultColumnDefinition 149")

    RealTimeResultColumnDefinition_189 = stc.create("RealTimeResultColumnDefinition",under = ResultDataSet_2, \
    ColumnClassName="RxStreamSummaryResults", \
    ColumnPropertyName="FcsErrorFrameCount", \
    ColumnDescription="", \
    ColumnWidth="148", \
    ColumnUnits="16", \
    ColumnPrecision="2", \
    ColumnSortType="NONE", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="RealTimeResultColumnDefinition 150")

    RealTimeResultColumnDefinition_190 = stc.create("RealTimeResultColumnDefinition",under = ResultDataSet_2, \
    ColumnClassName="RxStreamSummaryResults", \
    ColumnPropertyName="Ipv4ChecksumErrorRate", \
    ColumnDescription="", \
    ColumnWidth="164", \
    ColumnUnits="0", \
    ColumnPrecision="2", \
    ColumnSortType="NONE", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="RealTimeResultColumnDefinition 151")

    RealTimeResultColumnDefinition_191 = stc.create("RealTimeResultColumnDefinition",under = ResultDataSet_2, \
    ColumnClassName="RxStreamSummaryResults", \
    ColumnPropertyName="TcpUdpChecksumErrorRate", \
    ColumnDescription="", \
    ColumnWidth="187", \
    ColumnUnits="0", \
    ColumnPrecision="2", \
    ColumnSortType="NONE", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="RealTimeResultColumnDefinition 152")

    RealTimeResultColumnDefinition_192 = stc.create("RealTimeResultColumnDefinition",under = ResultDataSet_2, \
    ColumnClassName="RxStreamSummaryResults", \
    ColumnPropertyName="PrbsBitErrorRate", \
    ColumnDescription="", \
    ColumnWidth="130", \
    ColumnUnits="7", \
    ColumnPrecision="2", \
    ColumnSortType="NONE", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="RealTimeResultColumnDefinition 153")

    RealTimeResultColumnDefinition_193 = stc.create("RealTimeResultColumnDefinition",under = ResultDataSet_2, \
    ColumnClassName="RxStreamSummaryResults", \
    ColumnPropertyName="PrbsFillOctetRate", \
    ColumnDescription="", \
    ColumnWidth="117", \
    ColumnUnits="18", \
    ColumnPrecision="2", \
    ColumnSortType="NONE", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="RealTimeResultColumnDefinition 154")

    RealTimeResultColumnDefinition_194 = stc.create("RealTimeResultColumnDefinition",under = ResultDataSet_2, \
    ColumnClassName="RxStreamSummaryResults", \
    ColumnPropertyName="FcsErrorFrameRate", \
    ColumnDescription="", \
    ColumnWidth="141", \
    ColumnUnits="17", \
    ColumnPrecision="2", \
    ColumnSortType="NONE", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="RealTimeResultColumnDefinition 155")

    RealTimeResultColumnDefinition_195 = stc.create("RealTimeResultColumnDefinition",under = ResultDataSet_2, \
    ColumnClassName="RxStreamSummaryResults", \
    ColumnPropertyName="PrbsErrorFrameCount", \
    ColumnDescription="", \
    ColumnWidth="0", \
    ColumnUnits="16", \
    ColumnPrecision="2", \
    ColumnSortType="NONE", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="RealTimeResultColumnDefinition 156")

    RealTimeResultColumnDefinition_196 = stc.create("RealTimeResultColumnDefinition",under = ResultDataSet_2, \
    ColumnClassName="RxStreamSummaryResults", \
    ColumnPropertyName="PrbsErrorFrameRate", \
    ColumnDescription="", \
    ColumnWidth="0", \
    ColumnUnits="17", \
    ColumnPrecision="2", \
    ColumnSortType="NONE", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="RealTimeResultColumnDefinition 157")

    RealTimeResultColumnDefinition_197 = stc.create("RealTimeResultColumnDefinition",under = ResultDataSet_2, \
    ColumnClassName="RxStreamSummaryResults", \
    ColumnPropertyName="InSeqFrameCount", \
    ColumnDescription="", \
    ColumnWidth="147", \
    ColumnUnits="16", \
    ColumnPrecision="2", \
    ColumnSortType="NONE", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="RealTimeResultColumnDefinition 158")

    RealTimeResultColumnDefinition_198 = stc.create("RealTimeResultColumnDefinition",under = ResultDataSet_2, \
    ColumnClassName="RxStreamSummaryResults", \
    ColumnPropertyName="OutSeqFrameCount", \
    ColumnDescription="", \
    ColumnWidth="170", \
    ColumnUnits="16", \
    ColumnPrecision="2", \
    ColumnSortType="NONE", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="RealTimeResultColumnDefinition 159")

    RealTimeResultColumnDefinition_199 = stc.create("RealTimeResultColumnDefinition",under = ResultDataSet_2, \
    ColumnClassName="RxStreamSummaryResults", \
    ColumnPropertyName="InSeqFrameRate", \
    ColumnDescription="", \
    ColumnWidth="140", \
    ColumnUnits="17", \
    ColumnPrecision="2", \
    ColumnSortType="NONE", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="RealTimeResultColumnDefinition 160")

    RealTimeResultColumnDefinition_200 = stc.create("RealTimeResultColumnDefinition",under = ResultDataSet_2, \
    ColumnClassName="RxStreamSummaryResults", \
    ColumnPropertyName="OutSeqFrameRate", \
    ColumnDescription="", \
    ColumnWidth="161", \
    ColumnUnits="17", \
    ColumnPrecision="2", \
    ColumnSortType="NONE", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="RealTimeResultColumnDefinition 161")

    RealTimeResultColumnDefinition_201 = stc.create("RealTimeResultColumnDefinition",under = ResultDataSet_2, \
    ColumnClassName="RxStreamSummaryResults", \
    ColumnPropertyName="DroppedFrameCount", \
    ColumnDescription="", \
    ColumnWidth="127", \
    ColumnUnits="16", \
    ColumnPrecision="2", \
    ColumnSortType="NONE", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="RealTimeResultColumnDefinition 162")

    RealTimeResultColumnDefinition_202 = stc.create("RealTimeResultColumnDefinition",under = ResultDataSet_2, \
    ColumnClassName="RxStreamSummaryResults", \
    ColumnPropertyName="DroppedFramePercent", \
    ColumnDescription="", \
    ColumnWidth="125", \
    ColumnUnits="0", \
    ColumnPrecision="2", \
    ColumnSortType="NONE", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="RealTimeResultColumnDefinition 163")

    RealTimeResultColumnDefinition_203 = stc.create("RealTimeResultColumnDefinition",under = ResultDataSet_2, \
    ColumnClassName="RxStreamSummaryResults", \
    ColumnPropertyName="InOrderFrameCount", \
    ColumnDescription="", \
    ColumnWidth="126", \
    ColumnUnits="16", \
    ColumnPrecision="2", \
    ColumnSortType="NONE", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="RealTimeResultColumnDefinition 164")

    RealTimeResultColumnDefinition_204 = stc.create("RealTimeResultColumnDefinition",under = ResultDataSet_2, \
    ColumnClassName="RxStreamSummaryResults", \
    ColumnPropertyName="ReorderedFrameCount", \
    ColumnDescription="", \
    ColumnWidth="136", \
    ColumnUnits="16", \
    ColumnPrecision="2", \
    ColumnSortType="NONE", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="RealTimeResultColumnDefinition 165")

    RealTimeResultColumnDefinition_205 = stc.create("RealTimeResultColumnDefinition",under = ResultDataSet_2, \
    ColumnClassName="RxStreamSummaryResults", \
    ColumnPropertyName="DuplicateFrameCount", \
    ColumnDescription="", \
    ColumnWidth="131", \
    ColumnUnits="16", \
    ColumnPrecision="2", \
    ColumnSortType="NONE", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="RealTimeResultColumnDefinition 166")

    RealTimeResultColumnDefinition_206 = stc.create("RealTimeResultColumnDefinition",under = ResultDataSet_2, \
    ColumnClassName="RxStreamSummaryResults", \
    ColumnPropertyName="LateFrameCount", \
    ColumnDescription="", \
    ColumnWidth="106", \
    ColumnUnits="16", \
    ColumnPrecision="2", \
    ColumnSortType="NONE", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="RealTimeResultColumnDefinition 167")

    RealTimeResultColumnDefinition_207 = stc.create("RealTimeResultColumnDefinition",under = ResultDataSet_2, \
    ColumnClassName="RxStreamSummaryResults", \
    ColumnPropertyName="DroppedFrameRate", \
    ColumnDescription="", \
    ColumnWidth="121", \
    ColumnUnits="17", \
    ColumnPrecision="2", \
    ColumnSortType="NONE", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="RealTimeResultColumnDefinition 168")

    RealTimeResultColumnDefinition_208 = stc.create("RealTimeResultColumnDefinition",under = ResultDataSet_2, \
    ColumnClassName="RxStreamSummaryResults", \
    ColumnPropertyName="DroppedFramePercentRate", \
    ColumnDescription="", \
    ColumnWidth="85", \
    ColumnUnits="0", \
    ColumnPrecision="2", \
    ColumnSortType="NONE", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="RealTimeResultColumnDefinition 169")

    RealTimeResultColumnDefinition_209 = stc.create("RealTimeResultColumnDefinition",under = ResultDataSet_2, \
    ColumnClassName="RxStreamSummaryResults", \
    ColumnPropertyName="InOrderFrameRate", \
    ColumnDescription="", \
    ColumnWidth="119", \
    ColumnUnits="17", \
    ColumnPrecision="2", \
    ColumnSortType="NONE", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="RealTimeResultColumnDefinition 170")

    RealTimeResultColumnDefinition_210 = stc.create("RealTimeResultColumnDefinition",under = ResultDataSet_2, \
    ColumnClassName="RxStreamSummaryResults", \
    ColumnPropertyName="ReorderedFrameRate", \
    ColumnDescription="", \
    ColumnWidth="130", \
    ColumnUnits="17", \
    ColumnPrecision="2", \
    ColumnSortType="NONE", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="RealTimeResultColumnDefinition 171")

    RealTimeResultColumnDefinition_211 = stc.create("RealTimeResultColumnDefinition",under = ResultDataSet_2, \
    ColumnClassName="RxStreamSummaryResults", \
    ColumnPropertyName="DuplicateFrameRate", \
    ColumnDescription="", \
    ColumnWidth="124", \
    ColumnUnits="17", \
    ColumnPrecision="2", \
    ColumnSortType="NONE", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="RealTimeResultColumnDefinition 172")

    RealTimeResultColumnDefinition_212 = stc.create("RealTimeResultColumnDefinition",under = ResultDataSet_2, \
    ColumnClassName="RxStreamSummaryResults", \
    ColumnPropertyName="LateFrameRate", \
    ColumnDescription="", \
    ColumnWidth="99", \
    ColumnUnits="17", \
    ColumnPrecision="2", \
    ColumnSortType="NONE", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="RealTimeResultColumnDefinition 173")

    RealTimeResultColumnDefinition_213 = stc.create("RealTimeResultColumnDefinition",under = ResultDataSet_2, \
    ColumnClassName="RxStreamSummaryResults", \
    ColumnPropertyName="HistBin1Count", \
    ColumnDescription="", \
    ColumnWidth="70", \
    ColumnUnits="0", \
    ColumnPrecision="2", \
    ColumnSortType="NONE", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="RealTimeResultColumnDefinition 174")

    RealTimeResultColumnDefinition_214 = stc.create("RealTimeResultColumnDefinition",under = ResultDataSet_2, \
    ColumnClassName="RxStreamSummaryResults", \
    ColumnPropertyName="HistBin2Count", \
    ColumnDescription="", \
    ColumnWidth="70", \
    ColumnUnits="0", \
    ColumnPrecision="2", \
    ColumnSortType="NONE", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="RealTimeResultColumnDefinition 175")

    RealTimeResultColumnDefinition_215 = stc.create("RealTimeResultColumnDefinition",under = ResultDataSet_2, \
    ColumnClassName="RxStreamSummaryResults", \
    ColumnPropertyName="HistBin3Count", \
    ColumnDescription="", \
    ColumnWidth="70", \
    ColumnUnits="0", \
    ColumnPrecision="2", \
    ColumnSortType="NONE", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="RealTimeResultColumnDefinition 176")

    RealTimeResultGroupDefinition_13 = stc.create("RealTimeResultGroupDefinition",under = ResultDataSet_2, \
    GroupName="Errors", \
    GroupId="object://customgroup/1334ba8f-a144-4069-8cb7-11633334149f/Errors", \
    ColumnClassName="Port RxStreamSummaryResults TxStreamResults RxStreamSummaryResults RxStreamSummaryResults RxStreamSummaryResults RxStreamSummaryResults RxStreamSummaryResults RxStreamSummaryResults RxStreamSummaryResults RxStreamSummaryResults RxStreamSummaryResults RxStreamSummaryResults RxStreamSummaryResults RxStreamSummaryResults RxStreamSummaryResults RxStreamSummaryResults", \
    ColumnPropertyName="Name PortUiName FrameCount FrameCount Ipv4ChecksumErrorCount TcpUdpChecksumErrorCount PrbsBitErrorCount PrbsFillOctetCount PrbsBitErrorRatio FcsErrorFrameCount Ipv4ChecksumErrorRate TcpUdpChecksumErrorRate PrbsBitErrorRate PrbsFillOctetRate FcsErrorFrameRate PrbsErrorFrameCount PrbsErrorFrameRate", \
    CountQuery="select count(*) from (select TxStreamId from TxRxEotStreamResults group by DataSetId, TxStreamId)", \
    SqlString="select TxPortName as 'Tx Port', group_concat(distinct ActualRxPortName) as 'Rx Port', TxStreamBlockName as 'Stream Block', TxStreamId as 'Stream Id', TxStreamIndex as 'Stream Index', TxFrameCount as 'Tx Count (Frames)',  coalesce(sum(FrameCount), 0) as 'Rx Count (Frames)', coalesce(sum(Ipv4ChecksumErrorCount), 0) as 'Rx IPv4 Checksum Error Count', coalesce(sum(TcpUdpChecksumErrorCount), 0) as 'Rx TCP/UDP Checksum Error Count', coalesce(sum(PrbsBitErrorCount), 0) as 'PRBS Bit Error Count', coalesce(sum(PrbsFillOctetCount), 0) as 'PRBS Fill Octet Count', coalesce(round(cast(sum(PrbsBitErrorCount) as double)/(sum(PrbsFillOctetCount)*8), 3), 0.0) as 'PRBS Bit Error Ratio', coalesce(sum(FcsErrorFrameCount), 0) as 'Rx FCS Error Count (Frames)', coalesce(sum(PrbsErrorFrameCount), 0) as 'PRBS Error Frame Count' from TxRxEotStreamResults where isExpectedPort=1 group by DataSetId, TxStreamId", \
    UseCustomSqlString="TRUE", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="RealTimeResultGroupDefinition 13")

    RealTimeResultGroupDefinition_14 = stc.create("RealTimeResultGroupDefinition",under = ResultDataSet_2, \
    GroupName="Basic Sequencing", \
    GroupId="object://customgroup/e652f0ae-e04e-4f5b-922e-f6a0a21e9347/Basic Sequencing", \
    ColumnClassName="Port RxStreamSummaryResults TxStreamResults RxStreamSummaryResults RxStreamSummaryResults RxStreamSummaryResults RxStreamSummaryResults RxStreamSummaryResults", \
    ColumnPropertyName="Name PortUiName FrameCount FrameCount InSeqFrameCount OutSeqFrameCount InSeqFrameRate OutSeqFrameRate", \
    CountQuery="select count(*) from (select TxStreamId from TxRxEotStreamResults group by DataSetId, TxStreamId)", \
    SqlString="select TxPortName as 'Tx Port', group_concat(distinct ActualRxPortName) as 'Rx Port', TxStreamBlockName as 'Stream Block', TxStreamId as 'Stream Id', TxStreamIndex as 'Stream Index', TxFrameCount as 'Tx Count (Frames)', coalesce(sum(FrameCount), 0) as 'Rx Count (Frames)', coalesce(sum(SeqRunLength), 0) as 'Sequence Run Length', coalesce(sum(InSeqFrameCount), 0) as 'In Seq Count (Frames)', coalesce(sum(OutSeqFrameCount), 0) as 'Out of Seq Count (Frames)' from TxRxEotStreamResults where isExpectedPort=1 group by DataSetId, TxStreamId", \
    UseCustomSqlString="TRUE", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="RealTimeResultGroupDefinition 14")

    RealTimeResultGroupDefinition_15 = stc.create("RealTimeResultGroupDefinition",under = ResultDataSet_2, \
    GroupName="Advanced Sequencing", \
    GroupId="object://customgroup/3d3639f4-a55b-4466-8e16-2e7c6a70afa7/Advanced Sequencing", \
    ColumnClassName="Port RxStreamSummaryResults TxStreamResults RxStreamSummaryResults RxStreamSummaryResults RxStreamSummaryResults RxStreamSummaryResults RxStreamSummaryResults RxStreamSummaryResults RxStreamSummaryResults RxStreamSummaryResults RxStreamSummaryResults RxStreamSummaryResults RxStreamSummaryResults RxStreamSummaryResults RxStreamSummaryResults", \
    ColumnPropertyName="Name PortUiName FrameCount FrameCount DroppedFrameCount DroppedFramePercent InOrderFrameCount ReorderedFrameCount DuplicateFrameCount LateFrameCount DroppedFrameRate DroppedFramePercentRate InOrderFrameRate ReorderedFrameRate DuplicateFrameRate LateFrameRate", \
    CountQuery="select count(*) from (select TxStreamId from TxRxEotStreamResults group by DataSetId, TxStreamId)", \
    SqlString="select TxPortName as 'Tx Port', group_concat(distinct ActualRxPortName) as 'Rx Port', TxStreamBlockName as 'Stream Block', TxStreamId as  'Stream Id', TxStreamIndex as 'Stream Index', TxFrameCount as 'Tx Count (Frames)', coalesce(sum(FrameCount), 0) as 'Rx Count (Frames)', ExpectedRxFrameCount as 'Expected Rx Count (Frames)', (case when (ExpectedRxFrameCount - coalesce(sum(FrameCount), 0)) < 0 then '' else ExpectedRxFrameCount - coalesce(sum(FrameCount),0) end) as 'Tx-Rx (Frames)', (case when (ExpectedRxFrameCount - coalesce(sum(FrameCount), 0)) < 0 then '' else round(cast(ExpectedRxFrameCount - coalesce(sum(FrameCount), 0) as double) * 100.0 / ExpectedRxFrameCount, 5) end) as 'Tx-Rx (%)', coalesce(sum(DroppedFrameCount), 0) as 'Dropped Frame Count', round(cast(coalesce(sum(DroppedFrameCount), 0) as double) * 100.0 / ExpectedRxFrameCount, 5) as 'Dropped Frame (%)', coalesce(sum(InOrderFrameCount), 0) as 'In-order Frame Count', coalesce(sum(ReorderedFrameCount), 0) as 'Reordered Frame Count', coalesce(sum(DuplicateFrameCount), 0) as 'Duplicate Count (Frames)', coalesce(sum(LateFrameCount), 0) as 'Late Count (Frames)' from TxRxEotStreamResults where isExpectedPort=1 group by DataSetId, TxStreamId", \
    UseCustomSqlString="TRUE", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="RealTimeResultGroupDefinition 15")

    RealTimeResultGroupDefinition_16 = stc.create("RealTimeResultGroupDefinition",under = ResultDataSet_2, \
    GroupName="Histograms", \
    GroupId="object://customgroup/a3fa4141-b6c7-4c1b-935b-df51d6118259/Histograms", \
    ColumnClassName="Port RxStreamSummaryResults TxStreamResults RxStreamSummaryResults RxStreamSummaryResults RxStreamSummaryResults RxStreamSummaryResults RxStreamSummaryResults RxStreamSummaryResults RxStreamSummaryResults RxStreamSummaryResults RxStreamSummaryResults RxStreamSummaryResults RxStreamSummaryResults RxStreamSummaryResults RxStreamSummaryResults RxStreamSummaryResults RxStreamSummaryResults RxStreamSummaryResults RxStreamSummaryResults", \
    ColumnPropertyName="Name PortUiName FrameCount FrameCount HistBin1Count HistBin2Count HistBin3Count HistBin4Count HistBin5Count HistBin6Count HistBin7Count HistBin8Count HistBin9Count HistBin10Count HistBin11Count HistBin12Count HistBin13Count HistBin14Count HistBin15Count HistBin16Count", \
    CountQuery="select count(*) from (select TxStreamId from TxRxEotStreamResults group by DataSetId, TxStreamId)", \
    SqlString="select TxPortName as 'Tx Port', group_concat(distinct ActualRxPortName) as 'Rx Port', TxStreamBlockName as 'Stream Block', TxStreamId as 'Stream Id', TxStreamIndex as 'Stream Index', TxFrameCount as 'Tx Count (Frames)', coalesce(sum(FrameCount), 0) as 'Rx Count (Frames)', coalesce(sum(HistBin1Count), 0) as 'Bucket 1', coalesce(sum(HistBin2Count), 0) as 'Bucket 2', coalesce(sum(HistBin3Count), 0) as 'Bucket 3', coalesce(sum(HistBin4Count), 0) as 'Bucket 4', coalesce(sum(HistBin5Count), 0) as 'Bucket 5', coalesce(sum(HistBin6Count), 0) as 'Bucket 6', coalesce(sum(HistBin7Count), 0) as 'Bucket 7', coalesce(sum(HistBin8Count), 0) as 'Bucket 8', coalesce(sum(HistBin9Count), 0) as 'Bucket 9', coalesce(sum(HistBin10Count), 0) as 'Bucket 10', coalesce(sum(HistBin11Count), 0) as 'Bucket 11', coalesce(sum(HistBin12Count), 0) as 'Bucket 12', coalesce(sum(HistBin13Count), 0) as 'Bucket 13', coalesce(sum(HistBin14Count), 0) as 'Bucket 14', coalesce(sum(HistBin15Count), 0) as 'Bucket 15', coalesce(sum(HistBin16Count), 0) as 'Bucket 16' from TxRxEotStreamResults where isExpectedPort=1 group by DataSetId, TxStreamId", \
    UseCustomSqlString="TRUE", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="RealTimeResultGroupDefinition 16")

    RealTimeResultColumnDefinition_216 = stc.create("RealTimeResultColumnDefinition",under = ResultDataSet_2, \
    ColumnClassName="RxStreamSummaryResults", \
    ColumnPropertyName="HistBin4Count", \
    ColumnDescription="", \
    ColumnWidth="70", \
    ColumnUnits="0", \
    ColumnPrecision="2", \
    ColumnSortType="NONE", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="RealTimeResultColumnDefinition 177")

    RealTimeResultColumnDefinition_217 = stc.create("RealTimeResultColumnDefinition",under = ResultDataSet_2, \
    ColumnClassName="RxStreamSummaryResults", \
    ColumnPropertyName="HistBin5Count", \
    ColumnDescription="", \
    ColumnWidth="70", \
    ColumnUnits="0", \
    ColumnPrecision="2", \
    ColumnSortType="NONE", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="RealTimeResultColumnDefinition 178")

    RealTimeResultColumnDefinition_218 = stc.create("RealTimeResultColumnDefinition",under = ResultDataSet_2, \
    ColumnClassName="RxStreamSummaryResults", \
    ColumnPropertyName="HistBin6Count", \
    ColumnDescription="", \
    ColumnWidth="70", \
    ColumnUnits="0", \
    ColumnPrecision="2", \
    ColumnSortType="NONE", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="RealTimeResultColumnDefinition 179")

    RealTimeResultColumnDefinition_219 = stc.create("RealTimeResultColumnDefinition",under = ResultDataSet_2, \
    ColumnClassName="RxStreamSummaryResults", \
    ColumnPropertyName="HistBin7Count", \
    ColumnDescription="", \
    ColumnWidth="70", \
    ColumnUnits="0", \
    ColumnPrecision="2", \
    ColumnSortType="NONE", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="RealTimeResultColumnDefinition 180")

    RealTimeResultColumnDefinition_220 = stc.create("RealTimeResultColumnDefinition",under = ResultDataSet_2, \
    ColumnClassName="RxStreamSummaryResults", \
    ColumnPropertyName="HistBin8Count", \
    ColumnDescription="", \
    ColumnWidth="70", \
    ColumnUnits="0", \
    ColumnPrecision="2", \
    ColumnSortType="NONE", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="RealTimeResultColumnDefinition 181")

    RealTimeResultColumnDefinition_221 = stc.create("RealTimeResultColumnDefinition",under = ResultDataSet_2, \
    ColumnClassName="RxStreamSummaryResults", \
    ColumnPropertyName="HistBin9Count", \
    ColumnDescription="", \
    ColumnWidth="70", \
    ColumnUnits="0", \
    ColumnPrecision="2", \
    ColumnSortType="NONE", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="RealTimeResultColumnDefinition 182")

    RealTimeResultColumnDefinition_222 = stc.create("RealTimeResultColumnDefinition",under = ResultDataSet_2, \
    ColumnClassName="RxStreamSummaryResults", \
    ColumnPropertyName="HistBin10Count", \
    ColumnDescription="", \
    ColumnWidth="70", \
    ColumnUnits="0", \
    ColumnPrecision="2", \
    ColumnSortType="NONE", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="RealTimeResultColumnDefinition 183")

    RealTimeResultColumnDefinition_223 = stc.create("RealTimeResultColumnDefinition",under = ResultDataSet_2, \
    ColumnClassName="RxStreamSummaryResults", \
    ColumnPropertyName="HistBin11Count", \
    ColumnDescription="", \
    ColumnWidth="70", \
    ColumnUnits="0", \
    ColumnPrecision="2", \
    ColumnSortType="NONE", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="RealTimeResultColumnDefinition 184")

    RealTimeResultColumnDefinition_224 = stc.create("RealTimeResultColumnDefinition",under = ResultDataSet_2, \
    ColumnClassName="RxStreamSummaryResults", \
    ColumnPropertyName="HistBin12Count", \
    ColumnDescription="", \
    ColumnWidth="70", \
    ColumnUnits="0", \
    ColumnPrecision="2", \
    ColumnSortType="NONE", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="RealTimeResultColumnDefinition 184")

    RealTimeResultColumnDefinition_225 = stc.create("RealTimeResultColumnDefinition",under = ResultDataSet_2, \
    ColumnClassName="RxStreamSummaryResults", \
    ColumnPropertyName="HistBin13Count", \
    ColumnDescription="", \
    ColumnWidth="70", \
    ColumnUnits="0", \
    ColumnPrecision="2", \
    ColumnSortType="NONE", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="RealTimeResultColumnDefinition 185")

    RealTimeResultColumnDefinition_226 = stc.create("RealTimeResultColumnDefinition",under = ResultDataSet_2, \
    ColumnClassName="RxStreamSummaryResults", \
    ColumnPropertyName="HistBin14Count", \
    ColumnDescription="", \
    ColumnWidth="70", \
    ColumnUnits="0", \
    ColumnPrecision="2", \
    ColumnSortType="NONE", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="RealTimeResultColumnDefinition 186")

    RealTimeResultColumnDefinition_227 = stc.create("RealTimeResultColumnDefinition",under = ResultDataSet_2, \
    ColumnClassName="RxStreamSummaryResults", \
    ColumnPropertyName="HistBin15Count", \
    ColumnDescription="", \
    ColumnWidth="70", \
    ColumnUnits="0", \
    ColumnPrecision="2", \
    ColumnSortType="NONE", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="RealTimeResultColumnDefinition 378")

    RealTimeResultColumnDefinition_228 = stc.create("RealTimeResultColumnDefinition",under = ResultDataSet_2, \
    ColumnClassName="RxStreamSummaryResults", \
    ColumnPropertyName="HistBin16Count", \
    ColumnDescription="", \
    ColumnWidth="70", \
    ColumnUnits="0", \
    ColumnPrecision="2", \
    ColumnSortType="NONE", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="RealTimeResultColumnDefinition 379")

    RxPortResultFilter_1 = stc.create("RxPortResultFilter",under = Project_1, \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="RxPortResultFilter 1")

    AutomationOptions_1 = (stc.get( system1, 'children-AutomationOptions' )).split(' ')[0]
    stc.config(AutomationOptions_1, \
    CommandTimeout="3600", \
    LogLevel="WARN", \
    LogTo="stdout", \
    MaxBackup="0", \
    MaxFileSizeInMB="10", \
    SuppressTclErrors="FALSE", \
    AutoSubscribe="FALSE", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="AutomationOptions 1")

    PhysicalChassisManager_1 = stc.create("PhysicalChassisManager",under = system1, \
    RawImageArchiveDir="", \
    FirmwareArchiveDir="", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="PhysicalChassisManager 1")

    Sequencer_1 = stc.create("Sequencer",under = system1, \
    CurrentSubCommandName="", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="Sequencer 1")

    IfManager_1 = stc.create("IfManager",under = system1, \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="IfManager 1")

    LinkRegistry_1 = stc.create("LinkRegistry",under = system1, \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="LinkRegistry 1")

    FeatureSupportedVersion_1 = (stc.get( system1, 'children-FeatureSupportedVersion' )).split(' ')[0]
    stc.config(FeatureSupportedVersion_1, \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="FeatureSupportedVersion 1")

    ActiveEventManager_1 = (stc.get( system1, 'children-ActiveEventManager' )).split(' ')[0]
    stc.config(ActiveEventManager_1, \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="ActiveEventManager 1")

    SequencerGroupCommand_1 = stc.create("SequencerGroupCommand",under = system1, \
    ExecutionMode="BACKGROUND", \
    GroupCategory="CLEANUP_COMMAND", \
    AutoDestroy="FALSE", \
    ExecuteSynchronous="FALSE", \
    ProgressEnable="TRUE", \
    ProgressIsSafeCancel="TRUE", \
    Active="TRUE", \
    LocalActive="TRUE", \
    Name="Cleanup Commands")

# Set up relationships
    stc.config(Project_1,**{"DefaultSelection-targets" : [FrameLengthDistribution_1,CustomFillPattern_1]})
    stc.config(Port_1,**{"AffiliationPort-sources" : [EmulatedDevice_1]})
    stc.config(Port_1,**{"ActivePhy-targets" : [EthernetCopper_2]})
    stc.config(Port_2,**{"AffiliationPort-sources" : [EmulatedDevice_2]})
    stc.config(Port_2,**{"ActivePhy-targets" : [EthernetCopper_4]})
    stc.config(Tags_1,**{"DefaultTag-targets" : [Tag_1,Tag_2,Tag_3,Tag_4,Tag_5,Tag_6]})
    stc.config(PerspectiveNode_1,**{"PerspectiveChild-targets" : [ResultDataSet_1,DynamicResultView_1]})
    stc.config(PerspectiveNode_2,**{"PerspectiveChild-targets" : [ResultDataSet_1,DynamicResultView_1]})
    stc.config(Host_1,**{"TopLevelIf-targets" : [Ipv4If_1,Ipv6If_1,Ipv6If_2]})
    stc.config(Ipv4If_1,**{"StackedOnEndpoint-targets" : [EthIIIf_1]})
    stc.config(Ipv6If_1,**{"StackedOnEndpoint-targets" : [EthIIIf_1]})
    stc.config(Ipv6If_2,**{"StackedOnEndpoint-targets" : [EthIIIf_1]})
    stc.config(AnalyzerConfig_1,**{"ActiveHistogram-targets" : [LatencyHistogram_1]})
    stc.config(StreamBlock_1,**{"SrcBinding-targets" : [Ipv4If_3]})
    stc.config(StreamBlock_1,**{"DstBinding-targets" : [Ipv4If_4]})
    stc.config(StreamBlock_1,**{"AffiliationFrameLengthDistribution-targets" : [FrameLengthDistribution_1]})
    stc.config(StreamBlock_1,**{"AffiliationStreamBlockLoadProfile-targets" : [StreamBlockLoadProfile_1]})
    stc.config(Host_2,**{"TopLevelIf-targets" : [Ipv4If_2,Ipv6If_3,Ipv6If_4]})
    stc.config(Ipv4If_2,**{"StackedOnEndpoint-targets" : [EthIIIf_2]})
    stc.config(Ipv6If_3,**{"StackedOnEndpoint-targets" : [EthIIIf_2]})
    stc.config(Ipv6If_4,**{"StackedOnEndpoint-targets" : [EthIIIf_2]})
    stc.config(AnalyzerConfig_2,**{"ActiveHistogram-targets" : [LatencyHistogram_2]})
    stc.config(StreamBlock_2,**{"SrcBinding-targets" : [Ipv4If_4]})
    stc.config(StreamBlock_2,**{"DstBinding-targets" : [Ipv4If_3]})
    stc.config(StreamBlock_2,**{"AffiliationFrameLengthDistribution-targets" : [FrameLengthDistribution_1]})
    stc.config(StreamBlock_2,**{"AffiliationStreamBlockLoadProfile-targets" : [StreamBlockLoadProfile_2]})
    stc.config(EmulatedDevice_1,**{"TopLevelIf-targets" : [Ipv4If_3]})
    stc.config(EmulatedDevice_1,**{"PrimaryIf-targets" : [Ipv4If_3]})
    stc.config(Ipv4If_3,**{"StackedOnEndpoint-targets" : [VlanIf_1]})
    stc.config(VlanIf_1,**{"StackedOnEndpoint-targets" : [EthIIIf_3]})
    stc.config(EmulatedDeviceGenParams_1,**{"SelectedPort-targets" : [Port_2]})
    stc.config(EmulatedDeviceGenParams_1,**{"DeviceGenTopLevelIf-targets" : [DeviceGenIpv4IfParams_1]})
    stc.config(DeviceGenIpv4IfParams_1,**{"DeviceGenStackedOnIf-targets" : [DeviceGenEthIIIfParams_1]})
    stc.config(EmulatedDevice_2,**{"TopLevelIf-targets" : [Ipv4If_4]})
    stc.config(EmulatedDevice_2,**{"PrimaryIf-targets" : [Ipv4If_4]})
    stc.config(Ipv4If_4,**{"StackedOnEndpoint-targets" : [VlanIf_2]})
    stc.config(VlanIf_2,**{"StackedOnEndpoint-targets" : [EthIIIf_4]})
    stc.config(ResultQuery_3,**{"ResultFilters-targets" : [RxPortResultFilter_1]})
    stc.config(Sequencer_1,**{"SequencerFinalizeType-targets" : [SequencerGroupCommand_1]})

# Set up handles
    stc.config(SequencerGroupCommand_1,CommandList="")
    stc.config(Sequencer_1,CommandList="")
    stc.config(Sequencer_1,BreakpointList="")
    stc.config(Sequencer_1,DisabledCommandList="")
    stc.config(Sequencer_1,CleanupCommand=SequencerGroupCommand_1)
    stc.config(RxPortResultFilter_1,RxPortList="")
    stc.config(PresentationResultQuery_1,FromObjects=Project_1)
    stc.config(PresentationResultQuery_2,FromObjects=Project_1)
    stc.config(ResultQuery_1,ResultRootList=Project_1)
    stc.config(ResultQuery_1,PropertyHandleArray="")
    stc.config(ResultQuery_2,ResultRootList=Project_1)
    stc.config(ResultQuery_2,PropertyHandleArray="")
    stc.config(ResultQuery_4,ResultRootList=Project_1)
    stc.config(ResultQuery_4,PropertyHandleArray="")
    stc.config(ResultQuery_3,ResultRootList=Project_1)
    stc.config(ResultQuery_3,PropertyHandleArray="")

    stc.config('system1',IsLoadingFromConfiguration='false')

    if len(portLocations) > 0:
        cmdResult = stc.perform('GetObjects', ClassName='Port', Condition='IsVirtual=false')
        ports = cmdResult['ObjectList'].split()
        idx = 0
        for port in ports:
            stc.config(port, location=portLocations[idx])
            idx+=1

    stc.config('project1.testResultSetting', saveResultsRelativeTo='NONE', resultsDirectory=resultsDir)
    stc.config('system1.sequencer', errorHandler='STOP_ON_ERROR')

#    connect - perform the logical to physical port mapping, connect to the 
#              chassis' and reserve the ports. This routine performs the connect,
#              reserve, and logical to physical port mappings directly.
#              The port list is retrieved from the in-memory configuration.
def connect():
    stc.perform('attachPorts')

#    apply - apply writes the logical information held in memory on the 
#            workstation to the ports in the STC chassis'.
def apply():
    stc.apply()

#    run - subscribe to any results views located in the in-memory configuration
#          and execute the sequencer and return the test status from the 
#          command sequence, if any. Test status is set by the Stopped Reason
#          in the Stop Command Sequence command. This is a string value and 
#          can be anything. If there is no sequence defined or no Stop 
#          Command Sequence command is executed, then the test state is 
#          returned. Test state can take the values: NONE, PASSED or FAILED.
def run():
    # Subscribe to results for result query STC_Traffic-0001-generatorportresults
    stc.subscribe(parent='project1',
                  resultParent='project1',
                  configType='generator',
                  resultType='generatorportresults',
                  filterList='',
                  viewAttributeList='totalframecount generatorframecount generatorsigframecount generatorundersizeframecount generatoroversizeframecount generatorjumboframecount totalframerate generatorframerate generatoroctetrate generatorsigframerate generatorundersizeframerate generatoroversizeframerate generatorjumboframerate generatorcrcerrorframecount generatorl3checksumerrorcount generatorl4checksumerrorcount generatorcrcerrorframerate generatorl3checksumerrorrate generatorl4checksumerrorrate totalipv4framecount totalipv6framecount totalmplsframecount generatoripv4framecount generatoripv6framecount generatorvlanframecount generatormplsframecount totalipv4framerate totalipv6framerate totalmplsframerate generatoripv4framerate generatoripv6framerate generatorvlanframerate generatormplsframerate totalbitrate generatorbitrate l1bitcount l1bitrate pfcframecount pfcpri0framecount pfcpri1framecount pfcpri2framecount pfcpri3framecount pfcpri4framecount pfcpri5framecount pfcpri6framecount pfcpri7framecount l1bitratepercent totalbitcount ',
                  interval='1', filenamePrefix='STC_Traffic-0001-generatorportresults')

    # Subscribe to results for result query STC_Traffic-0002-analyzerportresults
    stc.subscribe(parent='project1',
                  resultParent='project1',
                  configType='analyzer',
                  resultType='analyzerportresults',
                  filterList='',
                  viewAttributeList='totalframecount sigframecount undersizeframecount oversizeframecount jumboframecount pauseframecount totalframerate sigframerate undersizeframerate oversizeframerate jumboframerate pauseframerate fcserrorframecount ipv4checksumerrorcount tcpchecksumerrorcount udpchecksumerrorcount prbsfilloctetcount prbsbiterrorcount fcserrorframerate ipv4checksumerrorrate tcpchecksumerrorrate udpchecksumerrorrate prbsbiterrorrate ipv4framecount ipv6framecount tcpframecount udpframecount mplsframecount icmpframecount vlanframecount ipv4framerate ipv6framerate tcpframerate udpframerate mplsframerate icmpframerate vlanframerate trigger1count trigger1rate trigger2count trigger2rate trigger3count trigger3rate trigger4count trigger4rate trigger5count trigger5rate trigger6count trigger6rate trigger7count trigger7rate trigger8count trigger8rate combotriggercount combotriggerrate totalbitrate prbsbiterrorratio vlanframerate l1bitcount l1bitrate pfcframecount fcoeframecount pfcframerate fcoeframerate pfcpri0framecount pfcpri1framecount pfcpri2framecount pfcpri3framecount pfcpri4framecount pfcpri5framecount pfcpri6framecount pfcpri7framecount prbserrorframecount prbserrorframerate userdefinedframecount1 userdefinedframerate1 userdefinedframecount2 userdefinedframerate2 userdefinedframecount3 userdefinedframerate3 userdefinedframecount4 userdefinedframerate4 userdefinedframecount5 userdefinedframerate5 userdefinedframecount6 userdefinedframerate6 l1bitratepercent outseqframecount droppedframecount inorderframecount reorderedframecount duplicateframecount lateframecount correctedrsfecerrorcount uncorrectedrsfecerrorcount correctedbaserfecerrorcount uncorrectedbaserfecerrorcount correctedrsfecsymbols prersfecserrate postrsfecserrate prebaserfecserrate postbaserfecserrate totalbitcount ',
                  interval='1', filenamePrefix='STC_Traffic-0002-analyzerportresults')

    # Subscribe to results for result query STC_Traffic-0003-rxstreamsummaryresults
    stc.subscribe(parent='project1',
                  resultParent='project1',
                  configType='streamblock',
                  resultType='rxstreamsummaryresults',
                  filterList=(stc.get( 'system1', 'children-RxPortResultFilter' )).split(' ')[0] ,
                  viewAttributeList='framecount sigframecount fcserrorframecount minlatency maxlatency droppedframecount droppedframepercent inorderframecount reorderedframecount duplicateframecount lateframecount prbsbiterrorcount prbsfilloctetcount ipv4checksumerrorcount tcpudpchecksumerrorcount framerate sigframerate fcserrorframerate droppedframerate droppedframepercentrate inorderframerate reorderedframerate duplicateframerate lateframerate prbsbiterrorrate prbsfilloctetrate ipv4checksumerrorrate tcpudpchecksumerrorrate bitrate shorttermavglatency avglatency prbsbiterrorratio l1bitcount l1bitrate prbserrorframecount prbserrorframerate aggregatedrxportcount portstrayframes bitcount shorttermavgjitter avgjitter minjitter maxjitter shorttermavginterarrivaltime avginterarrivaltime mininterarrivaltime maxinterarrivaltime inseqframecount outseqframecount inseqframerate outseqframerate histbin1count histbin2count histbin3count histbin4count histbin5count histbin6count histbin7count histbin8count histbin9count histbin10count histbin11count histbin12count histbin13count histbin14count histbin15count histbin16count ',
                  interval='1', filenamePrefix='STC_Traffic-0003-rxstreamsummaryresults')

    # Subscribe to results for result query STC_Traffic-0004-txstreamresults
    stc.subscribe(parent='project1',
                  resultParent='project1',
                  configType='streamblock',
                  resultType='txstreamresults',
                  filterList='',
                  viewAttributeList='framecount framerate bitrate expectedrxframecount l1bitcount l1bitrate streaminfo bitcount ',
                  interval='1', filenamePrefix='STC_Traffic-0004-txstreamresults')

    # Start the sequencer
    stc.perform('sequencerStart')

    # Wait for sequencer to finish
    testState = stc.waitUntilComplete()
    return testState

#    cleanup - release the ports, disconnect from the chassis' and reset 
#              the in-memory configuration.
def cleanup():
    stc.perform('chassisDisconnectAll')
    stc.perform('resetConfig')