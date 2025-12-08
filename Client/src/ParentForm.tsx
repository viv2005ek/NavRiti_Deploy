import React, { useState } from 'react';
import { motion, AnimatePresence, useMotionValue, useTransform } from 'framer-motion';

// --- Logic Helpers ---
const normalize = (val: number) => (val - 1) / 4; 

const ParentForm = () => {
  // --- 3D Tilt Logic ---
  const x = useMotionValue(0);
  const y = useMotionValue(0);
  const rotateX = useTransform(y, [-100, 100], [5, -5]); 
  const rotateY = useTransform(x, [-100, 100], [-5, 5]);

  const handleMouseMove = (event: React.MouseEvent<HTMLDivElement>) => {
    const rect = event.currentTarget.getBoundingClientRect();
    const centerX = rect.left + rect.width / 2;
    const centerY = rect.top + rect.height / 2;
    x.set((event.clientX - centerX) / 10); 
    y.set((event.clientY - centerY) / 10);
  };

  // --- Form State ---
  const [formData, setFormData] = useState({
    financialStability: 5, jobSecurity: 5, prestige: 3,
    location: 'national', migration: 'conditional',
    maxTuition: 30000, riskTolerance: 2, influence: 'medium',
    unacceptable: '', acceptable: ''
  });

  const [result, setResult] = useState<any>(null);
  const [loading, setLoading] = useState(false);

  const handleChange = (e: React.ChangeEvent<HTMLInputElement | HTMLSelectElement>) => {
    const { name, value } = e.target;
    setFormData(prev => ({ ...prev, [name]: value }));
  };

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    setLoading(true);
    setResult(null);

    const influenceMap: Record<string, number> = { low: 0.2, medium: 0.5, high: 0.8 };
    
    // Construct Payload
    const payload = {
      parent_id: crypto.randomUUID(),
      financial_stability_weight: normalize(Number(formData.financialStability)),
      job_security_weight: normalize(Number(formData.jobSecurity)),
      prestige_weight: normalize(Number(formData.prestige)),
      location_preference: formData.location === 'abroad' ? 'international' : formData.location,
      migration_willingness: formData.migration === 'depends' ? 'conditional' : formData.migration,
      budget_constraints: { max_tuition_per_year: Number(formData.maxTuition) },
      unacceptable_professions: formData.unacceptable.split(',').map(s => s.trim()).filter(s => s),
      acceptable_professions: formData.acceptable.split(',').map(s => s.trim()).filter(s => s),
      parent_risk_tolerance: normalize(Number(formData.riskTolerance)),
      weight_on_parent_layer: influenceMap[formData.influence] || 0.2
    };

    try {
      await new Promise(r => setTimeout(r, 1500)); // Fake delay for animation
      const response = await fetch('http://localhost:8000/api/parent/preferences', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(payload)
      });
      const data = await response.json();
      setResult(data);
    } catch (error) {
      console.error("Error", error);
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="min-h-screen w-full flex items-center justify-center bg-[#050505] text-white p-4 overflow-hidden relative">
      
      {/* Background Gradients */}
      <div className="absolute top-0 left-0 w-full h-full overflow-hidden z-0">
        <div className="absolute top-[-10%] left-[-10%] w-[50%] h-[50%] bg-purple-900/20 rounded-full blur-[120px]" />
        <div className="absolute bottom-[-10%] right-[-10%] w-[50%] h-[50%] bg-cyan-900/20 rounded-full blur-[120px]" />
      </div>

      {/* Custom Styles for Neon Slider (Tailwind doesn't support slider-thumb directly well) */}
      <style>{`
        input[type=range] { -webkit-appearance: none; background: transparent; }
        input[type=range]::-webkit-slider-thumb {
          -webkit-appearance: none; height: 16px; width: 16px; border-radius: 50%;
          background: white; cursor: pointer; margin-top: -6px;
          box-shadow: 0 0 10px #ffffff, 0 0 20px #22d3ee;
        }
        input[type=range]::-webkit-slider-runnable-track {
          width: 100%; height: 4px; cursor: pointer;
          background: linear-gradient(90deg, #22d3ee, #a855f7);
          border-radius: 2px;
        }
      `}</style>

      {/* 3D Glass Card */}
      <motion.div
        style={{ rotateX, rotateY, transformStyle: "preserve-3d" }}
        className="relative z-10 w-full max-w-2xl bg-white/5 backdrop-blur-2xl border border-white/10 rounded-3xl p-8 md:p-12 shadow-2xl"
        initial={{ opacity: 0, scale: 0.9 }}
        animate={{ opacity: 1, scale: 1 }}
        transition={{ duration: 0.8, ease: "easeOut" }}
        onMouseMove={handleMouseMove}
        onMouseLeave={() => { x.set(0); y.set(0); }}
      >
        <motion.h2 
          className="text-4xl font-bold text-center mb-10 bg-gradient-to-r from-white via-cyan-200 to-purple-200 bg-clip-text text-transparent"
          initial={{ y: -20, opacity: 0 }}
          animate={{ y: 0, opacity: 1 }}
          transition={{ delay: 0.2 }}
        >
          Career Configuration
        </motion.h2>

        <form onSubmit={handleSubmit} className="space-y-8">
            
            {/* Sliders Grid */}
            <div className="space-y-6">
                <InputGroup delay={0.3} label="Financial Stability" value={formData.financialStability}>
                    <input type="range" min="1" max="5" name="financialStability" value={formData.financialStability} onChange={handleChange} className="w-full" />
                </InputGroup>

                <InputGroup delay={0.4} label="Job Security" value={formData.jobSecurity}>
                    <input type="range" min="1" max="5" name="jobSecurity" value={formData.jobSecurity} onChange={handleChange} className="w-full" />
                </InputGroup>
            </div>

            {/* Selects Grid */}
            <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
                <SelectGroup delay={0.5} label="Location Preference">
                    <select name="location" value={formData.location} onChange={handleChange} 
                        className="w-full bg-black/40 border border-white/10 rounded-xl px-4 py-3 text-cyan-100 focus:outline-none focus:ring-2 focus:ring-cyan-400 transition-all">
                        <option value="local">Local</option>
                        <option value="national">National</option>
                        <option value="abroad">International</option>
                        <option value="conditional">Conditional</option>
                    </select>
                </SelectGroup>

                <SelectGroup delay={0.6} label="Migration Willingness">
                    <select name="migration" value={formData.migration} onChange={handleChange} 
                        className="w-full bg-black/40 border border-white/10 rounded-xl px-4 py-3 text-purple-100 focus:outline-none focus:ring-2 focus:ring-purple-400 transition-all">
                        <option value="yes">Yes</option>
                        <option value="no">No</option>
                        <option value="depends">Conditional</option>
                    </select>
                </SelectGroup>
            </div>

            {/* Inputs */}
            <motion.div 
                initial={{ opacity: 0 }} animate={{ opacity: 1 }} transition={{ delay: 0.7 }}
                className="relative group"
            >
                <label className="text-xs font-semibold tracking-wider text-gray-400 uppercase mb-2 block">Max Annual Tuition</label>
                <div className="relative">
                    <span className="absolute left-4 top-3 text-gray-400">$</span>
                    <input type="number" name="maxTuition" value={formData.maxTuition} onChange={handleChange} 
                        className="w-full bg-black/40 border border-white/10 rounded-xl pl-8 pr-4 py-3 text-white focus:outline-none focus:border-cyan-400 transition-all" />
                </div>
            </motion.div>

            <InputGroup delay={0.8} label="Risk Tolerance" value={formData.riskTolerance}>
                <input type="range" min="1" max="5" name="riskTolerance" value={formData.riskTolerance} onChange={handleChange} className="w-full" />
            </InputGroup>

            {/* Action Button */}
            <motion.button 
                whileHover={{ scale: 1.02, boxShadow: "0 0 20px rgba(34, 211, 238, 0.4)" }}
                whileTap={{ scale: 0.98 }}
                className="w-full py-4 mt-4 bg-gradient-to-r from-cyan-500 to-purple-600 rounded-xl font-bold text-lg tracking-wider uppercase transition-all relative overflow-hidden group"
                type="submit" disabled={loading}
            >
                <div className="absolute inset-0 bg-white/20 translate-y-full group-hover:translate-y-0 transition-transform duration-300" />
                {loading ? (
                    <div className="flex items-center justify-center gap-2">
                        <div className="w-5 h-5 border-2 border-white/30 border-t-white rounded-full animate-spin" />
                        <span>Processing AI...</span>
                    </div>
                ) : 'Analyze Path'}
            </motion.button>
        </form>

        {/* Results Modal */}
        <AnimatePresence>
            {result && (
                <motion.div 
                    initial={{ opacity: 0, height: 0, y: 20 }}
                    animate={{ opacity: 1, height: 'auto', y: 0 }}
                    exit={{ opacity: 0, height: 0, y: 20 }}
                    className="mt-8 overflow-hidden"
                >
                    <div className="bg-gradient-to-br from-green-500/10 to-cyan-500/10 border border-cyan-500/30 rounded-2xl p-6 text-center backdrop-blur-md">
                        <motion.div 
                            initial={{ scale: 0 }} animate={{ scale: 1 }} 
                            className="text-5xl mb-4"
                        >
                            🎯
                        </motion.div>
                        <h3 className="text-2xl font-bold text-white mb-2">
                            Recommended: <span className="text-cyan-400">{result.prediction.recommended_path}</span>
                        </h3>
                        <div className="flex justify-center gap-4 my-4">
                             <div className="bg-white/5 px-4 py-2 rounded-lg border border-white/10">
                                <p className="text-xs text-gray-400 uppercase">Match Score</p>
                                <p className="text-xl font-bold text-green-400">{result.prediction.score}%</p>
                             </div>
                        </div>
                        <p className="text-sm text-gray-300">{result.prediction.match_reason}</p>
                    </div>
                </motion.div>
            )}
        </AnimatePresence>
      </motion.div>
    </div>
  );
};

// Sub-components for cleaner code
const InputGroup = ({ children, delay, label, value }: any) => (
    <motion.div 
        initial={{ opacity: 0, x: -10 }} animate={{ opacity: 1, x: 0 }} transition={{ delay }}
        className="group"
    >
        <div className="flex justify-between items-center mb-2">
            <label className="text-xs font-semibold tracking-wider text-gray-400 uppercase group-hover:text-cyan-400 transition-colors">{label}</label>
            <span className="text-xs font-mono bg-white/10 px-2 py-0.5 rounded text-cyan-300">{value}/5</span>
        </div>
        {children}
    </motion.div>
);

const SelectGroup = ({ children, delay, label }: any) => (
    <motion.div 
        initial={{ opacity: 0, x: 10 }} animate={{ opacity: 1, x: 0 }} transition={{ delay }}
    >
        <label className="text-xs font-semibold tracking-wider text-gray-400 uppercase mb-2 block">{label}</label>
        {children}
    </motion.div>
);

export default ParentForm;