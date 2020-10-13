import fileinput

class MSBuild (GitHubPackage):
	def __init__ (self):
		GitHubPackage.__init__ (self, 'mrward', 'msbuild', '15',  # note: fix scripts/ci/run-test-mac-sdk.sh when bumping the version number
			revision = 'a9ee92a5d968636349dd55f7008653712f25701f')

	def build (self):
		try:
			self.sh ('./eng/cibuild_bootstrapped_msbuild.sh --host_type mono --configuration Release --skip_tests')
		finally:
			self.sh ('find artifacts stage1 -wholename \'*/log/*\' -type f -exec zip msbuild-bin-logs.zip {} \+')

	def install (self):
		# use the bootstrap msbuild as the system might not have one available!
		self.sh ('./stage1/mono-msbuild/msbuild mono/build/install.proj /p:MonoInstallPrefix=%s /p:Configuration=Release-MONO /p:IgnoreDiffFailure=true' % self.staged_prefix)

MSBuild ()
