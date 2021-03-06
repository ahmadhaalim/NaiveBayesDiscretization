from setuptools import setup

setup(
    name='NaiveBayesDiskritisasi',
    version='0.1',
    packages=['venv.Lib.site-packages.pip', 'venv.Lib.site-packages.pip._vendor',
              'venv.Lib.site-packages.pip._vendor.idna', 'venv.Lib.site-packages.pip._vendor.pep517',
              'venv.Lib.site-packages.pip._vendor.pytoml', 'venv.Lib.site-packages.pip._vendor.certifi',
              'venv.Lib.site-packages.pip._vendor.chardet', 'venv.Lib.site-packages.pip._vendor.chardet.cli',
              'venv.Lib.site-packages.pip._vendor.distlib', 'venv.Lib.site-packages.pip._vendor.distlib._backport',
              'venv.Lib.site-packages.pip._vendor.msgpack', 'venv.Lib.site-packages.pip._vendor.urllib3',
              'venv.Lib.site-packages.pip._vendor.urllib3.util', 'venv.Lib.site-packages.pip._vendor.urllib3.contrib',
              'venv.Lib.site-packages.pip._vendor.urllib3.contrib._securetransport',
              'venv.Lib.site-packages.pip._vendor.urllib3.packages',
              'venv.Lib.site-packages.pip._vendor.urllib3.packages.backports',
              'venv.Lib.site-packages.pip._vendor.urllib3.packages.ssl_match_hostname',
              'venv.Lib.site-packages.pip._vendor.colorama', 'venv.Lib.site-packages.pip._vendor.html5lib',
              'venv.Lib.site-packages.pip._vendor.html5lib._trie',
              'venv.Lib.site-packages.pip._vendor.html5lib.filters',
              'venv.Lib.site-packages.pip._vendor.html5lib.treewalkers',
              'venv.Lib.site-packages.pip._vendor.html5lib.treeadapters',
              'venv.Lib.site-packages.pip._vendor.html5lib.treebuilders', 'venv.Lib.site-packages.pip._vendor.lockfile',
              'venv.Lib.site-packages.pip._vendor.progress', 'venv.Lib.site-packages.pip._vendor.requests',
              'venv.Lib.site-packages.pip._vendor.packaging', 'venv.Lib.site-packages.pip._vendor.cachecontrol',
              'venv.Lib.site-packages.pip._vendor.cachecontrol.caches',
              'venv.Lib.site-packages.pip._vendor.webencodings', 'venv.Lib.site-packages.pip._vendor.pkg_resources',
              'venv.Lib.site-packages.pip._internal', 'venv.Lib.site-packages.pip._internal.cli',
              'venv.Lib.site-packages.pip._internal.req', 'venv.Lib.site-packages.pip._internal.vcs',
              'venv.Lib.site-packages.pip._internal.utils', 'venv.Lib.site-packages.pip._internal.models',
              'venv.Lib.site-packages.pip._internal.commands', 'venv.Lib.site-packages.pip._internal.operations',
              'venv.Lib.site-packages.past', 'venv.Lib.site-packages.past.tests', 'venv.Lib.site-packages.past.types',
              'venv.Lib.site-packages.past.utils', 'venv.Lib.site-packages.past.builtins',
              'venv.Lib.site-packages.past.translation', 'venv.Lib.site-packages.pytz', 'venv.Lib.site-packages.numpy',
              'venv.Lib.site-packages.numpy.ma', 'venv.Lib.site-packages.numpy.ma.tests',
              'venv.Lib.site-packages.numpy.doc', 'venv.Lib.site-packages.numpy.fft',
              'venv.Lib.site-packages.numpy.fft.tests', 'venv.Lib.site-packages.numpy.lib',
              'venv.Lib.site-packages.numpy.lib.tests', 'venv.Lib.site-packages.numpy.core',
              'venv.Lib.site-packages.numpy.core.tests', 'venv.Lib.site-packages.numpy.f2py',
              'venv.Lib.site-packages.numpy.f2py.tests', 'venv.Lib.site-packages.numpy.tests',
              'venv.Lib.site-packages.numpy.compat', 'venv.Lib.site-packages.numpy.compat.tests',
              'venv.Lib.site-packages.numpy.linalg', 'venv.Lib.site-packages.numpy.linalg.tests',
              'venv.Lib.site-packages.numpy.random', 'venv.Lib.site-packages.numpy.random.tests',
              'venv.Lib.site-packages.numpy.testing', 'venv.Lib.site-packages.numpy.testing.tests',
              'venv.Lib.site-packages.numpy.testing._private', 'venv.Lib.site-packages.numpy.distutils',
              'venv.Lib.site-packages.numpy.distutils.tests', 'venv.Lib.site-packages.numpy.distutils.command',
              'venv.Lib.site-packages.numpy.distutils.fcompiler', 'venv.Lib.site-packages.numpy.matrixlib',
              'venv.Lib.site-packages.numpy.matrixlib.tests', 'venv.Lib.site-packages.numpy.polynomial',
              'venv.Lib.site-packages.numpy.polynomial.tests', 'venv.Lib.site-packages.future',
              'venv.Lib.site-packages.future.moves', 'venv.Lib.site-packages.future.moves.dbm',
              'venv.Lib.site-packages.future.moves.html', 'venv.Lib.site-packages.future.moves.http',
              'venv.Lib.site-packages.future.moves.test', 'venv.Lib.site-packages.future.moves.urllib',
              'venv.Lib.site-packages.future.moves.xmlrpc', 'venv.Lib.site-packages.future.moves.tkinter',
              'venv.Lib.site-packages.future.tests', 'venv.Lib.site-packages.future.types',
              'venv.Lib.site-packages.future.utils', 'venv.Lib.site-packages.future.builtins',
              'venv.Lib.site-packages.future.backports', 'venv.Lib.site-packages.future.backports.html',
              'venv.Lib.site-packages.future.backports.http', 'venv.Lib.site-packages.future.backports.test',
              'venv.Lib.site-packages.future.backports.email', 'venv.Lib.site-packages.future.backports.email.mime',
              'venv.Lib.site-packages.future.backports.urllib', 'venv.Lib.site-packages.future.backports.xmlrpc',
              'venv.Lib.site-packages.future.standard_library', 'venv.Lib.site-packages.pandas',
              'venv.Lib.site-packages.pandas.io', 'venv.Lib.site-packages.pandas.io.sas',
              'venv.Lib.site-packages.pandas.io.json', 'venv.Lib.site-packages.pandas.io.formats',
              'venv.Lib.site-packages.pandas.io.msgpack', 'venv.Lib.site-packages.pandas.io.clipboard',
              'venv.Lib.site-packages.pandas.api', 'venv.Lib.site-packages.pandas.api.types',
              'venv.Lib.site-packages.pandas.api.extensions', 'venv.Lib.site-packages.pandas.core',
              'venv.Lib.site-packages.pandas.core.util', 'venv.Lib.site-packages.pandas.core.tools',
              'venv.Lib.site-packages.pandas.core.arrays', 'venv.Lib.site-packages.pandas.core.dtypes',
              'venv.Lib.site-packages.pandas.core.sparse', 'venv.Lib.site-packages.pandas.core.groupby',
              'venv.Lib.site-packages.pandas.core.indexes', 'venv.Lib.site-packages.pandas.core.reshape',
              'venv.Lib.site-packages.pandas.core.internals', 'venv.Lib.site-packages.pandas.core.computation',
              'venv.Lib.site-packages.pandas.util', 'venv.Lib.site-packages.pandas._libs',
              'venv.Lib.site-packages.pandas._libs.tslibs', 'venv.Lib.site-packages.pandas.tests',
              'venv.Lib.site-packages.pandas.tests.io', 'venv.Lib.site-packages.pandas.tests.io.sas',
              'venv.Lib.site-packages.pandas.tests.io.json', 'venv.Lib.site-packages.pandas.tests.io.parser',
              'venv.Lib.site-packages.pandas.tests.io.formats', 'venv.Lib.site-packages.pandas.tests.io.msgpack',
              'venv.Lib.site-packages.pandas.tests.api', 'venv.Lib.site-packages.pandas.tests.util',
              'venv.Lib.site-packages.pandas.tests.frame', 'venv.Lib.site-packages.pandas.tests.tools',
              'venv.Lib.site-packages.pandas.tests.arrays', 'venv.Lib.site-packages.pandas.tests.arrays.sparse',
              'venv.Lib.site-packages.pandas.tests.arrays.interval',
              'venv.Lib.site-packages.pandas.tests.arrays.categorical', 'venv.Lib.site-packages.pandas.tests.dtypes',
              'venv.Lib.site-packages.pandas.tests.dtypes.cast', 'venv.Lib.site-packages.pandas.tests.scalar',
              'venv.Lib.site-packages.pandas.tests.scalar.period',
              'venv.Lib.site-packages.pandas.tests.scalar.interval',
              'venv.Lib.site-packages.pandas.tests.scalar.timedelta',
              'venv.Lib.site-packages.pandas.tests.scalar.timestamp', 'venv.Lib.site-packages.pandas.tests.series',
              'venv.Lib.site-packages.pandas.tests.series.indexing', 'venv.Lib.site-packages.pandas.tests.sparse',
              'venv.Lib.site-packages.pandas.tests.sparse.frame', 'venv.Lib.site-packages.pandas.tests.sparse.series',
              'venv.Lib.site-packages.pandas.tests.tslibs', 'venv.Lib.site-packages.pandas.tests.generic',
              'venv.Lib.site-packages.pandas.tests.groupby', 'venv.Lib.site-packages.pandas.tests.groupby.aggregate',
              'venv.Lib.site-packages.pandas.tests.indexes', 'venv.Lib.site-packages.pandas.tests.indexes.multi',
              'venv.Lib.site-packages.pandas.tests.indexes.period',
              'venv.Lib.site-packages.pandas.tests.indexes.interval',
              'venv.Lib.site-packages.pandas.tests.indexes.datetimes',
              'venv.Lib.site-packages.pandas.tests.indexes.timedeltas', 'venv.Lib.site-packages.pandas.tests.reshape',
              'venv.Lib.site-packages.pandas.tests.reshape.merge', 'venv.Lib.site-packages.pandas.tests.tseries',
              'venv.Lib.site-packages.pandas.tests.tseries.offsets', 'venv.Lib.site-packages.pandas.tests.indexing',
              'venv.Lib.site-packages.pandas.tests.indexing.interval',
              'venv.Lib.site-packages.pandas.tests.indexing.multiindex', 'venv.Lib.site-packages.pandas.tests.plotting',
              'venv.Lib.site-packages.pandas.tests.resample', 'venv.Lib.site-packages.pandas.tests.extension',
              'venv.Lib.site-packages.pandas.tests.extension.base',
              'venv.Lib.site-packages.pandas.tests.extension.json',
              'venv.Lib.site-packages.pandas.tests.extension.arrow',
              'venv.Lib.site-packages.pandas.tests.extension.numpy_',
              'venv.Lib.site-packages.pandas.tests.extension.decimal', 'venv.Lib.site-packages.pandas.tests.internals',
              'venv.Lib.site-packages.pandas.tests.arithmetic', 'venv.Lib.site-packages.pandas.tests.reductions',
              'venv.Lib.site-packages.pandas.tests.computation', 'venv.Lib.site-packages.pandas.arrays',
              'venv.Lib.site-packages.pandas.compat', 'venv.Lib.site-packages.pandas.compat.numpy',
              'venv.Lib.site-packages.pandas.errors', 'venv.Lib.site-packages.pandas.tseries',
              'venv.Lib.site-packages.pandas.plotting', 'venv.Lib.site-packages.altgraph',
              'venv.Lib.site-packages.dateutil', 'venv.Lib.site-packages.dateutil.tz',
              'venv.Lib.site-packages.dateutil.parser', 'venv.Lib.site-packages.dateutil.zoneinfo',
              'venv.Lib.site-packages.macholib', 'venv.Lib.site-packages.ordlookup',
              'venv.Lib.site-packages.libfuturize', 'venv.Lib.site-packages.libfuturize.fixes',
              'venv.Lib.site-packages.PyInstaller', 'venv.Lib.site-packages.PyInstaller.lib',
              'venv.Lib.site-packages.PyInstaller.lib.modulegraph', 'venv.Lib.site-packages.PyInstaller.hooks',
              'venv.Lib.site-packages.PyInstaller.hooks.pre_find_module_path',
              'venv.Lib.site-packages.PyInstaller.hooks.pre_safe_import_module',
              'venv.Lib.site-packages.PyInstaller.utils', 'venv.Lib.site-packages.PyInstaller.utils.hooks',
              'venv.Lib.site-packages.PyInstaller.utils.hooks.subproc',
              'venv.Lib.site-packages.PyInstaller.utils.win32', 'venv.Lib.site-packages.PyInstaller.utils.cliutils',
              'venv.Lib.site-packages.PyInstaller.depend', 'venv.Lib.site-packages.PyInstaller.loader',
              'venv.Lib.site-packages.PyInstaller.loader.rthooks', 'venv.Lib.site-packages.PyInstaller.archive',
              'venv.Lib.site-packages.PyInstaller.building', 'venv.Lib.site-packages.win32ctypes',
              'venv.Lib.site-packages.win32ctypes.core', 'venv.Lib.site-packages.win32ctypes.core.cffi',
              'venv.Lib.site-packages.win32ctypes.core.ctypes', 'venv.Lib.site-packages.win32ctypes.tests',
              'venv.Lib.site-packages.win32ctypes.pywin32', 'venv.Lib.site-packages.libpasteurize',
              'venv.Lib.site-packages.libpasteurize.fixes', 'venv.Lib.site-packages.pip-9.0.1-py3.6.egg.pip',
              'venv.Lib.site-packages.pip-9.0.1-py3.6.egg.pip.req',
              'venv.Lib.site-packages.pip-9.0.1-py3.6.egg.pip.vcs',
              'venv.Lib.site-packages.pip-9.0.1-py3.6.egg.pip.utils',
              'venv.Lib.site-packages.pip-9.0.1-py3.6.egg.pip.compat',
              'venv.Lib.site-packages.pip-9.0.1-py3.6.egg.pip.models',
              'venv.Lib.site-packages.pip-9.0.1-py3.6.egg.pip._vendor',
              'venv.Lib.site-packages.pip-9.0.1-py3.6.egg.pip._vendor.distlib',
              'venv.Lib.site-packages.pip-9.0.1-py3.6.egg.pip._vendor.distlib._backport',
              'venv.Lib.site-packages.pip-9.0.1-py3.6.egg.pip._vendor.colorama',
              'venv.Lib.site-packages.pip-9.0.1-py3.6.egg.pip._vendor.html5lib',
              'venv.Lib.site-packages.pip-9.0.1-py3.6.egg.pip._vendor.html5lib._trie',
              'venv.Lib.site-packages.pip-9.0.1-py3.6.egg.pip._vendor.html5lib.filters',
              'venv.Lib.site-packages.pip-9.0.1-py3.6.egg.pip._vendor.html5lib.treewalkers',
              'venv.Lib.site-packages.pip-9.0.1-py3.6.egg.pip._vendor.html5lib.treeadapters',
              'venv.Lib.site-packages.pip-9.0.1-py3.6.egg.pip._vendor.html5lib.treebuilders',
              'venv.Lib.site-packages.pip-9.0.1-py3.6.egg.pip._vendor.lockfile',
              'venv.Lib.site-packages.pip-9.0.1-py3.6.egg.pip._vendor.progress',
              'venv.Lib.site-packages.pip-9.0.1-py3.6.egg.pip._vendor.requests',
              'venv.Lib.site-packages.pip-9.0.1-py3.6.egg.pip._vendor.requests.packages',
              'venv.Lib.site-packages.pip-9.0.1-py3.6.egg.pip._vendor.requests.packages.chardet',
              'venv.Lib.site-packages.pip-9.0.1-py3.6.egg.pip._vendor.requests.packages.urllib3',
              'venv.Lib.site-packages.pip-9.0.1-py3.6.egg.pip._vendor.requests.packages.urllib3.util',
              'venv.Lib.site-packages.pip-9.0.1-py3.6.egg.pip._vendor.requests.packages.urllib3.contrib',
              'venv.Lib.site-packages.pip-9.0.1-py3.6.egg.pip._vendor.requests.packages.urllib3.packages',
              'venv.Lib.site-packages.pip-9.0.1-py3.6.egg.pip._vendor.requests.packages.urllib3.packages.ssl_match_hostname',
              'venv.Lib.site-packages.pip-9.0.1-py3.6.egg.pip._vendor.packaging',
              'venv.Lib.site-packages.pip-9.0.1-py3.6.egg.pip._vendor.cachecontrol',
              'venv.Lib.site-packages.pip-9.0.1-py3.6.egg.pip._vendor.cachecontrol.caches',
              'venv.Lib.site-packages.pip-9.0.1-py3.6.egg.pip._vendor.webencodings',
              'venv.Lib.site-packages.pip-9.0.1-py3.6.egg.pip._vendor.pkg_resources',
              'venv.Lib.site-packages.pip-9.0.1-py3.6.egg.pip.commands',
              'venv.Lib.site-packages.pip-9.0.1-py3.6.egg.pip.operations'],
    url='',
    license='',
    author='Halim',
    author_email='halimprabowo@gmail.com',
    description=''
)
