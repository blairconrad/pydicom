# Copyright 2020 pydicom authors. See LICENSE file for details.
# -*- coding: utf-8 -*-
"""Unit tests for the env_info module."""

import pydicom.env_info


class TestEnvInfo(object):
    """Test the env_info module"""

    def test_report_looks_like_a_table(self, capsys):
        """Test that the report looks like a table"""
        pydicom.env_info.main()

        out, err = capsys.readouterr()
        assert out.startswith(
            "module       | version\n" +
            "------       | -------\n" +
            "platform     |"
        )

    def test_all_modules_reported(self, capsys):
        """Test that all modules are reported"""
        pydicom.env_info.main()

        out, err = capsys.readouterr()
        lines = out.split("\n")
        modules = [line.split("|")[0].strip() for line in lines[2:] if line]

        assert modules == [
            "platform",
            "Python",
            "pydicom",
            "gdcm",
            "jpeg_ls",
            "numpy",
            "PIL",
        ]
