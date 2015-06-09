#!/usr/bin/env python2
##################################################
# GNU Radio Python Flow Graph
# Title: Top Block
# Generated: Sun Jun  7 00:44:44 2015
##################################################

if __name__ == '__main__':
    import ctypes
    import sys
    if sys.platform.startswith('linux'):
        try:
            x11 = ctypes.cdll.LoadLibrary('libX11.so')
            x11.XInitThreads()
        except:
            print "Warning: failed to XInitThreads()"

from gnuradio import analog
from gnuradio import audio
from gnuradio import blocks
from gnuradio import eng_notation
from gnuradio import filter
from gnuradio import gr
from gnuradio import uhd
from gnuradio import wxgui
from gnuradio.eng_option import eng_option
from gnuradio.filter import firdes
from gnuradio.wxgui import scopesink2
from grc_gnuradio import wxgui as grc_wxgui
from optparse import OptionParser
import time
import wx

class top_block(grc_wxgui.top_block_gui):

    def __init__(self):
        grc_wxgui.top_block_gui.__init__(self, title="Top Block")
        _icon_path = "/usr/share/icons/hicolor/32x32/apps/gnuradio-grc.png"
        self.SetIcon(wx.Icon(_icon_path, wx.BITMAP_TYPE_ANY))

        ##################################################
        # Variables
        ##################################################
        self.samp_rate = samp_rate = 1e6
        self.cf = cf = 915e6

        ##################################################
        # Blocks
        ##################################################
        self.wxgui_scopesink2_0 = scopesink2.scope_sink_f(
        	self.GetWin(),
        	title="Scope Plot",
        	sample_rate=samp_rate/20,
        	v_scale=0,
        	v_offset=0,
        	t_scale=0,
        	ac_couple=False,
        	xy_mode=False,
        	num_inputs=1,
        	trig_mode=wxgui.TRIG_MODE_AUTO,
        	y_axis_label="Counts",
        )
        self.Add(self.wxgui_scopesink2_0.win)
        self.uhd_usrp_source_0_0 = uhd.usrp_source(
        	",".join(("addr=192.168.10.201", "")),
        	uhd.stream_args(
        		cpu_format="fc32",
        		channels=range(1),
        	),
        )
        self.uhd_usrp_source_0_0.set_samp_rate(samp_rate)
        self.uhd_usrp_source_0_0.set_center_freq(cf, 0)
        self.uhd_usrp_source_0_0.set_gain(15, 0)
        self.uhd_usrp_source_0_0.set_antenna("RX2", 0)
        self.uhd_usrp_sink_0 = uhd.usrp_sink(
        	",".join(("addr=192.168.10.2", "")),
        	uhd.stream_args(
        		cpu_format="fc32",
        		channels=range(1),
        	),
        )
        self.uhd_usrp_sink_0.set_clock_source("mimo", 0)
        self.uhd_usrp_sink_0.set_time_source("mimo", 0)
        self.uhd_usrp_sink_0.set_samp_rate(samp_rate)
        self.uhd_usrp_sink_0.set_center_freq(cf, 0)
        self.uhd_usrp_sink_0.set_gain(0, 0)
        self.uhd_usrp_sink_0.set_antenna("TX/RX", 0)
        self.fir_filter_xxx_1 = filter.fir_filter_fff(1, ([0.00020415,0.00029146,0.00036601,0.000415,0.00042952,0.00040606,0.00034744,0.00026268,0.00016596,7.4639e-05,6.5366e-06,-2.3095e-05,-4.5044e-06,6.4269e-05,0.00017624,0.00031579,0.00046059,0.00058501,0.00066449,0.00068028,0.00062363,0.0004985,0.00032224,0.00012373,-6.0908e-05,-0.00019451,-0.00024593,-0.00019679,-4.6398e-05,0.00018614,0.00046353,0.00073554,0.00094738,0.0010499,0.0010094,0.00081629,0.00048859,7.1709e-05,-0.00036795,-0.00075378,-0.0010128,-0.0010904,-0.00096203,-0.00064154,-0.0001815,0.00033316,0.00079863,0.0011104,0.0011834,0.00096986,0.00047172,-0.00025546,-0.0011086,-0.0019531,-0.0026453,-0.0030602,-0.0031157,-0.0027926,-0.002143,-0.001286,-0.00039047,0.00035313,0.00076716,0.00072155,0.00016212,-0.00087334,-0.0022552,-0.0037795,-0.0052007,-0.0062753,-0.0068072,-0.0066889,-0.0059277,-0.0046533,-0.0031021,-0.0015809,-0.0004144,0.00011462,-0.00017882,-0.0013398,-0.0032549,-0.0056611,-0.0081843,-0.010401,-0.011912,-0.01242,-0.011795,-0.010105,-0.0076234,-0.0047933,-0.0021569,-0.00026421,0.00042915,-0.00034672,-0.0026108,-0.0061069,-0.010328,-0.014587,-0.018128,-0.02026,-0.020485,-0.018609,-0.014806,-0.0096212,-0.0039075,0.0012931,0.0049176,0.0060676,0.0041857,-0.00080843,-0.0084475,-0.017729,-0.027214,-0.035203,-0.03997,-0.040019,-0.034323,-0.022517,-0.005005,0.017036,0.04176,0.066851,0.089802,0.10822,0.12014,0.12426,0.12014,0.10822,0.089802,0.066851,0.04176,0.017036,-0.005005,-0.022517,-0.034323,-0.040019,-0.03997,-0.035203,-0.027214,-0.017729,-0.0084475,-0.00080843,0.0041857,0.0060676,0.0049176,0.0012931,-0.0039075,-0.0096212,-0.014806,-0.018609,-0.020485,-0.02026,-0.018128,-0.014587,-0.010328,-0.0061069,-0.0026108,-0.00034672,0.00042915,-0.00026421,-0.0021569,-0.0047933,-0.0076234,-0.010105,-0.011795,-0.01242,-0.011912,-0.010401,-0.0081843,-0.0056611,-0.0032549,-0.0013398,-0.00017882,0.00011462,-0.0004144,-0.0015809,-0.0031021,-0.0046533,-0.0059277,-0.0066889,-0.0068072,-0.0062753,-0.0052007,-0.0037795,-0.0022552,-0.00087334,0.00016212,0.00072155,0.00076716,0.00035313,-0.00039047,-0.001286,-0.002143,-0.0027926,-0.0031157,-0.0030602,-0.0026453,-0.0019531,-0.0011086,-0.00025546,0.00047172,0.00096986,0.0011834,0.0011104,0.00079863,0.00033316,-0.0001815,-0.00064154,-0.00096203,-0.0010904,-0.0010128,-0.00075378,-0.00036795,7.1709e-05,0.00048859,0.00081629,0.0010094,0.0010499,0.00094738,0.00073554,0.00046353,0.00018614,-4.6398e-05,-0.00019679,-0.00024593,-0.00019451,-6.0908e-05,0.00012373,0.00032224,0.0004985,0.00062363,0.00068028,0.00066449,0.00058501,0.00046059,0.00031579,0.00017624,6.4269e-05,-4.5044e-06,-2.3095e-05,6.5366e-06,7.4639e-05,0.00016596,0.00026268,0.00034744,0.00040606,0.00042952,0.000415,0.00036601,0.00029146,0.00020415]))
        self.fir_filter_xxx_1.declare_sample_delay(0)
        self.fir_filter_xxx_0_0 = filter.fir_filter_fff(1, ([0.04, 0.04, 0.04, 0.04, 0.04, 0.04, 0.04, 0.04, 0.04, 0.04, 0.04, 0.04, 0.04, 0.04, 0.04, 0.04, 0.04, 0.04, 0.04, 0.04, 0.04, 0.04, 0.04, 0.04, 0.04]))
        self.fir_filter_xxx_0_0.declare_sample_delay(0)
        self.fir_filter_xxx_0 = filter.fir_filter_ccc(20, ([-0.0002, 0.0025, 0.0112, 0.0310, 0.0625, 0.1007, 0.1357, 0.1567, 0.1567, 0.1357, 0.1007, 0.0625, 0.0310, 0.0112, 0.0025, -0.0002]))
        self.fir_filter_xxx_0.declare_sample_delay(0)
        self.blocks_wavfile_sink_0 = blocks.wavfile_sink(sys.argv[1], 1, 48000, 16)
        self.blocks_sub_xx_0 = blocks.sub_ff(1)
        self.blocks_divide_xx_0 = blocks.divide_ff(1)
        self.blocks_complex_to_mag_0 = blocks.complex_to_mag(1)
        self.audio_sink_0 = audio.sink(48000, "hw:0, 0", True)
        self.analog_const_source_x_0_0_0_0 = analog.sig_source_f(0, analog.GR_CONST_WAVE, 0, 0, 25)
        self.analog_const_source_x_0_0_0 = analog.sig_source_c(0, analog.GR_CONST_WAVE, 0, 0, 0.25)
        self.analog_agc2_xx_0 = analog.agc2_ff(10e-2, 10e-10, 1000, 1000)
        self.analog_agc2_xx_0.set_max_gain(65536)

        ##################################################
        # Connections
        ##################################################
        self.connect((self.analog_agc2_xx_0, 0), (self.blocks_divide_xx_0, 0))    
        self.connect((self.analog_const_source_x_0_0_0, 0), (self.uhd_usrp_sink_0, 0))    
        self.connect((self.analog_const_source_x_0_0_0_0, 0), (self.blocks_divide_xx_0, 1))    
        self.connect((self.blocks_complex_to_mag_0, 0), (self.blocks_sub_xx_0, 0))    
        self.connect((self.blocks_complex_to_mag_0, 0), (self.fir_filter_xxx_0_0, 0))    
        self.connect((self.blocks_divide_xx_0, 0), (self.audio_sink_0, 0))    
        self.connect((self.blocks_divide_xx_0, 0), (self.blocks_wavfile_sink_0, 0))    
        self.connect((self.blocks_sub_xx_0, 0), (self.fir_filter_xxx_1, 0))    
        self.connect((self.fir_filter_xxx_0, 0), (self.blocks_complex_to_mag_0, 0))    
        self.connect((self.fir_filter_xxx_0_0, 0), (self.blocks_sub_xx_0, 1))    
        self.connect((self.fir_filter_xxx_1, 0), (self.analog_agc2_xx_0, 0))    
        self.connect((self.fir_filter_xxx_1, 0), (self.wxgui_scopesink2_0, 0))    
        self.connect((self.uhd_usrp_source_0_0, 0), (self.fir_filter_xxx_0, 0))    


    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.wxgui_scopesink2_0.set_sample_rate(self.samp_rate/20)
        self.uhd_usrp_source_0_0.set_samp_rate(self.samp_rate)
        self.uhd_usrp_sink_0.set_samp_rate(self.samp_rate)

    def get_cf(self):
        return self.cf

    def set_cf(self, cf):
        self.cf = cf
        self.uhd_usrp_source_0_0.set_center_freq(self.cf, 0)
        self.uhd_usrp_sink_0.set_center_freq(self.cf, 0)


if __name__ == '__main__':
    parser = OptionParser(option_class=eng_option, usage="%prog: [options]")
    (options, args) = parser.parse_args()
    tb = top_block()
    tb.Start(True)
    tb.Wait()
