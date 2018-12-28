class Fluxctl < Formula
  desc "Command-line tool to access Weave Flux, the Kubernetes GitOps operator"
  homepage "https://github.com/weaveworks/flux"
  url "https://github.com/weaveworks/flux.git",
      :tag      => "1.8.1",
      :revision => "7b24d23e7ef157c87836de7af4e058da10d35298"

  bottle do
    cellar :any_skip_relocation
    sha256 "4455161fc56d5b84f4c31f5eb0a0d8bfd6603fd04cf744ea4c61016087a11706" => :mojave
    sha256 "48367b7304f1f6d7f8e8ed54a9c4da83358d005d9b62e7f70f989401f58dd029" => :high_sierra
    sha256 "0c85f2b7e5756b5c37f43fb06e89b221d0aa81008a3e7814939709a1e6d37436" => :sierra
  end

  depends_on "dep" => :build
  depends_on "go" => :build

  def install
    ENV["GOPATH"] = buildpath
    dir = buildpath/"src/github.com/weaveworks/flux"
    dir.install buildpath.children - [buildpath/".brew_home"]

    cd dir do
      system "dep", "ensure", "-vendor-only"
      system "make", "release-bins"
      bin.install "build/fluxctl_darwin_amd64" => "fluxctl"
      prefix.install_metafiles
    end
  end

  test do
    run_output = shell_output("#{bin}/fluxctl 2>&1")
    assert_match "fluxctl helps you deploy your code.", run_output

    version_output = shell_output("#{bin}/fluxctl version 2>&1")
    assert_match version.to_s, version_output

    # As we can't bring up a Kubernetes cluster in this test, we simply
    # run "fluxctl sync" and check that it 1) errors out, and 2) complains
    # about a missing .kube/config file.
    require "pty"
    require "timeout"
    r, _w, pid = PTY.spawn("#{bin}/fluxctl sync", :err=>:out)
    begin
      Timeout.timeout(5) do
        assert r.gets.chomp =~ %r{Error: stat .*\/.kube\/config: no such file or directory}
        Process.wait pid
        assert_equal 1, $CHILD_STATUS.exitstatus
      end
    rescue Timeout::Error
      puts "process not finished in time, killing it"
      Process.kill("TERM", pid)
    end
  end
end
