from odoo import models, fields, api
from datetime import date

class Siswa(models.Model):
    _name = 'addons_sekolah.siswa'
    _description = 'Data Siswa'

    nis = fields.Char(string='NIS', required=True)
    name = fields.Char(string='Nama Siswa', required=True)
    jns_kelamin = fields.Selection([('laki-laki', 'Laki-laki'), ('perempuan', 'Perempuan')], string='Jenis Kelamin')
    tgl_lahir = fields.Date(string='Tanggal Lahir')
    agama = fields.Char(string='Agama')
    nm_ayah = fields.Char(string='Nama Ayah')
    nm_ibu = fields.Char(string='Nama Ibu')
    usia = fields.Char(string='Usia', compute='_compute_usia', store=True)
    alamat = fields.Text(string='Alamat')
    kelas_id = fields.Many2one('addons_sekolah.kelas', string='Kelas')

    @api.depends('tgl_lahir')
    def _compute_usia(self):
        for record in self:
            if record.tgl_lahir:
                today = date.today()
                usia = today.year - record.tgl_lahir.year - ((today.month, today.day) < (record.tgl_lahir.month, record.tgl_lahir.day))
                record.usia = f"{usia} tahun"
            else:
                record.usia = "Belum diisi"