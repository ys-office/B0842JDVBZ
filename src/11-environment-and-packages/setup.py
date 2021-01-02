from setuptools import setup, find_packages


setup(
    name='pythonbook',
    version='1.0.0',
    packages=find_packages(),

    # 作者、プロジェクト情報
    author='rei suyama',
    author_email='rhoboro@gmail.com',
    url='https://github.com/rhoboro/pythonbook',

    # 短い説明文と長い説明文を用意
    # content_typeは下記のいずれか
    # text/plain, text/x-rst, text/markdown
    description='This is a test package for me.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',

    # Pythonバージョンは3.6以上で4未満
    python_requires='~=3.6',

    # PyPI上での検索、閲覧のために利用される
    # ライセンス、Pythonバージョン、OSを含めること
    classifiers=[
      'License :: OSI Approved :: MIT License',
      'Programming Language :: Python :: 3',
      'Programming Language :: Python :: 3.6',
      'Programming Language :: Python :: 3.7',
      'Operating System :: OS Independent',
    ],
    install_requires = [
        # Clickのバージョンは7.0以上8未満
        'Click~=7.0',
        # sampleprojectをコミットを指定して取得
        'sampleproject@git+https://github.com/pypa/sampleproject#sha1=0754c8ab224f0886f4939cca3f4ca9e5fd5e5d90',
    ],
    extras_require = {
        's3': ['boto3'],
        'gcs': ['google-cloud-storage'],
    },
    package_data={'pythonbook': ['data/*']},
)