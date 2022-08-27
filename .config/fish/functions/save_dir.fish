function save_dir --on-event fish_postexec PWD
  set -U fish_most_recent_dir $PWD
end
