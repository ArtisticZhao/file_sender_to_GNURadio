#!/usr/bin/env python2
# -*- coding: utf-8 -*-
##################################################
# GNU Radio Python Flow Graph
# Title: Frontend TRX NODE1 UHD
# Generated: Thu Jul  4 10:10:57 2019
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

from PyQt4 import Qt
from gnuradio import analog
from gnuradio import blocks
from gnuradio import digital
from gnuradio import eng_notation
from gnuradio import filter
from gnuradio import gr
from gnuradio import qtgui
from gnuradio import uhd
from gnuradio.eng_option import eng_option
from gnuradio.filter import firdes
from gnuradio.qtgui import Range, RangeWidget
from optparse import OptionParser
import dslwp
import lilacsat
import math
import sip
import sys
import time
from gnuradio import qtgui


class send_data_12k(gr.top_block, Qt.QWidget):

    def __init__(self):
        gr.top_block.__init__(self, "Frontend TRX NODE1 UHD")
        Qt.QWidget.__init__(self)
        self.setWindowTitle("Frontend TRX NODE1 UHD")
        qtgui.util.check_set_qss()
        try:
            self.setWindowIcon(Qt.QIcon.fromTheme('gnuradio-grc'))
        except:
            pass
        self.top_scroll_layout = Qt.QVBoxLayout()
        self.setLayout(self.top_scroll_layout)
        self.top_scroll = Qt.QScrollArea()
        self.top_scroll.setFrameStyle(Qt.QFrame.NoFrame)
        self.top_scroll_layout.addWidget(self.top_scroll)
        self.top_scroll.setWidgetResizable(True)
        self.top_widget = Qt.QWidget()
        self.top_scroll.setWidget(self.top_widget)
        self.top_layout = Qt.QVBoxLayout(self.top_widget)
        self.top_grid_layout = Qt.QGridLayout()
        self.top_layout.addLayout(self.top_grid_layout)

        self.settings = Qt.QSettings("GNU Radio", "send_data_12k")
        self.restoreGeometry(self.settings.value("geometry").toByteArray())

        ##################################################
        # Variables
        ##################################################
        self.sps = sps = 5
        self.nfilts = nfilts = 16
        self.alpha = alpha = 0.35

        self.variable_constellation_0 = variable_constellation_0 = digital.constellation_calcdist(([-1, 1]), ([0, 1]), 2, 1).base()

        self.tx_gain = tx_gain = 15
        self.timing_loop_bw = timing_loop_bw = 0.05
        self.samp_rate = samp_rate = 250000
        self.rx_gain = rx_gain = 35
        self.rrc_taps = rrc_taps = firdes.root_raised_cosine(nfilts, nfilts, 1.0/float(sps), alpha, 11*sps*nfilts)
        self.phase_bw = phase_bw = 0.1
        self.offset = offset = 0
        self.if_rate = if_rate = 48000
        self.fll_bw = fll_bw = 0.01
        self.fc = fc = 401.6e6
        self.equalizer_gain = equalizer_gain = 0.05
        self.digigain = digigain = 20
        self.audio_rate = audio_rate = 48000

        ##################################################
        # Blocks
        ##################################################
        self.tab = Qt.QTabWidget()
        self.tab_widget_0 = Qt.QWidget()
        self.tab_layout_0 = Qt.QBoxLayout(Qt.QBoxLayout.TopToBottom, self.tab_widget_0)
        self.tab_grid_layout_0 = Qt.QGridLayout()
        self.tab_layout_0.addLayout(self.tab_grid_layout_0)
        self.tab.addTab(self.tab_widget_0, 'Waterfall')
        self.tab_widget_1 = Qt.QWidget()
        self.tab_layout_1 = Qt.QBoxLayout(Qt.QBoxLayout.TopToBottom, self.tab_widget_1)
        self.tab_grid_layout_1 = Qt.QGridLayout()
        self.tab_layout_1.addLayout(self.tab_grid_layout_1)
        self.tab.addTab(self.tab_widget_1, 'Spectrum')
        self.top_grid_layout.addWidget(self.tab, 4, 0, 1, 1)
        for r in range(4, 5):
            self.top_grid_layout.setRowStretch(r, 1)
        for c in range(0, 1):
            self.top_grid_layout.setColumnStretch(c, 1)
        self._tx_gain_range = Range(0, 89, 1, 15, 200)
        self._tx_gain_win = RangeWidget(self._tx_gain_range, self.set_tx_gain, 'TX Gain', "counter_slider", float)
        self.top_grid_layout.addWidget(self._tx_gain_win, 1, 0, 1, 1)
        for r in range(1, 2):
            self.top_grid_layout.setRowStretch(r, 1)
        for c in range(0, 1):
            self.top_grid_layout.setColumnStretch(c, 1)
        self._timing_loop_bw_range = Range(0.0, 0.2, 0.01, 0.05, 200)
        self._timing_loop_bw_win = RangeWidget(self._timing_loop_bw_range, self.set_timing_loop_bw, 'Time: Bandwidth', "counter_slider", float)
        self.tab_grid_layout_1.addWidget(self._timing_loop_bw_win, 1, 0, 1, 1)
        for r in range(1, 2):
            self.tab_grid_layout_1.setRowStretch(r, 1)
        for c in range(0, 1):
            self.tab_grid_layout_1.setColumnStretch(c, 1)
        self._rx_gain_range = Range(0, 73, 1, 35, 200)
        self._rx_gain_win = RangeWidget(self._rx_gain_range, self.set_rx_gain, 'RX Gain', "counter_slider", float)
        self.top_grid_layout.addWidget(self._rx_gain_win, 2, 0, 1, 1)
        for r in range(2, 3):
            self.top_grid_layout.setRowStretch(r, 1)
        for c in range(0, 1):
            self.top_grid_layout.setColumnStretch(c, 1)
        self._phase_bw_range = Range(0.0, 1.0, 0.01, 0.1, 200)
        self._phase_bw_win = RangeWidget(self._phase_bw_range, self.set_phase_bw, 'Phase: Bandwidth', "counter_slider", float)
        self.tab_grid_layout_1.addWidget(self._phase_bw_win, 2, 0, 1, 1)
        for r in range(2, 3):
            self.tab_grid_layout_1.setRowStretch(r, 1)
        for c in range(0, 1):
            self.tab_grid_layout_1.setColumnStretch(c, 1)
        self._offset_tool_bar = Qt.QToolBar(self)
        self._offset_tool_bar.addWidget(Qt.QLabel("offset"+": "))
        self._offset_line_edit = Qt.QLineEdit(str(self.offset))
        self._offset_tool_bar.addWidget(self._offset_line_edit)
        self._offset_line_edit.returnPressed.connect(
        	lambda: self.set_offset(int(str(self._offset_line_edit.text().toAscii()))))
        self.top_grid_layout.addWidget(self._offset_tool_bar)
        self._fll_bw_range = Range(0.0, 0.2, 0.001, 0.01, 200)
        self._fll_bw_win = RangeWidget(self._fll_bw_range, self.set_fll_bw, 'FLL: Bandwidth', "counter_slider", float)
        self.tab_grid_layout_1.addWidget(self._fll_bw_win, 0, 0, 1, 1)
        for r in range(0, 1):
            self.tab_grid_layout_1.setRowStretch(r, 1)
        for c in range(0, 1):
            self.tab_grid_layout_1.setColumnStretch(c, 1)
        self._equalizer_gain_range = Range(0.0, 0.2, 0.01, 0.05, 200)
        self._equalizer_gain_win = RangeWidget(self._equalizer_gain_range, self.set_equalizer_gain, 'Equalizer: Gain', "counter_slider", float)
        self.tab_grid_layout_1.addWidget(self._equalizer_gain_win, 3, 0, 1, 1)
        for r in range(3, 4):
            self.tab_grid_layout_1.setRowStretch(r, 1)
        for c in range(0, 1):
            self.tab_grid_layout_1.setColumnStretch(c, 1)
        self._digigain_tool_bar = Qt.QToolBar(self)
        self._digigain_tool_bar.addWidget(Qt.QLabel("digigain"+": "))
        self._digigain_line_edit = Qt.QLineEdit(str(self.digigain))
        self._digigain_tool_bar.addWidget(self._digigain_line_edit)
        self._digigain_line_edit.returnPressed.connect(
        	lambda: self.set_digigain(eng_notation.str_to_num(str(self._digigain_line_edit.text().toAscii()))))
        self.top_grid_layout.addWidget(self._digigain_tool_bar, 0, 0, 1, 1)
        for r in range(0, 1):
            self.top_grid_layout.setRowStretch(r, 1)
        for c in range(0, 1):
            self.top_grid_layout.setColumnStretch(c, 1)
        self.uhd_usrp_source_0 = uhd.usrp_source(
        	",".join(("", "")),
        	uhd.stream_args(
        		cpu_format="fc32",
        		channels=range(1),
        	),
        )
        self.uhd_usrp_source_0.set_subdev_spec('A:A', 0)
        self.uhd_usrp_source_0.set_samp_rate(samp_rate)
        self.uhd_usrp_source_0.set_center_freq(fc, 0)
        self.uhd_usrp_source_0.set_gain(rx_gain, 0)
        self.uhd_usrp_source_0.set_antenna('RX2', 0)
        self.uhd_usrp_sink_1 = uhd.usrp_sink(
        	",".join(("", "")),
        	uhd.stream_args(
        		cpu_format="fc32",
        		channels=range(1),
        	),
        )
        self.uhd_usrp_sink_1.set_subdev_spec('A:A', 0)
        self.uhd_usrp_sink_1.set_samp_rate(samp_rate)
        self.uhd_usrp_sink_1.set_center_freq(259.5e6+offset, 0)
        self.uhd_usrp_sink_1.set_gain(tx_gain, 0)
        self.rational_resampler_xxx_0_0 = filter.rational_resampler_ccc(
                interpolation=125,
                decimation=48,
                taps=None,
                fractional_bw=None,
        )
        self.rational_resampler_xxx_0 = filter.rational_resampler_ccc(
                interpolation=24,
                decimation=125,
                taps=None,
                fractional_bw=None,
        )
        self.qtgui_waterfall_sink_x_0 = qtgui.waterfall_sink_c(
        	1024, #size
        	firdes.WIN_BLACKMAN_hARRIS, #wintype
        	fc, #fc
        	samp_rate, #bw
        	"", #name
                1 #number of inputs
        )
        self.qtgui_waterfall_sink_x_0.set_update_time(0.10)
        self.qtgui_waterfall_sink_x_0.enable_grid(False)
        self.qtgui_waterfall_sink_x_0.enable_axis_labels(True)

        if not True:
          self.qtgui_waterfall_sink_x_0.disable_legend()

        if "complex" == "float" or "complex" == "msg_float":
          self.qtgui_waterfall_sink_x_0.set_plot_pos_half(not True)

        labels = ['', '', '', '', '',
                  '', '', '', '', '']
        colors = [0, 0, 0, 0, 0,
                  0, 0, 0, 0, 0]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
                  1.0, 1.0, 1.0, 1.0, 1.0]
        for i in xrange(1):
            if len(labels[i]) == 0:
                self.qtgui_waterfall_sink_x_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_waterfall_sink_x_0.set_line_label(i, labels[i])
            self.qtgui_waterfall_sink_x_0.set_color_map(i, colors[i])
            self.qtgui_waterfall_sink_x_0.set_line_alpha(i, alphas[i])

        self.qtgui_waterfall_sink_x_0.set_intensity_range(-100, 0)

        self._qtgui_waterfall_sink_x_0_win = sip.wrapinstance(self.qtgui_waterfall_sink_x_0.pyqwidget(), Qt.QWidget)
        self.tab_grid_layout_0.addWidget(self._qtgui_waterfall_sink_x_0_win)
        self.qtgui_number_sink_0 = qtgui.number_sink(
            gr.sizeof_float,
            0.001,
            qtgui.NUM_GRAPH_NONE,
            1
        )
        self.qtgui_number_sink_0.set_update_time(0.10)
        self.qtgui_number_sink_0.set_title('')

        labels = ['RSSI', '', '', '', '',
                  '', '', '', '', '']
        units = ['', '', '', '', '',
                 '', '', '', '', '']
        colors = [("black", "black"), ("black", "black"), ("black", "black"), ("black", "black"), ("black", "black"),
                  ("black", "black"), ("black", "black"), ("black", "black"), ("black", "black"), ("black", "black")]
        factor = [1, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        for i in xrange(1):
            self.qtgui_number_sink_0.set_min(i, -1)
            self.qtgui_number_sink_0.set_max(i, 1)
            self.qtgui_number_sink_0.set_color(i, colors[i][0], colors[i][1])
            if len(labels[i]) == 0:
                self.qtgui_number_sink_0.set_label(i, "Data {0}".format(i))
            else:
                self.qtgui_number_sink_0.set_label(i, labels[i])
            self.qtgui_number_sink_0.set_unit(i, units[i])
            self.qtgui_number_sink_0.set_factor(i, factor[i])

        self.qtgui_number_sink_0.enable_autoscale(False)
        self._qtgui_number_sink_0_win = sip.wrapinstance(self.qtgui_number_sink_0.pyqwidget(), Qt.QWidget)
        self.top_grid_layout.addWidget(self._qtgui_number_sink_0_win, 0, 1, 1, 1)
        for r in range(0, 1):
            self.top_grid_layout.setRowStretch(r, 1)
        for c in range(1, 2):
            self.top_grid_layout.setColumnStretch(c, 1)
        self.qtgui_freq_sink_x_0_1 = qtgui.freq_sink_c(
        	1024, #size
        	firdes.WIN_BLACKMAN_hARRIS, #wintype
        	0, #fc
        	samp_rate, #bw
        	"", #name
        	1 #number of inputs
        )
        self.qtgui_freq_sink_x_0_1.set_update_time(0.10)
        self.qtgui_freq_sink_x_0_1.set_y_axis(-140, 10)
        self.qtgui_freq_sink_x_0_1.set_y_label('Relative Gain', 'dB')
        self.qtgui_freq_sink_x_0_1.set_trigger_mode(qtgui.TRIG_MODE_FREE, 0.0, 0, "")
        self.qtgui_freq_sink_x_0_1.enable_autoscale(False)
        self.qtgui_freq_sink_x_0_1.enable_grid(False)
        self.qtgui_freq_sink_x_0_1.set_fft_average(1.0)
        self.qtgui_freq_sink_x_0_1.enable_axis_labels(True)
        self.qtgui_freq_sink_x_0_1.enable_control_panel(False)

        if not True:
          self.qtgui_freq_sink_x_0_1.disable_legend()

        if "complex" == "float" or "complex" == "msg_float":
          self.qtgui_freq_sink_x_0_1.set_plot_pos_half(not True)

        labels = ['', '', '', '', '',
                  '', '', '', '', '']
        widths = [1, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        colors = ["blue", "red", "green", "black", "cyan",
                  "magenta", "yellow", "dark red", "dark green", "dark blue"]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
                  1.0, 1.0, 1.0, 1.0, 1.0]
        for i in xrange(1):
            if len(labels[i]) == 0:
                self.qtgui_freq_sink_x_0_1.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_freq_sink_x_0_1.set_line_label(i, labels[i])
            self.qtgui_freq_sink_x_0_1.set_line_width(i, widths[i])
            self.qtgui_freq_sink_x_0_1.set_line_color(i, colors[i])
            self.qtgui_freq_sink_x_0_1.set_line_alpha(i, alphas[i])

        self._qtgui_freq_sink_x_0_1_win = sip.wrapinstance(self.qtgui_freq_sink_x_0_1.pyqwidget(), Qt.QWidget)
        self.top_grid_layout.addWidget(self._qtgui_freq_sink_x_0_1_win)
        self.qtgui_freq_sink_x_0_0 = qtgui.freq_sink_c(
        	1024, #size
        	firdes.WIN_BLACKMAN_hARRIS, #wintype
        	0, #fc
        	if_rate, #bw
        	"", #name
        	2 #number of inputs
        )
        self.qtgui_freq_sink_x_0_0.set_update_time(0.10)
        self.qtgui_freq_sink_x_0_0.set_y_axis(-100, 0)
        self.qtgui_freq_sink_x_0_0.set_y_label('Relative Gain', 'dB')
        self.qtgui_freq_sink_x_0_0.set_trigger_mode(qtgui.TRIG_MODE_FREE, 0.0, 0, "")
        self.qtgui_freq_sink_x_0_0.enable_autoscale(False)
        self.qtgui_freq_sink_x_0_0.enable_grid(False)
        self.qtgui_freq_sink_x_0_0.set_fft_average(1.0)
        self.qtgui_freq_sink_x_0_0.enable_axis_labels(True)
        self.qtgui_freq_sink_x_0_0.enable_control_panel(False)

        if not True:
          self.qtgui_freq_sink_x_0_0.disable_legend()

        if "complex" == "float" or "complex" == "msg_float":
          self.qtgui_freq_sink_x_0_0.set_plot_pos_half(not True)

        labels = ['', '', '', '', '',
                  '', '', '', '', '']
        widths = [1, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        colors = ["blue", "red", "green", "black", "cyan",
                  "magenta", "yellow", "dark red", "dark green", "dark blue"]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
                  1.0, 1.0, 1.0, 1.0, 1.0]
        for i in xrange(2):
            if len(labels[i]) == 0:
                self.qtgui_freq_sink_x_0_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_freq_sink_x_0_0.set_line_label(i, labels[i])
            self.qtgui_freq_sink_x_0_0.set_line_width(i, widths[i])
            self.qtgui_freq_sink_x_0_0.set_line_color(i, colors[i])
            self.qtgui_freq_sink_x_0_0.set_line_alpha(i, alphas[i])

        self._qtgui_freq_sink_x_0_0_win = sip.wrapinstance(self.qtgui_freq_sink_x_0_0.pyqwidget(), Qt.QWidget)
        self.tab_grid_layout_0.addWidget(self._qtgui_freq_sink_x_0_0_win)
        self.qtgui_freq_sink_x_0 = qtgui.freq_sink_c(
        	4096, #size
        	firdes.WIN_BLACKMAN_hARRIS, #wintype
        	fc, #fc
        	samp_rate, #bw
        	"", #name
        	1 #number of inputs
        )
        self.qtgui_freq_sink_x_0.set_update_time(0.10)
        self.qtgui_freq_sink_x_0.set_y_axis(-140, 10)
        self.qtgui_freq_sink_x_0.set_y_label('Relative Gain', 'dB')
        self.qtgui_freq_sink_x_0.set_trigger_mode(qtgui.TRIG_MODE_FREE, 0.0, 0, "")
        self.qtgui_freq_sink_x_0.enable_autoscale(False)
        self.qtgui_freq_sink_x_0.enable_grid(False)
        self.qtgui_freq_sink_x_0.set_fft_average(1.0)
        self.qtgui_freq_sink_x_0.enable_axis_labels(True)
        self.qtgui_freq_sink_x_0.enable_control_panel(False)

        if not True:
          self.qtgui_freq_sink_x_0.disable_legend()

        if "complex" == "float" or "complex" == "msg_float":
          self.qtgui_freq_sink_x_0.set_plot_pos_half(not True)

        labels = ['', '', '', '', '',
                  '', '', '', '', '']
        widths = [1, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        colors = ["blue", "red", "green", "black", "cyan",
                  "magenta", "yellow", "dark red", "dark green", "dark blue"]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
                  1.0, 1.0, 1.0, 1.0, 1.0]
        for i in xrange(1):
            if len(labels[i]) == 0:
                self.qtgui_freq_sink_x_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_freq_sink_x_0.set_line_label(i, labels[i])
            self.qtgui_freq_sink_x_0.set_line_width(i, widths[i])
            self.qtgui_freq_sink_x_0.set_line_color(i, colors[i])
            self.qtgui_freq_sink_x_0.set_line_alpha(i, alphas[i])

        self._qtgui_freq_sink_x_0_win = sip.wrapinstance(self.qtgui_freq_sink_x_0.pyqwidget(), Qt.QWidget)
        self.tab_grid_layout_1.addWidget(self._qtgui_freq_sink_x_0_win)
        self.qtgui_const_sink_x_0 = qtgui.const_sink_c(
        	1024, #size
        	"", #name
        	1 #number of inputs
        )
        self.qtgui_const_sink_x_0.set_update_time(0.10)
        self.qtgui_const_sink_x_0.set_y_axis(-2, 2)
        self.qtgui_const_sink_x_0.set_x_axis(-2, 2)
        self.qtgui_const_sink_x_0.set_trigger_mode(qtgui.TRIG_MODE_FREE, qtgui.TRIG_SLOPE_POS, 0.0, 0, "")
        self.qtgui_const_sink_x_0.enable_autoscale(False)
        self.qtgui_const_sink_x_0.enable_grid(False)
        self.qtgui_const_sink_x_0.enable_axis_labels(True)

        if not True:
          self.qtgui_const_sink_x_0.disable_legend()

        labels = ['A', 'B', '', '', '',
                  '', '', '', '', '']
        widths = [1, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        colors = ["blue", "red", "red", "red", "red",
                  "red", "red", "red", "red", "red"]
        styles = [0, 0, 0, 0, 0,
                  0, 0, 0, 0, 0]
        markers = [0, 0, 0, 0, 0,
                   0, 0, 0, 0, 0]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
                  1.0, 1.0, 1.0, 1.0, 1.0]
        for i in xrange(1):
            if len(labels[i]) == 0:
                self.qtgui_const_sink_x_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_const_sink_x_0.set_line_label(i, labels[i])
            self.qtgui_const_sink_x_0.set_line_width(i, widths[i])
            self.qtgui_const_sink_x_0.set_line_color(i, colors[i])
            self.qtgui_const_sink_x_0.set_line_style(i, styles[i])
            self.qtgui_const_sink_x_0.set_line_marker(i, markers[i])
            self.qtgui_const_sink_x_0.set_line_alpha(i, alphas[i])

        self._qtgui_const_sink_x_0_win = sip.wrapinstance(self.qtgui_const_sink_x_0.pyqwidget(), Qt.QWidget)
        self.top_grid_layout.addWidget(self._qtgui_const_sink_x_0_win, 3, 0, 1, 2)
        for r in range(3, 4):
            self.top_grid_layout.setRowStretch(r, 1)
        for c in range(0, 2):
            self.top_grid_layout.setColumnStretch(c, 1)
        self.low_pass_filter_0 = filter.fir_filter_ccf(1, firdes.low_pass(
        	1, if_rate, 10e3, 2e3, firdes.WIN_HAMMING, 6.76))
        self.lilacsat_vitfilt27_fb_0_0 = lilacsat.vitfilt27_fb()
        self.lilacsat_vitfilt27_fb_0 = lilacsat.vitfilt27_fb()
        self.lilacsat_two_bit_dpd_precoder_0 = lilacsat.two_bit_dpd_precoder(True)
        self.lilacsat_plan13_cc_0 = lilacsat.plan13_cc(False, '1 99999U          18116.20394676  .00036833  00000-0  16699-2 0 00008', '2 99999 097.3996 199.1566 0012704 281.9916 248.9397 15.20802792000016', 126.62741524, 45.73288422, 200, 401440000, samp_rate, False, True)
        self.lilacsat_kiss_decode_pdu_0_0 = lilacsat.kiss_decode_pdu()
        self.lilacsat_fec_decode_b_0_0_0 = lilacsat.fec_decode_b(214, True, False, False)
        self.lilacsat_fec_decode_b_0_0 = lilacsat.fec_decode_b(214, True, False, False)
        self.lilacsat_attach_rs_codeblock_0 = lilacsat.attach_rs_codeblock(1)
        self.lilacsat_attach_preamble_and_tailer_0 = lilacsat.attach_preamble_and_tailer(200, 100, True)
        self.dslwp_ccsds_pseudo_randomizer_0 = dslwp.ccsds_pseudo_randomizer(2)
        self.dslwp_attach_sync_marker_0 = dslwp.attach_sync_marker((0x1a, 0xcf, 0xfc, 0x1d), 2)
        self.digital_pfb_clock_sync_xxx_0 = digital.pfb_clock_sync_ccf(sps, timing_loop_bw, (rrc_taps), nfilts, nfilts/2, 0.05, 2)
        self.digital_lms_dd_equalizer_cc_0_0 = digital.lms_dd_equalizer_cc(2, equalizer_gain, 2, variable_constellation_0)
        self.digital_gmsk_mod_0 = digital.gmsk_mod(
        	samples_per_symbol=8,
        	bt=0.5,
        	verbose=False,
        	log=False,
        )
        self.digital_fll_band_edge_cc_0 = digital.fll_band_edge_cc(sps, alpha, 100, fll_bw)
        self.digital_costas_loop_cc_0_0 = digital.costas_loop_cc(phase_bw, 2, False)
        self.blocks_unpack_k_bits_bb_0_0_0_0 = blocks.unpack_k_bits_bb(8)
        self.blocks_unpack_k_bits_bb_0_0_0 = blocks.unpack_k_bits_bb(8)
        self.blocks_socket_pdu_1 = blocks.socket_pdu("TCP_CLIENT", 'localhost', '52001', 10000, False)
        self.blocks_rms_xx_0 = blocks.rms_cf(0.0001)
        self.blocks_pdu_to_tagged_stream_0 = blocks.pdu_to_tagged_stream(blocks.byte_t, 'packet_len')
        self.blocks_nlog10_ff_0 = blocks.nlog10_ff(20, 1, 0)
        self.blocks_multiply_xx_0 = blocks.multiply_vcc(1)
        self.blocks_multiply_const_vxx_0 = blocks.multiply_const_vcc((10**(digigain/20), ))
        self.blocks_message_debug_0_0 = blocks.message_debug()
        self.blocks_message_debug_0 = blocks.message_debug()
        self.blocks_delay_0 = blocks.delay(gr.sizeof_float*1, 1)
        self.blocks_complex_to_real_0 = blocks.complex_to_real(1)
        self.analog_sig_source_x_0 = analog.sig_source_c(samp_rate, analog.GR_COS_WAVE, 60e3, 1, 0)
        self.analog_feedforward_agc_cc_0 = analog.feedforward_agc_cc(1024, 1)

        ##################################################
        # Connections
        ##################################################
        self.msg_connect((self.blocks_socket_pdu_1, 'pdus'), (self.lilacsat_kiss_decode_pdu_0_0, 'in'))
        self.msg_connect((self.dslwp_attach_sync_marker_0, 'out'), (self.lilacsat_attach_preamble_and_tailer_0, 'in'))
        self.msg_connect((self.dslwp_ccsds_pseudo_randomizer_0, 'out'), (self.dslwp_attach_sync_marker_0, 'in'))
        self.msg_connect((self.lilacsat_attach_preamble_and_tailer_0, 'out'), (self.lilacsat_two_bit_dpd_precoder_0, 'in'))
        self.msg_connect((self.lilacsat_attach_rs_codeblock_0, 'out'), (self.dslwp_ccsds_pseudo_randomizer_0, 'in'))
        self.msg_connect((self.lilacsat_fec_decode_b_0_0, 'out'), (self.blocks_message_debug_0, 'print_pdu'))
        self.msg_connect((self.lilacsat_fec_decode_b_0_0, 'out'), (self.blocks_socket_pdu_1, 'pdus'))
        self.msg_connect((self.lilacsat_fec_decode_b_0_0_0, 'out'), (self.blocks_message_debug_0, 'print_pdu'))
        self.msg_connect((self.lilacsat_fec_decode_b_0_0_0, 'out'), (self.blocks_socket_pdu_1, 'pdus'))
        self.msg_connect((self.lilacsat_kiss_decode_pdu_0_0, 'out'), (self.blocks_message_debug_0_0, 'print_pdu'))
        self.msg_connect((self.lilacsat_kiss_decode_pdu_0_0, 'out'), (self.lilacsat_attach_rs_codeblock_0, 'in'))
        self.msg_connect((self.lilacsat_two_bit_dpd_precoder_0, 'out'), (self.blocks_pdu_to_tagged_stream_0, 'pdus'))
        self.connect((self.analog_feedforward_agc_cc_0, 0), (self.digital_fll_band_edge_cc_0, 0))
        self.connect((self.analog_sig_source_x_0, 0), (self.blocks_multiply_xx_0, 1))
        self.connect((self.blocks_complex_to_real_0, 0), (self.blocks_delay_0, 0))
        self.connect((self.blocks_complex_to_real_0, 0), (self.lilacsat_vitfilt27_fb_0, 0))
        self.connect((self.blocks_delay_0, 0), (self.lilacsat_vitfilt27_fb_0_0, 0))
        self.connect((self.blocks_multiply_const_vxx_0, 0), (self.lilacsat_plan13_cc_0, 0))
        self.connect((self.blocks_multiply_const_vxx_0, 0), (self.qtgui_freq_sink_x_0_0, 0))
        self.connect((self.blocks_multiply_xx_0, 0), (self.rational_resampler_xxx_0, 0))
        self.connect((self.blocks_nlog10_ff_0, 0), (self.qtgui_number_sink_0, 0))
        self.connect((self.blocks_pdu_to_tagged_stream_0, 0), (self.digital_gmsk_mod_0, 0))
        self.connect((self.blocks_rms_xx_0, 0), (self.blocks_nlog10_ff_0, 0))
        self.connect((self.blocks_unpack_k_bits_bb_0_0_0, 0), (self.lilacsat_fec_decode_b_0_0_0, 0))
        self.connect((self.blocks_unpack_k_bits_bb_0_0_0_0, 0), (self.lilacsat_fec_decode_b_0_0, 0))
        self.connect((self.digital_costas_loop_cc_0_0, 0), (self.digital_lms_dd_equalizer_cc_0_0, 0))
        self.connect((self.digital_fll_band_edge_cc_0, 0), (self.digital_pfb_clock_sync_xxx_0, 0))
        self.connect((self.digital_fll_band_edge_cc_0, 0), (self.qtgui_freq_sink_x_0_0, 1))
        self.connect((self.digital_gmsk_mod_0, 0), (self.rational_resampler_xxx_0_0, 0))
        self.connect((self.digital_lms_dd_equalizer_cc_0_0, 0), (self.blocks_complex_to_real_0, 0))
        self.connect((self.digital_lms_dd_equalizer_cc_0_0, 0), (self.qtgui_const_sink_x_0, 0))
        self.connect((self.digital_pfb_clock_sync_xxx_0, 0), (self.digital_costas_loop_cc_0_0, 0))
        self.connect((self.lilacsat_plan13_cc_0, 0), (self.low_pass_filter_0, 0))
        self.connect((self.lilacsat_vitfilt27_fb_0, 0), (self.blocks_unpack_k_bits_bb_0_0_0, 0))
        self.connect((self.lilacsat_vitfilt27_fb_0_0, 0), (self.blocks_unpack_k_bits_bb_0_0_0_0, 0))
        self.connect((self.low_pass_filter_0, 0), (self.analog_feedforward_agc_cc_0, 0))
        self.connect((self.low_pass_filter_0, 0), (self.blocks_rms_xx_0, 0))
        self.connect((self.rational_resampler_xxx_0, 0), (self.blocks_multiply_const_vxx_0, 0))
        self.connect((self.rational_resampler_xxx_0_0, 0), (self.qtgui_freq_sink_x_0_1, 0))
        self.connect((self.rational_resampler_xxx_0_0, 0), (self.uhd_usrp_sink_1, 0))
        self.connect((self.uhd_usrp_source_0, 0), (self.blocks_multiply_xx_0, 0))
        self.connect((self.uhd_usrp_source_0, 0), (self.qtgui_freq_sink_x_0, 0))
        self.connect((self.uhd_usrp_source_0, 0), (self.qtgui_waterfall_sink_x_0, 0))

    def closeEvent(self, event):
        self.settings = Qt.QSettings("GNU Radio", "send_data_12k")
        self.settings.setValue("geometry", self.saveGeometry())
        event.accept()

    def get_sps(self):
        return self.sps

    def set_sps(self, sps):
        self.sps = sps
        self.set_rrc_taps(firdes.root_raised_cosine(self.nfilts, self.nfilts, 1.0/float(self.sps), self.alpha, 11*self.sps*self.nfilts))

    def get_nfilts(self):
        return self.nfilts

    def set_nfilts(self, nfilts):
        self.nfilts = nfilts
        self.set_rrc_taps(firdes.root_raised_cosine(self.nfilts, self.nfilts, 1.0/float(self.sps), self.alpha, 11*self.sps*self.nfilts))

    def get_alpha(self):
        return self.alpha

    def set_alpha(self, alpha):
        self.alpha = alpha
        self.set_rrc_taps(firdes.root_raised_cosine(self.nfilts, self.nfilts, 1.0/float(self.sps), self.alpha, 11*self.sps*self.nfilts))

    def get_variable_constellation_0(self):
        return self.variable_constellation_0

    def set_variable_constellation_0(self, variable_constellation_0):
        self.variable_constellation_0 = variable_constellation_0

    def get_tx_gain(self):
        return self.tx_gain

    def set_tx_gain(self, tx_gain):
        self.tx_gain = tx_gain
        self.uhd_usrp_sink_1.set_gain(self.tx_gain, 0)


    def get_timing_loop_bw(self):
        return self.timing_loop_bw

    def set_timing_loop_bw(self, timing_loop_bw):
        self.timing_loop_bw = timing_loop_bw
        self.digital_pfb_clock_sync_xxx_0.set_loop_bandwidth(self.timing_loop_bw)

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.uhd_usrp_source_0.set_samp_rate(self.samp_rate)
        self.uhd_usrp_sink_1.set_samp_rate(self.samp_rate)
        self.qtgui_waterfall_sink_x_0.set_frequency_range(self.fc, self.samp_rate)
        self.qtgui_freq_sink_x_0_1.set_frequency_range(0, self.samp_rate)
        self.qtgui_freq_sink_x_0.set_frequency_range(self.fc, self.samp_rate)
        self.analog_sig_source_x_0.set_sampling_freq(self.samp_rate)

    def get_rx_gain(self):
        return self.rx_gain

    def set_rx_gain(self, rx_gain):
        self.rx_gain = rx_gain
        self.uhd_usrp_source_0.set_gain(self.rx_gain, 0)


    def get_rrc_taps(self):
        return self.rrc_taps

    def set_rrc_taps(self, rrc_taps):
        self.rrc_taps = rrc_taps
        self.digital_pfb_clock_sync_xxx_0.update_taps((self.rrc_taps))

    def get_phase_bw(self):
        return self.phase_bw

    def set_phase_bw(self, phase_bw):
        self.phase_bw = phase_bw
        self.digital_costas_loop_cc_0_0.set_loop_bandwidth(self.phase_bw)

    def get_offset(self):
        return self.offset

    def set_offset(self, offset):
        self.offset = offset
        Qt.QMetaObject.invokeMethod(self._offset_line_edit, "setText", Qt.Q_ARG("QString", str(self.offset)))
        self.uhd_usrp_sink_1.set_center_freq(259.5e6+self.offset, 0)

    def get_if_rate(self):
        return self.if_rate

    def set_if_rate(self, if_rate):
        self.if_rate = if_rate
        self.qtgui_freq_sink_x_0_0.set_frequency_range(0, self.if_rate)
        self.low_pass_filter_0.set_taps(firdes.low_pass(1, self.if_rate, 10e3, 2e3, firdes.WIN_HAMMING, 6.76))

    def get_fll_bw(self):
        return self.fll_bw

    def set_fll_bw(self, fll_bw):
        self.fll_bw = fll_bw
        self.digital_fll_band_edge_cc_0.set_loop_bandwidth(self.fll_bw)

    def get_fc(self):
        return self.fc

    def set_fc(self, fc):
        self.fc = fc
        self.uhd_usrp_source_0.set_center_freq(self.fc, 0)
        self.qtgui_waterfall_sink_x_0.set_frequency_range(self.fc, self.samp_rate)
        self.qtgui_freq_sink_x_0.set_frequency_range(self.fc, self.samp_rate)

    def get_equalizer_gain(self):
        return self.equalizer_gain

    def set_equalizer_gain(self, equalizer_gain):
        self.equalizer_gain = equalizer_gain
        self.digital_lms_dd_equalizer_cc_0_0.set_gain(self.equalizer_gain)

    def get_digigain(self):
        return self.digigain

    def set_digigain(self, digigain):
        self.digigain = digigain
        Qt.QMetaObject.invokeMethod(self._digigain_line_edit, "setText", Qt.Q_ARG("QString", eng_notation.num_to_str(self.digigain)))
        self.blocks_multiply_const_vxx_0.set_k((10**(self.digigain/20), ))

    def get_audio_rate(self):
        return self.audio_rate

    def set_audio_rate(self, audio_rate):
        self.audio_rate = audio_rate


def main(top_block_cls=send_data_12k, options=None):

    from distutils.version import StrictVersion
    if StrictVersion(Qt.qVersion()) >= StrictVersion("4.5.0"):
        style = gr.prefs().get_string('qtgui', 'style', 'raster')
        Qt.QApplication.setGraphicsSystem(style)
    qapp = Qt.QApplication(sys.argv)

    tb = top_block_cls()
    tb.start()
    tb.show()

    def quitting():
        tb.stop()
        tb.wait()
    qapp.connect(qapp, Qt.SIGNAL("aboutToQuit()"), quitting)
    qapp.exec_()


if __name__ == '__main__':
    main()
