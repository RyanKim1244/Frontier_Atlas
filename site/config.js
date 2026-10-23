/* Frontier Atlas runtime settings. Leave supabaseUrl empty to run as a read-only static site. */
window.ATLAS_CONFIG = {
  supabaseUrl: "https://sqoonckkmsmtojmdlrrd.supabase.co",
  // The anon key is meant to be public: row-level security in supabase/migrations decides what it can do.
  // Never put the service_role key here.
  supabaseAnonKey: "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6InNxb29uY2trbXNtdG9qbWRscnJkIiwicm9sZSI6ImFub24iLCJpYXQiOjE3OTI3NDgwNDEsImV4cCI6MjEwODMyNDA0MX0.3stSOk_iwp92Vwe6w2HibHta2Sl5vIDHHtnDLIuVQUg",
  providers: ["github", "google"],   // add "kakao" once the Kakao app is set up
  contact: "",                       // contact email shown on the privacy page
  dataRegion: "",                    // the Supabase project's region, e.g. "Northeast Asia (Seoul)"
  repo: "https://github.com/RyanKim1244/Frontier_Atlas"
};
